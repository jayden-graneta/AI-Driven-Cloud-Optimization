**Weekly Report \#2: Literature Review & Research Taxonomy**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**01/15/26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives and Status:**  
Objectives:

* Develop and document a systematic search strategy for academic databases (IEEE, ACM, etc.).  
* Read and annotate 10–15 peer-reviewed papers on AI-driven cloud management.  
* Construct a research taxonomy to categorize existing scaling methodologies.  
* Identify 3–5 concrete research gaps that justify the proposed study.

Status:

* Completed systematic search log across IEEE Xplore, ACM Digital Library, and Google Scholar.  
* Annotated 12 high-quality papers focusing on workload forecasting and RL-based scaling.  
* Drafted a preliminary taxonomy table comparing Reactive, Proactive, and Hybrid methods.  
* Identified 3 actionable research gaps relevant to Azure traces and scaling stability.

**Systematic Search Strategy and Search Log:**  
While searching for academic peer-reviewed papers related to my problem scope and question, I used sites such as Google Scholar and IEEE Xplore. My search focused on system-level metrics such as SLA, cost, and latency.

| Database | Query String | Date Searched | Results | Papers Used |
| :---- | :---- | :---- | :---- | :---- |
| Google Scholar | “AI-driven autoscaling Microsoft Azure VM traces workload.” | 01/17/26 | 2,100 | 8 |
| IEEE Xplore | "AI" AND "cloud autoscaling" AND "VM" | 01/17/26 | 412 | 1 |
| Professor | n/a | 01/18/26 | 1 | 1 |

**Research Taxonomy Overview**

| Approach Category | Control Logic | Required Inputs | Primary Metrics | Key Limitations |
| :---- | :---- | :---- | :---- | :---- |
| Reactive | Heuristic Thresholds | Real-time CPU % | SLA Violation Rate | Provisioning Lag: Cannot preemptively handle bursts |
| Supervised | Time-Series (LSTM/RNN) | Historical Traces | Accuracy (RMSE), Utilization | Stability Gap: Models may trigger excessive, unstable scaling events. |
| Reinforcement | Policy Agents (RL) | System State | Cumulative Cost, Reward | Convergence: Requires long training/exploration times. |
| Cloud-Native | Micro-scaling | Container Metrics | Response Time, Latency | Noisy Neighbour: Interference on shared physical resources |

**Research Gap:**

* Metric-Aware Stability Gap: Research frequently focuses on prediction accuracy (RMSE) while ignoring the "jitter" or high frequency of scaling events that can cause production systems to become unstable.  
* Modern Dataset Realism: A large amount of RL literature still uses Google Borg traces from 2011; there is a gap in comparing these models to the more recent Microsoft Azure public virtual machine traces (2019/2021).  
* Baseline Fairness: Unoptimized static thresholds are often compared to advanced Al techniques. To determine actual performance gains, a tuned reactive baseline is required.  
* Provisioning Delay Assumption: A lot of research makes the assumption that resources are instantly available. To address this, the trace-driven simulation will include realistic provisioning lags and cool-downs

**Decisions Made:**

* The project will address the "Stability Gap" by including a penalty for frequent scaling events in the evaluation metrics.  
* The taxonomy confirms that a hybrid predictive-reactive approach is most suitable for the "bursty" nature observed in the Azure VM traces.

**Next Week's Plans (Week 03):**

* Data Engineering: Implement the ingestion and cleaning pipeline for the Azure VM dataset.  
* Workload Characterization: Extract time-series features (burstiness, diurnal cycles) and produce Exploratory Data Analysis (EDA) figures.  
* Add documentation from the problem statement and bibliography to GitHub.

**Links:**  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Annotated bibliography: [Doc](https://github.com/jayden-graneta/cp395/blob/main/docs/weekly%20tasks/Annotated%20bibliography.md)  
Milestone: [Literature Review](https://github.com/jayden-graneta/cp395/blob/main/docs/milestones/Milestone%2001_%20Literature%20Review.md) 
