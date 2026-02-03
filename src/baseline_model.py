import pandas as pd
import numpy as np
import os

def generate_baselines():
    input_path = 'data/week4_bursty_subset.csv'
    output_path = 'data/task2_baselines.csv'
    
    if not os.path.exists(input_path):
        print("Error: Run data_loader.py first to create the subset!")
        return

    df = pd.read_csv(input_path)
    
    # 1. Baseline Prediction: Sliding Window Average (Window Size = 12, i.e., 1 hour)
    # This satisfies the requirement for a 'justified baseline predictor' 
    print("--- Generating Sliding Window Baselines ---")
    
    # Sort to ensure time-series integrity
    df = df.sort_values(['vmid', 'time_step'])
    
    # Calculate the moving average of the last 12 steps (1 hour of data)
    df['cpu_ma_1h'] = df.groupby('vmid')['cpu_norm'].transform(lambda x: x.rolling(window=12, min_periods=1).mean())
    
    # 2. Baseline Policy: Reactive Threshold 
    # If the moving average is > 70%, we 'scale up' (1). If < 20%, 'scale down' (-1).
    df['scaling_action'] = 0
    df.loc[df['cpu_ma_1h'] > 0.7, 'scaling_action'] = 1
    df.loc[df['cpu_ma_1h'] < 0.2, 'scaling_action'] = -1
    
    # 3. Ground Truth (The 'Target' for future ML models)
    # We want to predict the CPU 1 step (5 mins) into the future
    df['target_next_cpu'] = df.groupby('vmid')['cpu_norm'].shift(-1)
    
    # Drop rows where we don't have a future target
    df = df.dropna(subset=['target_next_cpu'])
    
    df.to_csv(output_path, index=False)
    print(f"--- Task 2 Complete: Created {output_path} ---")

if __name__ == "__main__":
    generate_baselines()