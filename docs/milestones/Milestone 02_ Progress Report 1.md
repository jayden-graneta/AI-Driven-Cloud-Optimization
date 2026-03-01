**Milestone 02: Progress Report 1**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**02/15//26**  
**Dr. Mustafa Daraghmeh**

**Introduction:**  
The goal of this research is to optimize cloud resource scaling for bursty workloads. Traditional reactive autoscalers often suffer from a "Stability-Accuracy Gap" due to physical system constraints like provisioning lags. This project aims to implement a proactive AI-driven method to mitigate these delays.

**Data Trace:**

* Using the Microsoft Azure public VM traces, a specific subset of 500 bursty VMs was identified for testing.  
* Dataset: week4\_bursty\_subset.csv containing high-variance resource demand.  
* Volume: Initial cleaning and engineering resulted in a processed dataset of 19,114 records.  
* Key Characteristics: The workload exhibits rapid diurnal cycles and unpredictable spikes that challenge standard threshold-based policies.

**Baseline Prototyping & Initial Prototype Design:**

* Simulator: A custom trace-driven engine (simulation\_engine.py) that replays Azure traces row-by-row.  
* System Constraints: The harness strictly enforces a 300-second provisioning delay (1 timestep) and a 10-minute cooldown (2 timesteps).  
* Safety Logic: A capacity floor (geq 1.0) is enforced to maintain physical realism and prevent negative resource allocation.

**Feasibility:**

* SLA Violation Rate: 0.00%.  
* Average System Reward: \-1.23.  
* Interpretation: While the reactive policy successfully avoids SLA violations, the negative reward indicates significant resource waste (over-provisioning). This confirms the feasibility of using AI to improve cost-efficiency

**Reproducibility Plan:**

* Version Control: All code and data filters are managed in a private GitHub repository.  
* Environment Specs: A requirements.txt file is included to lock dependencies like pyyaml and pyarrow.  
* Configurations: All experiment parameters are stored in config.yaml, and a global random seed (42) is used for repeatable runs.

**AI Implementation Plan:**  
In the next phase (Weeks 8-10), I will replace the reactive baseline with a Proactive LSTM model. The objective is to predict demand spikes 5 minutes in advance to initiate provisioning before the 300s delay expires, thereby reducing the current resource waste.

**Links:**  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Simulation\_engine.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/simulation_engine.py)  
Analyze\_results.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/analyze_results.py)  
Config.yaml: [file](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/config.yaml)  
