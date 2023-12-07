"""
this module checks the efficiency of knowlege graph deployed on neo4J
methodolgy used:
    1. check if source nodes from original df exist in output df
    2. Check if target names from original df exist as targets in output df
    3. Check if source nodes from output df exist in original df
    4. Check if target names from output df exist as targets in original df
"""
def check_ef(dataset, entities_list):



    def get_ner_list(text):
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
            

        #3. entity extraction
        target_entity_types = ["DISEASE", "GENE", "RNA", "DNA", "DRUG", "CHEMICAL", "CELL_LINE", "CELL_TYPE", "PROTEIN", "PATHWAY", "MUTATION", "ORGAN", "TISSUE", "SYMPTOM", "SPECIES"]
        
        """
        * I HAVEN'T SPEND MUCH ON FEATURE ENGINEERING,  'target_entity_types' AND    
        CONTAINS TYPES OF ENTITIES I AM CONSIDERING TO BE EXTRACTED 
        """

        nlp = spacy.load("en_ner_bc5cdr_md")
        doc= nlp(text)


        ner_list= []  
        for token in doc.ents:
            if token not in ner_list and token.label_ in target_entity_types:
                ner_list.append(token)

        return ner_list
    
    

    ner_list= get_ner_list(dataset)

    ner_set = set([str(item).lower() for item in ner_list])
    entities_set = set([item.lower() for item in entities_list])

    true_positive = len(ner_set.intersection(entities_set))
    false_positive = len(ner_set - entities_set)
    false_negative = len(entities_set - ner_set)


    accuracy = true_positive / (true_positive + false_positive + false_negative)


    return accuracy

