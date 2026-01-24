import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_workload_viz():
    input_file = 'data/cleaned_vmtable.csv'
    
    if not os.path.exists(input_file):
        print("Error: cleaned_vmtable.csv not found. Run preprocess.py first!")
        return

    # Load cleaned data
    df = pd.read_csv(input_file)

    # Task 2: Distribution Analysis (Workload Characterization)
    plt.figure(figsize=(10, 6))
    plt.hist(df['cpu_norm'], bins=50, color='#2ecc71', edgecolor='black', alpha=0.8)
    
    plt.title('Task 2: Azure VM Workload Characterization', fontsize=14)
    plt.xlabel('Normalized CPU Utilization (0.0 - 1.0)', fontsize=12)
    plt.ylabel('Frequency (Number of VMs)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Save to docs for your report
    os.makedirs('docs', exist_ok=True)
    plt.savefig('docs/workload_histogram.png')
    print("--- Success! Histogram saved to docs/workload_histogram.png ---")
    plt.show()

if __name__ == "__main__":
    generate_workload_viz()