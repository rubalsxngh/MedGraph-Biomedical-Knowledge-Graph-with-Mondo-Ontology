import tkinter as tk
from tkinter import Tk, Text, END
import os

# Initialize the Tkinter root window
root = Tk()

# Get the current working directory and replace backslashes with forward slashes
cwd_path = os.getcwd()
cwd_path = cwd_path.replace("\\", "/")

# Labels for user input
tk.Label(root, text='Disease Name').grid(row=0)
tk.Label(root, text='No. of Articles').grid(row=1)
tk.Label(root, text='Neo4J Sandbox Bolt URL').grid(row=2)
tk.Label(root, text='Neo4J Sandbox Password').grid(row=3)

# Entry widgets for user input
disease_name = tk.Entry(root)
no_of_disease = tk.Entry(root)
neo4j_url = tk.Entry(root)
neo4j_password = tk.Entry(root)

disease_name.grid(row=0, column=1)
no_of_disease.grid(row=1, column=1)
neo4j_url.grid(row=2, column=1)
neo4j_password.grid(row=3, column=1)

# Text widget for displaying status updates
status_text = Text(root, height=5, width=40)
status_text.grid(row=4, column=0, columnspan=2, pady=10)

# Function to update the status text widget
def update_status(message):
    status_text.insert(END, message + "\n")
    status_text.see(END)

# Function to handle the "Knowledge Graph" button click
def openFile():
    from my_packages.get_document import module_get_document
    from my_packages.get_knowledgeGraph import module_getKnowledgeGraph  # Fix typo in the import statement
    from my_packages.create_graph import module_createGraph

    kg_disease = disease_name.get()
    no_of_articles = no_of_disease.get()
    dataset_file_path = f"{cwd_path}/datasets/dataset.txt"  # Use an f-string for better readability

    update_status('Fetching the Documents....')
    module_get_document.get_docx(kg_disease, no_of_articles, dataset_file_path)
    update_status('Documents Fetched Successfully.....')

    log_file_path = f"{cwd_path}/output/output_log.txt"

    try:
        with open(log_file_path, 'w') as fh:
            fh.write("Welcome to the log file!")
    except Exception as e:
        print(e)

    update_status('Successfully created a Log file /output/output_log.txt')

    update_status('Creating a Knowledge graph.....')
    output_df_path = module_getKnowledgeGraph.get_gph(cwd_path, log_file_path, dataset_file_path)
    update_status('Successfully created Knowledge Graph....')
    update_status('Deploying Knowledge Graph onto Neo4J....')
    class_labels = module_createGraph.load_gh(neo4j_url.get(), neo4j_password.get(), output_df_path)

    update_status('Successfully deployed onto Neo4J....')

# "Knowledge Graph" button
create_graph_button = tk.Button(root, text='Knowledge Graph', command=openFile)
create_graph_button.grid(row=5, column=1, padx=5, pady=5, columnspan=2, sticky='n')

# "Exit" button
exit_button = tk.Button(root, text='Exit', command=root.destroy)
exit_button.grid(row=6, column=1, padx=5, pady=5, columnspan=1, sticky='s')

root.columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()
