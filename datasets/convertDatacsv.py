import csv

with open("D:/VIISem/knowledgeGraphUsingMondo/datasets/disease_names_clintrials.txt", "r") as file:
    lines = file.readlines()

delimiter = "\t"

with open("D:/VIISem/knowledgeGraphUsingMondo/datasets/disease_names.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    header = ["DiseaseName", "SourceName", "ConceptID", "SourceID", "DiseaseMIM", "LastModified", "Category"]
    csvwriter.writerow(header)

    for line in lines:
        fields = line.strip().split(delimiter)
        csvwriter.writerow(fields)

print("Data converted to CSV.")


with open("D:/VIISem/knowledgeGraphUsingMondo/datasets/gene_conditions.txt", "r") as file:
    lines = file.readlines()

delimiter = "\t"

with open("D:/VIISem/knowledgeGraphUsingMondo/datasets/gene_conditions.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    header = ["GeneID", "AssociatedGenes", "RelatedGenes", "ConceptID", "DiseaseName", "SourceName", "SourceID", "DiseaseMIM", "LastUpdated"]
    csvwriter.writerow(header)

    for line in lines:
        fields = line.strip().split(delimiter)
        csvwriter.writerow(fields)

print("Data converted to CSV.")