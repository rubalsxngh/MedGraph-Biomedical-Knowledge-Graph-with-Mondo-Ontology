import requests

#downloading the disease names dataset
url = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/disease_names"

response = requests.get(url)

if response.status_code == 200:
    with open("D:/VIISem/knowledgeGraphUsingMondo/datasets/disease_names_clintrials.txt", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")


#downloading the gene conditions dataset

url= "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/gene_condition_source_id"

response = requests.get(url)

if response.status_code == 200:
    with open("D:/VIISem/knowledgeGraphUsingMondo/datasets/gene_conditions.txt", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")