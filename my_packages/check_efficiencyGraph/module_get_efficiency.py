"""
this module checks the efficiency of knowlege graph deployed on neo4J
methodolgy used:
    1. check if source nodes from original df exist in output df
    2. Check if target names from original df exist as targets in output df
    3. Check if source nodes from output df exist in original df
    4. Check if target names from output df exist as targets in original df
"""
def check_ef(output_file_path, original_file_path):
    import pandas as pd

    output_df = pd.read_csv(output_file_path)
    original_df = pd.read_csv(original_file_path)


    source_check_original_to_output = original_df['source'].isin(output_df['source_name'])
    target_check_original_to_output = original_df['target'].isin(output_df['source_name'])

    result_df = pd.DataFrame({
        'source': original_df['source'],
        'source_exists_in_output': source_check_original_to_output,
        'target': original_df['target'],
        'target_exists_in_output': target_check_original_to_output
    })

    percentage_matched = result_df['source_exists_in_output'].mean() * 100
    percentage_matched_target = result_df['target_exists_in_output'].mean() * 100
    
    print("checking for original-> output")
    print("Percentage of source values matched:", percentage_matched)
    print("Percentage of target values matched:", percentage_matched_target)

