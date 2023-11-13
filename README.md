# MedGraph-Biomedical-Knowledge-Graph-with-Mondo-Ontology

**Overview**
The goal of the MedGraph project is to create an extensive biological knowledge graph. The system parses medical article abstracts using SciSpacy for Named Entity Recognition (NER) in order to extract entities. Then, to provide a more detailed understanding of biomedical ideas, semantic relations between these items are identified using the Mondo Ontology. These retrieved entities and relations are smoothly integrated into a structured DataFrame by the project. Neo4j is used to deploy the data, resulting in a strong knowledge graph that enables sophisticated queries and insights. This project provides an organized and integrated picture of biomedical information, making it a useful tool for medical researchers, scholars and practitioners.

**Dependencies**
  bs4
  python-docx
  docx
  requests
  spacy
  pywikibot
  transformers
  rdflib
  tqdm
  pandas
  neo4j
  scispacy



