import pandas as pd
import numpy as np

class CloudEnv:
    def __init__(self, provisioning_delay=1, cooldown=2, stability_penalty=0.5):
        self.delay = provisioning_delay # 1 step = 5 mins
        self.cooldown = cooldown       # 2 steps = 10 mins
        self.penalty = stability_penalty # Cost per scale event
        
    def calculate_reward(self, demand, current_capacity, action_taken):
        """
        Mathematical definition of the Reward Function.
        Goal: Maximize utilization without exceeding capacity.
        """
        # 1. SLA Violation Check
        sla_violation = 1 if demand > current_capacity else 0
        
        # 2. Utilization Reward (How close is capacity to demand?)
        # Penalty for over-provisioning (waste)
        waste = max(0, current_capacity - demand)
        
        # 3. Stability Penalty (Cost of 'Jitter')
        action_cost = self.penalty if action_taken != 0 else 0
        
        # Final Reward Formula: (Efficiency) - (SLA Penalty) - (Stability Penalty)
        reward = -(waste) - (sla_violation * 10) - action_cost
        
        return reward, sla_violation

def run_simulation():
    df = pd.read_csv('data/task2_baselines.csv')
    env = CloudEnv()
    
    results = []
    
    # Group by VM to simulate each one independently
    for vmid, group in df.groupby('vmid'):
        capacity = 1.0 # Start with 1.0 (100% of a VM)
        pending_actions = [] # Queue for provisioning delay
        last_action_step = -10
        
        for i, row in group.iterrows():
            t = row['time_step']
            demand = row['cpu_norm']
            action = row['scaling_action']
            
            # --- Enforce Provisioning Delay ---
            # Actions from 'delay' steps ago take effect now
            if pending_actions and (t - pending_actions[0][0]) >= env.delay:
                _, capacity_change = pending_actions.pop(0)
                capacity += capacity_change
            
            # --- Enforce Cooldown & Action Logic ---
            actual_action = 0
            if (t - last_action_step) >= env.cooldown:
                if action != 0:
                    # Action is proposed: +1 CPU unit or -1 CPU unit
                    # In this simulation, 1 unit = 0.5 (50% capacity)
                    change = 0.5 if action == 1 else -0.5
                    pending_actions.append((t, change))
                    last_action_step = t
                    actual_action = action
            
            reward, sla = env.calculate_reward(demand, capacity, actual_action)
            results.append({
                'vmid': vmid,
                'time_step': t,
                'demand': demand,
                'capacity': capacity,
                'reward': reward,
                'sla_violation': sla
            })
            
    sim_df = pd.DataFrame(results)
    sim_df.to_csv('data/task3_simulation_results.csv', index=False)
    print("--- Task 3 Complete: Simulation Results Saved ---")

if __name__ == "__main__":
    run_simulation()