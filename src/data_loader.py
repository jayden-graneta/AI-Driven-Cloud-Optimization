import pandas as pd
import os
import requests
import tqdm

def setup_directories():
    """Ensure data and docs folders exist."""
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('docs/figures', exist_ok=True)

def ingest_azure_telemetry():
    # URL for the first high-resolution CPU readings file (1 of 195)
    # This satisfies the "Filtering Strategy" requirement to avoid memory overflow.
    cpu_url = "https://azurepublicdatasettraces.blob.core.windows.net/azurepublicdatasetv2/trace_data/vm_cpu_readings/vm_cpu_readings-file-1-of-195.csv.gz"
    raw_path = 'data/raw/vm_cpu_readings-file-1.csv.gz'
    output_path = 'data/week4_bursty_subset.csv'

    # Step 1: Download the file if it doesn't exist
    if not os.path.exists(raw_path):
        print(f"--- Downloading high-res telemetry (approx. 150MB) ---")
        response = requests.get(cpu_url, stream=True)
        with open(raw_path, "wb") as f:
            for data in response.iter_content(chunk_size=1024):
                f.write(data)
    
    # Step 2: Load into Pandas
    # Schema: timestamp, vmid, min_cpu, max_cpu, avg_cpu
    print("--- Reading dataset and calculating burstiness ---")
    cols = ['timestamp', 'vmid', 'min_cpu', 'max_cpu', 'avg_cpu']
    df = pd.read_csv(raw_path, compression='gzip', names=cols)

    # Step 3: Filtering Strategy (Supervisor Action Item)
    # We calculate the Coefficient of Variation (CV = std/mean) to find bursty VMs
    vm_stats = df.groupby('vmid')['avg_cpu'].agg(['std', 'mean'])
    vm_stats['cv'] = vm_stats['std'] / (vm_stats['mean'] + 0.1) # 0.1 prevents div by zero
    
    # Select the top 500 burstiest VMs
    bursty_vms = vm_stats.sort_values(by='cv', ascending=False).head(500).index
    df_filtered = df[df['vmid'].isin(bursty_vms)].copy()

    # Step 4: Cleaning and Normalization
    df_filtered['cpu_norm'] = df_filtered['avg_cpu'] / 100.0
    # Azure V2 readings are every 300 seconds (5 minutes)
    df_filtered['time_step'] = df_filtered['timestamp'] // 300
    
    # Sort for time-series consistency
    df_filtered = df_filtered.sort_values(['vmid', 'time_step'])

    # Step 5: Save the processed research subset
    df_filtered.to_csv(output_path, index=False)
    print(f"--- Success! Created {output_path} with {len(df_filtered)} records ---")
    print(f"--- Filtered for the top 500 burstiest VMs out of {df['vmid'].nunique()} total ---")

if __name__ == "__main__":
    setup_directories()
    ingest_azure_telemetry()