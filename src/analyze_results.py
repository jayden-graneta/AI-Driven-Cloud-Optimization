import pandas as pd
df = pd.read_csv('data/task3_simulation_results.csv')

# Calculate metrics for the report
total_steps = len(df)
sla_violations = df['sla_violation'].sum()
sla_rate = (sla_violations / total_steps) * 100
avg_reward = df['reward'].mean()

print(f"--- Analysis for Progress Report 1 ---")
print(f"Total Records Processed: {total_steps}")
print(f"SLA Violation Rate: {sla_rate:.2f}%")
print(f"Average System Reward: {avg_reward:.2f}")