import pandas as pd
import numpy as np
import os

def clean_data(input_path, output_path):
    print(f"--- Starting Data Ingestion: {input_path} ---")
    
    # 1. Load Data
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found. Drop your CSV in the /data folder!")
        return

    df = pd.read_csv(input_path)
    
    # 2. Basic Cleaning
    # Drop rows where essential CPU data is missing
    initial_count = len(df)
    df = df.dropna(subset=['avg_cpu'])
    print(f"Dropped {initial_count - len(df)} rows with missing CPU values.")

    # 3. Unit Normalization (Standardizing for the AI)
    # Most Azure traces are 0-100. AI models prefer 0.0 to 1.0.
    df['cpu_norm'] = df['avg_cpu'] / 100.0
    
    # 4. Sorting & Indexing
    # Ensure data is chronological for each VM
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df = df.sort_values(by=['vmid', 'timestamp'])

    # 5. Exporting the 'Gold' Dataset
    df.to_csv(output_path, index=False)
    print(f"--- Success! Cleaned data saved to: {output_path} ---")

if __name__ == "__main__":
    # Ensure folders exist
    os.makedirs('data', exist_ok=True)
    
    # Update 'raw_azure.csv' to the name of the file you downloaded
    clean_data('data/raw_azure.csv', 'data/cleaned_workload.csv')