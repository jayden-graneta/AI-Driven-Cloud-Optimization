import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_evaluation_report():
    df = pd.read_csv('data/task3_simulation_results.csv')
    
    # 1. Calculate Summary Metrics
    total_steps = len(df)
    total_sla_violations = df['sla_violation'].sum()
    sla_violation_rate = (total_sla_violations / total_steps) * 100
    avg_reward = df['reward'].mean()
    
    print(f"--- Week 4 Baseline Evaluation ---")
    print(f"SLA Violation Rate: {sla_violation_rate:.2f}%")
    print(f"Average Reward (Stability Adjusted): {avg_reward:.2f}")

    # 2. Visualize a Single Bursty VM (Proof of Concept)
    # Pick one VM to show the "Lag" problem
    sample_vmid = df['vmid'].unique()[5] 
    sample_data = df[df['vmid'] == sample_vmid].head(100) # Look at first 100 steps (approx 8 hours)

    plt.figure(figsize=(12, 6))
    plt.plot(sample_data['time_step'], sample_data['demand'], label='CPU Demand (Actual)', color='blue', alpha=0.6)
    plt.step(sample_data['time_step'], sample_data['capacity'], label='Allocated Capacity (Baseline)', color='red', where='post')
    
    # Highlight SLA Violations
    violations = sample_data[sample_data['sla_violation'] == 1]
    plt.scatter(violations['time_step'], violations['demand'], color='black', marker='x', label='SLA Violation (Lag)')

    plt.title(f'Baseline Performance: VM {sample_vmid}\n(Threshold 70/20 | 5-Min Delay | 10-Min Cooldown)')
    plt.xlabel('Time Step (5-Min Intervals)')
    plt.ylabel('CPU Utilization / Capacity')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Save for Weekly Report
    plt.savefig('docs/figures/baseline_performance_lag.png')
    print("--- Evaluation Plot Saved to docs/figures/baseline_performance_lag.png ---")

if __name__ == "__main__":
    sns.set_theme()
    generate_evaluation_report()