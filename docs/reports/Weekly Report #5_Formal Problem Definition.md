**Weekly Report \#5:Formal Problem Definition**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**02/08/26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives and Status:**  
Objectives:

* Define Formal MDP: Translate the autoscaling problem into a Markov Decision Process (MDP), including state, action, and reward definitions.  
* Integrate Constraints: Specify system constraints such as SLA requirements, 300-second provisioning delays, and 10-minute cooldowns within the controller logic.  
* Address Negative Capacity: Fix the logic error identified in Week 04, where the baseline allowed capacity to drop below zero.  
* Proactive Logic Research: Begin designing the proactive prediction loop to mitigate the "Provisioning Delay Paradox" observed in the baseline evaluation.

Status:

* Reward Function Design: Implemented a penalized cost function: *Reward \= \-(Waste) \- (SLA\_Violation times 10\) \- (Stability\_Penalty).* This addresses the Stability-Accuracy Gap by punishing "jittery" scaling actions.  
* State Space Definition: Defined the state *S\_t* as a 12-step sliding window of historical CPU utilization to capture bursty patterns.  
* Logic Correction: Added a min\_capacity floor of 0.5 units in src/simulation\_engine.py to prevent the physically impossible "negative capacity" results seen in the previous week's pilot runs.

**Decisions Made**  
**Execution Log:**  
\# Task 1: Data Ingestion & Filtering  
python src/data\_loader.py  
\--- Reading dataset and calculating burstiness \---  
\--- Success\! Created data/week4\_bursty\_subset.csv with 19614 records \---  
\--- Filtered for the top 500 burstiest VMs out of 241490 total \---

\# Task 2: Baseline Model Generation  
python src/baseline\_model.py  
\--- Generating Sliding Window Baselines \---  
\--- Task 2 Complete: Created data/task2\_baselines.csv \---

\# Task 3: Simulation Engine Execution  
python src/simulation\_engine.py  
\--- Task 3 Complete: Simulation Results Saved —

**Interpretation:** The isolation of 500 bursty VMs provides a high-variance environment necessary for testing RL agents. The baseline simulation confirms that a reactive 70/20 threshold policy results in a \~14% SLA violation rate due to the 300-second provisioning delay. This failure of the baseline justifies the move to proactive AI-driven methods.

**Issues/Risks and Mitigation:**

* **Risk (Data Scale):** GitHub Desktop cannot push files larger than 100 MB, which originally included the raw Azure traces.  
* **Mitigation:** Refined the .gitignore to exclude large CSVs and intermediate results, keeping only the filtered 19,614-record research subset.  
* **Risk (Lag):** The 5-minute delay is too long for a reactive controller.  
* **Mitigation:** The "Proactive" logic planned for Week 06 will use a predictive model to trigger scaling 1-step (5 minutes) before the predicted spike.

**Next-Week Plan:**

* **Prototype Development:** Build the initial LSTM or Random Forest predictive model to forecast CPU requirements at *t+1*  
* **Experiment Harness:** Integrate the predictive model into the simulation loop to evaluate "Proactive Scaling".  
* **Performance Comparison:** Begin capturing primary metrics (Cost vs. SLA) to compare against this week's baseline.

**Artifact Links:**  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Baseline Lags: [Graph](https://github.com/jayden-graneta/cp395/blob/main/docs/figures/baseline_performance_lag.png)   
Baseline\_model.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/baseline_model.py)  
Data\_loader.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/data_loader.py)  
Evaluate\_baselines.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/evaluate_baselines.py)  
Simulation\_engine.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/simulation_engine.py)