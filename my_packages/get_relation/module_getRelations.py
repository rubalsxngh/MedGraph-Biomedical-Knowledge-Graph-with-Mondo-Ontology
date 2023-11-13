"""
this package is repsonsible to return a list called p_dc which has relations to P-value mappings i.e {'P11': 'is_a_medical_disease'}
"""
def get_property_id(site, property_name):
    import pywikibot
    """
    Get the Wikidata property ID (P-value) for a given property name.
    """
    params = {'action': 'wbsearchentities',
            'format': 'json',
            'language': 'en',
            'type': 'property',
            'search': property_name}
        
    request = pywikibot.data.api.Request(site=site, **params)
    result = request.submit()
        
    if result and 'search' in result:
        for item in result['search']:
            if 'id' in item:
                return item['id']
        
    return None


def map_relations(site, relations):
    """
    Map relations to their Wikidata P-values.
    """
    mapped_relations = {}
        
    for relation_name in relations:
        property_id = get_property_id(site, relation_name)
        if property_id:
            mapped_relations[property_id] = relation_name
        
    return mapped_relations


"""
In the get_rl function, we are extracting the defined relations from mondo ontology, 
and then generating the P values
"""
def get_rl():
    import pywikibot
    from rdflib import Graph, URIRef

    ontology_file = r"d:/VIISem/knowledgeGraphUsingMondo/mondoOntology/mondo.owl"
    g = Graph()
    g.parse(ontology_file, format="xml")
    owl = URIRef("http://www.w3.org/2002/07/owl#")

    query = """
        SELECT ?property
        WHERE {
            ?property a owl:ObjectProperty .
        }
    """

    results = g.query(query)
    object_properties = [str(row[0]).split('#')[-1] for row in results]
    
    p_dc = {
    'P31': 'instance_of', 'P279': 'subclass_of', 'P2293': 'is_a_medical_condition', 'P1554': 'orphanet_id', 'P486': 'MeSH_ID', 'P699': 'Disease_Ontology_ID', 'P1050': 'medical_treatment', 'P2176': 'drug_used_for_treatment', 'P2888': 'drug_interaction', 'P828': 'has_gene_location', 'P668': 'gene', 'P1199': 'drug_target', 'P2670': 'has_parts_of_the_class', 'P780': 'symptoms', 'P828': 'has_gene_location', 'P2175': 'clinical_features', 'P1120': 'affected_by', 'P486': 'MeSH_ID',  'P140': 'diseases', 'P491': 'ICD-10',  'P493': 'ICD-9'
    }

    li= [value for key, value in p_dc.items()]

    object_properties+= li


    wikidata = pywikibot.Site('wikidata', 'wikidata')
    relation_mapping = map_relations(wikidata, object_properties)
    p_dc = {property_id: relation_name for property_id, relation_name in relation_mapping.items()}

    return p_dc