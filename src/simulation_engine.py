import pandas as pd
import numpy as np
import yaml
import random
import os

class CloudEnv:
    def __init__(self, config):
        # Load constraints from YAML
        self.delay = config['simulation']['provisioning_delay_steps']
        self.cooldown = config['simulation']['cooldown_steps']
        self.min_capacity = config['simulation']['min_capacity']
        self.stability_penalty = 0.5 
        
    def calculate_reward(self, demand, current_capacity, action_taken):
        """
        Formal MDP Reward Function defining the trade-off between 
        Resource Waste, SLA Violations, and Stability.
        """
        # 1. SLA Violation Check (Demand exceeds supply)
        sla_violation = 1 if demand > current_capacity else 0
        
        # 2. Utilization Reward (Penalty for over-provisioning/waste)
        waste = max(0, current_capacity - demand)
        
        # 3. Stability Penalty (Cost of jittery scaling events)
        action_cost = self.stability_penalty if action_taken != 0 else 0
        
        # Final Reward Formula
        reward = -(waste) - (sla_violation * 10) - action_cost
        
        return reward, sla_violation

def load_config(path="config.yaml"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found at {path}. Please create it in the root directory.")
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def run_simulation():
    # 1. Initialize Reproducibility
    config = load_config()
    np.random.seed(config['simulation']['seed'])
    random.seed(config['simulation']['seed'])
    
    # 2. Load bursty trace data
    df = pd.read_csv('data/task2_baselines.csv')
    env = CloudEnv(config)
    results = []
    
    # Group by VM to simulate each independently
    for vmid, group in df.groupby('vmid'):
        capacity = 1.0 
        pending_actions = [] 
        last_action_step = -config['simulation']['cooldown_steps']
        
        for i, row in group.iterrows():
            t = row['time_step']
            demand = row['cpu_norm']
            action = row['scaling_action']
            
            # --- Enforce Provisioning Delay ---
            if pending_actions and (t - pending_actions[0][0]) >= env.delay:
                _, capacity_change = pending_actions.pop(0)
                capacity += capacity_change
                
                # FIX: Enforce Physical Capacity Floor (No Negative Values)
                capacity = max(env.min_capacity, capacity)
            
            # --- Predictor -> Policy Loop ---
            actual_action = 0
            if (t - last_action_step) >= env.cooldown:
                if action != 0:
                    # Logic: Scale by configured step size
                    change = config['policy']['step_size'] if action == 1 else -config['policy']['step_size']
                    pending_actions.append((t, change))
                    last_action_step = t
                    actual_action = action
            
            # --- Metrics Calculation ---
            reward, sla = env.calculate_reward(demand, capacity, actual_action)
            results.append({
                'vmid': vmid,
                'time_step': t,
                'demand': demand,
                'capacity': capacity,
                'reward': reward,
                'sla_violation': sla,
                'config_seed': config['simulation']['seed']
            })
            
    # 3. Save Results for Progress Report 1
    sim_df = pd.DataFrame(results)
    sim_df.to_csv('data/task3_simulation_results.csv', index=False)
    
    print(f"--- Task 6 Complete: Results Saved with Seed {config['simulation']['seed']} ---")

if __name__ == "__main__":
    run_simulation()