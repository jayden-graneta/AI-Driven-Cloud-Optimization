import pandas as pd
import numpy as np
import os

def process_vmtable():
    columns = ['vmid', 'subid', 'deployid', 'ts', 'vcpu', 'vmem', 'vssd', 'min_cpu', 'max_cpu', 'avg_cpu']
    file_path = 'data/vmtable.csv' 
    output_path = 'data/cleaned_vmtable.csv'

    if not os.path.exists(file_path):
        print(f"Error: Could not find {file_path}")
        return

    print("--- Starting Data Ingestion ---")
    # Read the file
    df = pd.read_csv(file_path, names=columns)

    # FIX: Force avg_cpu to be numeric. 'coerce' turns strings into NaN
    df['avg_cpu'] = pd.to_numeric(df['avg_cpu'], errors='coerce')

    # Drop the rows that couldn't be converted
    df_clean = df.dropna(subset=['avg_cpu']).copy()
    
    # Task 1: Normalization (Now it will work!)
    df_clean['cpu_norm'] = df_clean['avg_cpu'] / 100.0
    
    df_clean.to_csv(output_path, index=False)
    print(f"--- Success! {len(df_clean)} records saved to {output_path} ---")

if __name__ == "__main__":
    process_vmtable()