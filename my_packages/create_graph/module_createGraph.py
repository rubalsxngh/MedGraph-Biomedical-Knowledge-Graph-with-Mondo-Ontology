"""
this file contains helper functions to convert datafram suitable to upload on neo4J
and a function load_gh() that deploys the data onto neo4J sandbox,
this function also return the different labels of nodes upload on neo4j
"""
from neo4j import GraphDatabase
from pywikibot import WikidataBot

class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, parameters=None, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query, parameters))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response

def get_p31(row):
    import pywikibot
    
    try:
        site = pywikibot.Site("wikidata", "wikidata")
        itempage = pywikibot.ItemPage(site, row)
        
        itemdata = itempage.get()
        
        # Check if 'P31' claim exists
        if 'P31' in itemdata['claims']:
            target = itemdata['claims']['P31'][0].target
            
            # Check if the target is an ItemPage
            if isinstance(target, pywikibot.ItemPage):
                return target.labels['en']
            else:
                # Handle the case where 'P31' target is not an ItemPage
                return f'Redirects to: {target.title()}'
        else:
            return 'No P31 Claim'
    
    except pywikibot.exceptions.NoPageError:
        return 'Item does not exist'
    
    except pywikibot.exceptions.IsRedirectPageError as e:
        # Handle redirect page
        return f'Redirects to: {e.title}'

    except Exception as e:
        return f'Error: {str(e)}'


    

def add_nodes(conn, rows, batch_size=10000):

    query = '''UNWIND $rows AS row
               MERGE (:Node {name: row.name, id: row.id, type: row.node_label})
               RETURN count(*) as total
    '''
    return insert_data(conn, query, rows, batch_size)



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
def load_gh(uril, passw, df_csv):

    #establishing a neo4j connection
    from neo4j import GraphDatabase
    import pandas as pd
    try:
        conn = Neo4jConnection(uri=uril, user="neo4j", pwd=passw)
    except Exception as e:
        print(e)

    df= pd.read_csv(df_csv)
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
    print

    def add_edges(rows, batch_size=50000):
    
        query = """UNWIND $rows AS row
                MATCH (src:Node {id: row.source_q}), (tar:Node {id: row.target_q})
                CREATE (src)-[:%s]->(tar)
        """ % edge
        
        return insert_data(conn, query, rows, batch_size)
    
    for edge in edge_ls:
        y = df[df['rel_name'] == edge]

        add_edges(y)
    
    y = all_nodes_df['node_label'].value_counts()
    return y