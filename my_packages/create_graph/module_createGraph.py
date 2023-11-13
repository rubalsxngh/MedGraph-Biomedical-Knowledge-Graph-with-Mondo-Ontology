"""
this file contains helper functions to convert datafram suitable to upload on neo4J
and a function load_gh() that deploys the data onto neo4J sandbox,
this function also return the different labels of nodes upload on neo4j
"""



def get_p31(row):
    import pywikibot
    from pywikibot import WikidataBot
    
    itempage = pywikibot.ItemPage(WikidataBot, row)
    itemdata = itempage.get()
    try:
        target = itemdata['claims']['P31'][0].getTarget()
        target.get()
        return target.labels['en']
    except:
        return 'Unknown'
    

def add_nodes(conn, rows, batch_size=10000):

    query = '''UNWIND $rows AS row
               MERGE (:Node {name: row.name, id: row.id, type: row.node_label})
               RETURN count(*) as total
    '''
    return insert_data(conn, query, rows, batch_size)


def add_edges(rows, batch_size=50000):
    
    
    query = """UNWIND $rows AS row
               MATCH (src:Node {id: row.source_q}), (tar:Node {id: row.target_q})
               CREATE (src)-[:%s]->(tar)
    """ % edge
    
    return insert_data(query, rows, batch_size)


def insert_data(conn, query, rows, batch_size = 10000):
    import time

    total = 0
    batch = 0
    start = time.time()
    result = None

    while batch * batch_size < len(rows):

        res = conn.query(query, parameters={'rows': rows[batch*batch_size:(batch+1)*batch_size].to_dict('records')})
        try:
            total += res[0]['total']
        except:
            total += 0
        batch += 1
        result = {"total":total, "batches":batch, "time":time.time()-start}
        print(result)

    return result


"""
the function load_gh takes connection detials and dataframe as an input and 
loads the dataframe to neo4j
"""
def load_gh(uri, passw, df):

    #establishing a neo4j connection
    from neo4j import GraphDatabase
    import pandas as pd
    conn = GraphDatabase.driver(uri, auth=("neo4j", passw))

    #converting dataframe to nodes->rel->target and removing all the duplicates
    source_df = df[['source_name', 'source_q']].drop_duplicates()
    source_df.columns = ['name', 'id']
    target_df = df[['target_name', 'target_q']].drop_duplicates()
    target_df.columns = ['name', 'id']
    all_nodes_df = pd.concat([source_df, target_df]).drop_duplicates()
    all_nodes_df.shape

    all_nodes_df['node_label'] = all_nodes_df['id'].map(get_p31)
    
    add_nodes(conn, all_nodes_df)

    edge_ls = df['rel_name'].unique().tolist()

    for edge in edge_ls:
        y = df[df['rel_name'] == edge]
        add_edges(y)
    
    y = all_nodes_df['node_label'].value_counts()
    return y