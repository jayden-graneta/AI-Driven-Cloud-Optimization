import pandas as pd
import numpy as np
import yaml
import os

# --- TASK 2: SELECTION MODULE CLASS ---
class SelectionModule:
    def __init__(self, config):
        # Defaulting to 80% up / 30% down if not in yaml
        self.up_threshold = config.get('policy', {}).get('up_threshold', 0.8)
        self.down_threshold = config.get('policy', {}).get('down_threshold', 0.3)
        
    def get_action(self, current_capacity, predicted_load):
        if predicted_load > (current_capacity * self.up_threshold):
            return "SCALE_UP"
        elif predicted_load < (current_capacity * self.down_threshold):
            return "SCALE_DOWN"
        return "MAINTAIN"

class CloudEnv:
    def __init__(self, config):
        self.delay = config['simulation']['provisioning_delay_steps']
        self.cooldown = config['simulation']['cooldown_steps']
        self.min_capacity = config['simulation']['min_capacity']
        self.stability_penalty = 0.5 
        
    def calculate_reward(self, demand, current_capacity, action_taken):
        sla_violation = 1 if demand > current_capacity else 0
        waste = max(0, current_capacity - demand)
        action_cost = self.stability_penalty if action_taken != 0 else 0
        reward = -(waste) - (sla_violation * 10) - action_cost
        return reward, sla_violation

def load_config(path="config.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def run_simulation():
    config = load_config()
    env = CloudEnv(config)
    selector = SelectionModule(config)
    results = []
    
    df = pd.read_csv('data/task7_subscription_aggregated.csv')
    
    # Process each Subscription
    for subid, group in df.groupby('SubscriptionID'):
        capacity = 1.0 
        pending_actions = [] 
        last_action_step = -config['simulation']['cooldown_steps']
        history = [] 

        # We use enumerate to get a safe 't' value in case 'time_step' column is missing
        for t, (idx, row) in enumerate(group.iterrows()):
            demand = row['avg_cpu'] 
            
            history.append(demand)
            if len(history) > 12:
                history.pop(0)

            # Proactive Prediction Logic
            if len(history) == 12:
                predicted_load = np.mean(history) * 1.1 
            else:
                predicted_load = demand

            # Enforce Provisioning Delay
            if pending_actions and (t - pending_actions[0][0]) >= env.delay:
                _, change = pending_actions.pop(0)
                capacity = max(env.min_capacity, capacity + change)

            # Proactive Selection
            actual_action = 0
            if (t - last_action_step) >= env.cooldown:
                decision = selector.get_action(capacity, predicted_load)
                
                if decision == "SCALE_UP":
                    change = config['policy']['step_size']
                    pending_actions.append((t, change))
                    actual_action = 1
                    last_action_step = t
                elif decision == "SCALE_DOWN":
                    change = -config['policy']['step_size']
                    pending_actions.append((t, change))
                    actual_action = -1
                    last_action_step = t

            reward, sla = env.calculate_reward(demand, capacity, actual_action)
            results.append({
                'subid': subid,
                'time_step': t,
                'demand': demand,
                'predicted_demand': predicted_load,
                'capacity': capacity,
                'reward': reward,
                'sla_violation': sla
            })
            
    sim_df = pd.DataFrame(results)
    sim_df.to_csv('data/task8_proactive_results.csv', index=False)
    print(f"--- Proactive Simulation Complete ---")
    print(f"Average System Reward: {sim_df['reward'].mean():.4f}")

if __name__ == "__main__":
    run_simulation()