"""
this .py file is package to build a knowledge graph, the above functions are 
helper functions used at various stages throughout

*** function get_gph() is the main function
        different phases starts with a single line comment explaining that perticular phase

*** this file also contain pywikibot api key, https://www.mediawiki.org/wiki/API:Main_page, use this link to generate your own token

"""

def getItems(site, itemtitle):
    from pywikibot.data import api
    params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': itemtitle}
    request = api.Request(site=site,**params)
    return request.submit()

def getItem(site, wdItem, token):
    from pywikibot.data import api
    request = api.Request(site=site,
                          action='wbgetentities',
                          format='json',
                          ids=wdItem)    
    return request.submit()

def prettyPrint(variable):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(variable)

def write2log(output_display, data, log_file_path):
    with open(log_file_path, 'a') as fh:
        fh.write("\n")
        fh.write(output_display + "\n")
        if isinstance(data, str):
            fh.write(data + "\n")
        elif isinstance(data, (list, dict, tuple, set)):
            fh.write(str(data))
        else:
            fh.write(data.text + "")
        
        fh.write("\n")

"""
the get_gph function,
input (dataset.txt) -> ouput (nodes.csv) to deploy it to neo4J
"""

def get_gph(cwd_path, log_file_path, dataset_file_path):

    import spacy
    from spacy.lang.en.stop_words import STOP_WORDS
    from spacy.matcher import Matcher
    from spacy.tokens import Doc, Span, Token
    from transformers import BertTokenizer
    import pywikibot
    import os
    from my_packages.get_relation import module_getRelations
    from tqdm import tqdm
    import pandas as pd
    #import scispacy

    #1. load a spacy pipeline
    non_nc = spacy.load('en_core_web_md')
    nlp = spacy.load('en_core_web_md')
    nlp.add_pipe('merge_noun_chunks')

    #2. Open the dataset.txt file for reading
    with open(dataset_file_path, 'r') as file:
        text = file.read() #reading the collected dataset into a string
        

    #3. entity extraction
    target_entity_types = ["DISEASE", "GENE", "RNA", "DNA", "DRUG", "CHEMICAL", "CELL_LINE", "CELL_TYPE", "PROTEIN", "PATHWAY", "MUTATION", "ORGAN", "TISSUE", "SYMPTOM", "SPECIES"]
    
    """
    * I HAVEN'T SPEND MUCH ON FEATURE ENGINEERING,  'target_entity_types' AND    
    CONTAINS TYPES OF ENTITIES I AM CONSIDERING TO BE EXTRACTED 
    """

    nlp = spacy.load("en_ner_bc5cdr_md")
    doc= nlp(text)


    ner_list= []  #initiliazing the named entity list

    for token in doc.ents:
        if token not in ner_list and token.label_ in target_entity_types:
            ner_list.append(token)
    
    write2log("the ner_list", ner_list, log_file_path)
    
    #5. sementic extraction
    token= os.getenv("WIKIDATA_API_KEY")
    wikidata = pywikibot.Site('wikidata', 'wikidata')
    site = pywikibot.Site("wikidata", "wikidata")
    
    item_ls = [] #this list will contain the items with respected Q values i.e {'Q81': 'lymphoma}
    i = 0

    for el in ner_list:
        try:
            itemtitle = str(el).replace('-', '_') 
        except Exception as span_o:
            print(span_o)

        wikidataEntries = getItems(site, itemtitle)
        try:
            tup = (wikidataEntries['search'][0]['id'], el)
            item_ls.append(tup)
        except IndexError:
            i += 1
        

    dedup_item_ls = []
    for item in item_ls:
        if item not in dedup_item_ls:
            dedup_item_ls.append(item)
    
    write2log("Q-value extraction", dedup_item_ls, log_file_path)

    
    #6. relation extraction
    """
    the relation extraction is done at package called module_getRelations and that package 
    returns p_dc, check module_getRelations
    for more informations.
    """

    p_dc= module_getRelations.get_rl(cwd_path)
    write2log("the relations list", p_dc, log_file_path)

    #7. data frame creation
    full_node_tup_ls = []

    try:

        for el in tqdm(item_ls):
            itempage = pywikibot.ItemPage(wikidata, el[0])
            itemdata = itempage.get()
            source_node = itemdata['labels']['en']

            for key in p_dc.keys():
                try:
                    for i in itemdata['claims'][key]:
                        target = i.getTarget()
                        target_id = target.id
                        target_label = target.labels['en']
                        
                        # Check if the target exists in dedup_item_ls
                        tup = (source_node, el[0], key, p_dc[key], target_label, target_id)
                        full_node_tup_ls.append(tup)
                except:
                    continue
    
    except Exception as e:
        print('the error occured at step 7')
    
    df= pd.DataFrame(full_node_tup_ls, columns=['source_name', 'source_q', 'rel_p', 'rel_name', 'target_name', 'target_q'])
    output_df_path= cwd_path+ "/ouput/dataframe_srt.csv"
    with open(output_df_path, 'w') as fh:
        pass

    df.to_csv(output_df_path, index= False)
    
    return output_df_path


            
    
    
    

