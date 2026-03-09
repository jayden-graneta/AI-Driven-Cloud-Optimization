import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA

# Load your aggregated subscription data
df = pd.read_csv('data/task7_subscription_aggregated.csv')
# Select one Subscription ID to compare models
subset = df[df['SubscriptionID'] == 0]['avg_cpu'].values

# Split: 80% train, 20% test
train_size = int(len(subset) * 0.8)
train, test = subset[0:train_size], subset[train_size:]

# 1. Moving Average Baseline
window = 12
ma_pred = [np.mean(train[i-window:i]) if i >= window else np.mean(train) for i in range(len(subset))]
ma_mse = mean_squared_error(test, ma_pred[train_size:])

# 2. ARIMA Baseline
arima_model = ARIMA(train, order=(5,1,0))
arima_fit = arima_model.fit()
arima_pred = arima_fit.forecast(steps=len(test))
arima_mse = mean_squared_error(test, arima_pred)

print(f"--- Comparative Results ---")
print(f"Moving Average MSE: {ma_mse:.4f}")
print(f"ARIMA MSE: {arima_mse:.4f}")
# Placeholder for your LSTM MSE result
print(f"Proactive LSTM MSE: [Run your model to get this value]")