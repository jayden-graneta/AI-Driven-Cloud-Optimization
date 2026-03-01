import pandas as pd
import os

def aggregate_to_sub_level(input_file, output_file):
    print(f"Loading {input_file}...")
    df = pd.read_csv(input_file)
    
    # Step 1: Create Synthetic Subscription IDs 
    # We convert 'vmid' to a numeric code first so the division works
    print("Mapping VMs to synthetic Subscription clusters...")
    df['vmid_numeric'] = df['vmid'].astype('category').cat.codes
    
    # Grouping roughly 10 VMs per 'Subscription'
    df['SubscriptionID'] = (df['vmid_numeric'] // 10).astype(int) 

    # Step 2: Aggregate by the new SubscriptionID and timestamp
    print("Aggregating resource usage...")
    # Using 'avg_cpu' as the primary signal for the LSTM
    aggregated_df = df.groupby(['SubscriptionID', 'timestamp']).agg({
        'avg_cpu': 'sum',
        'max_cpu': 'sum',
        'vmid': 'count'  # Count how many VMs are in this cluster
    }).reset_index()

    # Rename for clarity
    aggregated_df.rename(columns={'vmid': 'vm_count'}, inplace=True)
    
    print(f"Success! Created {aggregated_df['SubscriptionID'].nunique()} subscription clusters.")
    aggregated_df.to_csv(output_file, index=False)
    print(f"File saved to: {output_file}")

if __name__ == "__main__":
    input_path = 'data/week4_bursty_subset.csv'
    output_path = 'data/task7_subscription_aggregated.csv'
    
    if os.path.exists(input_path):
        aggregate_to_sub_level(input_path, output_path)
    else:
        print(f"Error: {input_path} not found.")