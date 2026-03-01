import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler

# 1. Load the Aggregated Data you created in Task 1
df = pd.read_csv('data/task7_subscription_aggregated.csv')
data = df[df['SubscriptionID'] == 0]['avg_cpu'].values.reshape(-1, 1) # Training on Sub 0 first

# 2. Scale data (Crucial for LSTM convergence)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# 3. Create Sequences (Lookback = 12 steps / 1 hour)
def create_sequences(data, seq_length):
    x, y = [], []
    for i in range(len(data) - seq_length):
        x.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(x), np.array(y)

X, y = create_sequences(scaled_data, 12)
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32)

# 4. Define the LSTM Architecture
class ProactiveLSTM(nn.Module):
    def __init__(self):
        super(ProactiveLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=64, num_layers=2, batch_first=True)
        self.linear = nn.Linear(64, 1)
        
    def forward(self, x):
        out, _ = self.lstm(x)
        return self.linear(out[:, -1, :])

model = ProactiveLSTM()
print("Model initialized: Ready to predict t+1 (5-minute lead time)")