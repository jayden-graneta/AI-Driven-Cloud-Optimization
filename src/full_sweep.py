import pandas as pd
import numpy as np
import torch
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from proactive_lstm import ProactiveLSTM 

# 1. Load Data
df = pd.read_csv('data/task7_subscription_aggregated.csv')
subscriptions = df['SubscriptionID'].unique()
all_mse = []

# 2. Load Model Safely
model = ProactiveLSTM(hidden_size=128, dropout=0.1)
model_path = 'data/best_proactive_model.pth'

if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path))
    model.eval()
    print(f"Loaded model from {model_path}")
else:
    print("Warning: best_proactive_model.pth not found. Using current weights.")

print(f"Starting Robust Sweep across {len(subscriptions)} clusters...")

for sub_id in subscriptions:
    sub_data = df[df['SubscriptionID'] == sub_id]['avg_cpu'].values.reshape(-1, 1)
    
    # FIX: Ensure we have at least 30 points to create sequences
    if len(sub_data) < 30:
        continue 
    
    try:
        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(sub_data)
        
        # Take the last 20% for testing
        test_size = int(len(scaled) * 0.2)
        test_data = scaled[-(test_size + 12):] 
        
        x_test = [test_data[i:i+12] for i in range(len(test_data)-12)]
        y_test = test_data[12:]
        
        if len(x_test) == 0: continue

        X_test_tensor = torch.tensor(np.array(x_test), dtype=torch.float32)
        
        with torch.no_grad():
            preds = model(X_test_tensor).numpy()
            preds_rescaled = scaler.inverse_transform(preds)
            actual_rescaled = scaler.inverse_transform(np.array(y_test).reshape(-1, 1))
            mse = mean_squared_error(actual_rescaled, preds_rescaled)
            all_mse.append(mse)
    except Exception as e:
        continue

# 3. Final Global Metrics
if len(all_mse) > 0:
    print(f"\n--- Week 10: Global Metrics ---")
    print(f"Global Average MSE: {np.mean(all_mse):.4f}")
    print(f"Clusters Successfully Processed: {len(all_mse)}")
else:
    print("\nNo clusters were processed. Check your data split logic.")