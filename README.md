# MedGraph-Biomedical-Knowledge-Graph-with-Mondo-Ontology

**Overview**
The goal of the MedGraph project is to create an extensive biological knowledge graph. The system parses medical article abstracts using BeautifulSoup from PubMed. The we use SciSpacy for Named Entity Recognition (NER) in order to extract entities. Then, to provide a more detailed understanding of biomedical ideas, semantic relations between these items are identified using the Mondo Ontology. These retrieved entities and relations are smoothly integrated into a structured DataFrame by the project. Neo4j is used to deploy the data, resulting in a strong knowledge graph that enables sophisticated queries and insights. This project provides an organized and integrated picture of biomedical information, making it a useful tool for medical researchers, scholars and practitioners.

**Project Structure**
![WorkFlow](https://i.imgur.com/C5CdBKs.png)

**Dependencies**
* bs4
* python-docx
* docx
* requests
* spacy
* pywikibot
* transformers
* rdflib
* tqdm
* pandas
* neo4j
* scispacy

**Setup**
* Open the ./main.ipynb file.
* Execute all the cells.
* Utilize various packages for specific tasks such as acquiring datasets, creating dataframes, deploying the graph, and assessing efficiency.
* Comprehensive information is embedded within the code for reference.
- Remember! To beautify the graph, run a script ./cipherQueries/cipher.txt on neo4J, in order to change node labels color

**Run Project**
* Install all the dependecies.
    ``` bash
    pip install -r requirements.txt
    pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.0.0/en_core_web_md-3.0.0.tar.gz
    pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz

* Run GUI version.
    ``` bash
    python /main_gui.py

**Ouput Sample**
![Graph output](https://i.imgur.com/rggrcuB.png)

![Cipher query example](https://i.imgur.com/1NzjULa.png)

**Contributers**
* Pratham Gangwal [Pratham Gangwal](https://github.com/gangwalp)



