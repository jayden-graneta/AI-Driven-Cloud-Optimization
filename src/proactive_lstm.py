import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# 1. Define Model
class ProactiveLSTM(nn.Module):
    def __init__(self, input_size=1, hidden_size=64, num_layers=2):
        super(ProactiveLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_size, 1)
    def forward(self, x):
        out, _ = self.lstm(x)
        return self.linear(out[:, -1, :])

# 2. Data Prep
df = pd.read_csv('data/task7_subscription_aggregated.csv')
data = df[df['SubscriptionID'] == 0]['avg_cpu'].values.reshape(-1, 1)
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

# Ensure split leaves enough room for sequences
train_size = int(len(data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size - 12:] # Include overlap for the first sequence

def create_sequences(data, seq_length):
    x, y = [], []
    for i in range(len(data) - seq_length):
        x.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(x), np.array(y)

X_train, y_train = create_sequences(train_data, 12)
X_test, y_test = create_sequences(test_data, 12)

# FORCE 3D SHAPE: [Samples, TimeSteps, Features]
X_train = torch.tensor(X_train, dtype=torch.float32)
if X_train.dim() == 2: X_train = X_train.unsqueeze(-1)

X_test = torch.tensor(X_test, dtype=torch.float32)
if X_test.dim() == 2: X_test = X_test.unsqueeze(-1)

y_train = torch.tensor(y_train, dtype=torch.float32)

# 3. Training Loop
model = ProactiveLSTM(hidden_size=128) 
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001) # Lower learning rate for stability

print("Training LSTM with enhanced parameters...")
for epoch in range(500): # Increased to 500
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    if (epoch+1) % 100 == 0:
        print(f"Epoch {epoch+1}/500, Loss: {loss.item():.6f}")
        
# 4. Evaluation
model.eval()
with torch.no_grad():
    predictions = model(X_test).numpy()

predictions_rescaled = scaler.inverse_transform(predictions)
y_test_rescaled = scaler.inverse_transform(y_test.reshape(-1, 1))

lstm_mse = mean_squared_error(y_test_rescaled, predictions_rescaled)
print(f"\n--- Week 08 Task 1: Comparative Results ---")
print(f"Moving Average MSE: 36.3726")
print(f"ARIMA MSE (Baseline): 1.8138")
print(f"Proactive LSTM MSE: {lstm_mse:.4f}")