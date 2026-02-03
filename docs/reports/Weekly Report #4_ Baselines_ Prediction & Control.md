**Weekly Report \#4: Baselines: Prediction & Control**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**02/01/26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives and Status:**  
Objectives:

* Using feedback from the professor, switch from static metadata (vmtable) to high-resolution time-series telemetry (vm\_cpu\_readings).  
* Implement a robust filtering strategy to handle large-scale Azure trace data.  
* Define a formal MDP (Markov Decision Process) including provisioning delays and stability penalties.  
* Establish a "Fair Baseline" performance level using threshold-based scaling with cooldowns.  
* Create a filtering strategy 

Status:

* Successfully switched from vmtable to vm\_cpu\_readings (current data set: [Azure Data Set](https://azurepublicdatasettraces.blob.core.windows.net/azurepublicdatasetv2/trace_data/vm_cpu_readings/vm_cpu_readings-file-1-of-195.csv.gz))  
* Successfully implemented a sliding window baseline predictor as well as a reactive threshold policy.  
* Successfully built a simulation engine that enforces a 300-second provisioning delay and a 10-minute cooldown.  
* Created an evaluation metric and preformance visulization showing provision delays using seaborn and matplotlib

### 

### **Decisions Made**

**Dataset & Filtering Strategy**

* **High-Res Telemetry:** Shifted to the vm\_cpu\_readings dataset. This provides the 5-minute (300s) granularity required to observe temporal bursts that scheduling averages hide.  
* **Sampling:** To manage compute resources, I implemented a Coefficient of Variation (CV) filter. I am now targeting the top 500 most "spiky" workloads, ensuring the research focuses on the hardest-to-scale scenarios.

**Constraint Standardization**

* **Fixed Provisioning Delay:** Standardized a **300-second (1 step)** delay. This reflects the realistic time for an Azure VM to transition to a "Ready" state.  
* **Cooldown Period:** Implemented a **10-minute (2 step)** cooldown. This prevents the baseline from "flapping," making it a more rigorous comparison point.

**Metric Refinement**

* **Penalized Cost:** Introduced a **Stability Penalty** for every scaling action. This addresses the "Stability-Accuracy Gap" by punishing models that achieve high accuracy through excessive, unstable scaling.  
* **Physical Constraints:** Added a "Lower Bound" constraint to the capacity logic to ensure allocated resources never drop below zero, a logic error identified during initial pilot runs.

### **Early Observations & Evaluation**

* **The Provisioning Lag:** As seen in the generated baseline\_performance\_lag.png, the reactive baseline is consistently "behind the curve." Because it only reacts once a threshold is hit, the 5-minute delay causes the system to remain in **SLA violation** for the duration of sudden bursts.  
* **Baseline Fairness:** The 10-minute cooldown successfully stabilized the red line (Capacity), but this stability comes at the cost of increased SLA violations during successive spikes.  
* **Current Baseline Stats:**  
  * **SLA Violation Rate:** \~14.2% (observed during burst heavy-traffic periods).  
  * **Average Reward:** Significantly penalized by the new stability and waste metrics.

### **Issues/Risks & Assumptions**

**Assumptions**

* A 300-second delay is assumed to be constant across all VM types for this phase of the simulation.  
* Replaying traces accurately represents real-time system dynamics.

**Risks & Mitigations**

* **Data Scale Risk:** Processing the full Azure trace (195 files) exceeds local memory. **Mitigation:** My ingestion pipeline now only processes a representative subset of 500 VMs from the first telemetry file.  
* **Negative Capacity:** Initial runs allowed capacity to drop below 0\. **Mitigation:** Enforced a min\_capacity \= 0.5 floor in src/simulation\_engine.py.

### **Next Week's Plans**

* **Model Selection:** Transition from Moving Averages to the first Al-driven method (LSTM or Random Forest).  
* **Predictive Scaling:** Implement "Proactive" logic where the model predicts the CPU state at **t+1** to initiate scaling *before* the spike occurs.  
* **LLM Integration Prep:** Begin researching the bounded LLM role for configuration reasoning.

**Terminal returns:**  
```bash
# Task 1: Data Ingestion & Filtering
$ python src/data_loader.py
--- Reading dataset and calculating burstiness ---
--- Success! Created data/week4_bursty_subset.csv with 19614 records ---
--- Filtered for the top 500 burstiest VMs out of 241490 total ---

# Task 2: Baseline Model Generation
$ python src/baseline_model.py
--- Generating Sliding Window Baselines ---
--- Task 2 Complete: Created data/task2_baselines.csv ---

# Task 3: Simulation Engine Execution
$ python src/simulation_engine.py
--- Task 3 Complete: Simulation Results Saved ---
```

**Links:**  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Baseline Lags: [Graph](https://github.com/jayden-graneta/cp395/blob/main/docs/figures/baseline_performance_lag.png)   
Baseline\_model.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/baseline_model.py)  
Data\_loader.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/data_loader.py)  
Evaluate\_baselines.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/evaluate_baselines.py)  
Simulation\_engine.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/simulation_engine.py)

