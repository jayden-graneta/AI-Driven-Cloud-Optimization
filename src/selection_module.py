class SelectionModule:
    def __init__(self, config):
        self.up_threshold = config['thresholds']['up']
        self.down_threshold = config['thresholds']['down']
        self.provisioning_delay = 300  # 5 minutes
        
    def get_action(self, current_capacity, predicted_load):
        """
        Decision logic based on predicted load t+300s from now.
        """
        # If predicted load exceeds current capacity, scale up NOW 
        # so it's ready when the spike arrives in 300s.
        if predicted_load > (current_capacity * self.up_threshold):
            return "SCALE_UP"
        
        # If predicted load is very low, we can safely scale down.
        elif predicted_load < (current_capacity * self.down_threshold):
            return "SCALE_DOWN"
            
        return "MAINTAIN"