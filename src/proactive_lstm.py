import torch
import torch.nn as nn
import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# 1. Define Model with Regularization
class ProactiveLSTM(nn.Module):
    def __init__(self, input_size=1, hidden_size=64, num_layers=2, dropout=0.2):
        super(ProactiveLSTM, self).__init__()
        # Added dropout inside the LSTM layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, dropout=dropout)
        # Explicit dropout layer before the final output
        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        # Apply dropout to the last time step's output
        out = self.dropout(out[:, -1, :])
        return self.linear(out)

# 2. Data Preparation
df = pd.read_csv('data/task7_subscription_aggregated.csv')
# Standardizing on SubscriptionID 0 for the comparison baseline
data = df[df['SubscriptionID'] == 0]['avg_cpu'].values.reshape(-1, 1)
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

train_size = int(len(data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size - 12:] 

def create_sequences(data, seq_length):
    x, y = [], []
    for i in range(len(data) - seq_length):
        x.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(x), np.array(y)

X_train, y_train = create_sequences(train_data, 12)
X_test, y_test = create_sequences(test_data, 12)

X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)

# Ensure 3D shape: [Samples, TimeSteps, Features]
if X_train.dim() == 2: X_train = X_train.unsqueeze(-1)
if X_test.dim() == 2: X_test = X_test.unsqueeze(-1)

# 3. Training Loop with Early Stopping
model = ProactiveLSTM(hidden_size=128, dropout=0.1) 
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)

best_loss = float('inf')
patience = 50  # Number of epochs to wait for improvement
trigger_times = 0

print("Training LSTM with Regularization and Early Stopping...")
for epoch in range(500):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    
    # Early Stopping check
    if loss.item() < best_loss:
        best_loss = loss.item()
        trigger_times = 0
        # Save state if this is the best version yet
        torch.save(model.state_dict(), 'data/best_proactive_model.pth')
    else:
        trigger_times += 1
        if trigger_times >= patience:
            print(f"Early stopping triggered at epoch {epoch+1}")
            break

    if (epoch+1) % 50 == 0:
        print(f"Epoch {epoch+1}/500, Loss: {loss.item():.6f}")

# 4. Evaluation
model.eval()
with torch.no_grad():
    predictions = model(X_test).numpy()

predictions_rescaled = scaler.inverse_transform(predictions)
y_test_rescaled = scaler.inverse_transform(y_test.reshape(-1, 1))

lstm_mse = mean_squared_error(y_test_rescaled, predictions_rescaled)

print(f"\n--- Regularized Results ---")
print(f"Moving Average MSE: 36.3726")
print(f"ARIMA MSE (Baseline): 1.8138")
print(f"NEW Proactive LSTM MSE: {lstm_mse:.4f}")

# 5. Export Results for compare_models.py
results = {
    "lstm_mse": float(lstm_mse),
    "status": "Regularized",
    "best_loss": float(best_loss)
}
with open('data/lstm_results.json', 'w') as f:
    json.dump(results, f)
    print("\nResults saved to data/lstm_results.json")

