**Weekly Report \#10**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**03/13//26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives:**

* Conduct a Full Cluster Sweep across all 51 subscription-level clusters.  
* Quantify the Generalization Gap between localized and global model performance.  
* Analyze the impact of workload variability on forecasting accuracy.

**Updates:**

* Full Sweep Execution: Developed src/full\_sweep.py to iterate through the Azure dataset.  
* Robust Sequence Handling: Implemented error-handling to manage clusters with insufficient data points, successfully processing 50 out of 51 clusters.  
* Global Evaluation: Identified a significant discrepancy between localized tuning and global performance.

#### **Key Results: The Generalization Gap**

| Environment | MSE | Status |
| :---- | :---- | :---- |
| Subscription 0 (Localized) | 69.5495 | Optimized / Specialist |
| Global Average (50 Clusters) | 2247.5204 | Generalization Failure |

**Analysis:**  
The Global MSE (2247.52) is significantly higher than the Localized MSE (69.54). This confirms that a single LSTM model trained on one subscription cannot effectively generalize across the diverse workload patterns of a multi-tenant cloud environment without federated learning or cluster-specific weights.

**Sensitivity Analysis:**  
The experiment revealed that the model is highly sensitive to Workload Volatility.

* Low Volatility (Sub 0): High accuracy, stable rewards.  
* High Volatility (Global): The model misses burst peaks, leading to high MSE and potential SLA violations.  
* System Constraint: The stagnant System Reward (-7.8848) confirms that forecasting accuracy is secondary to Provisioning Latency (300s). Even with a perfect forecast, the "Spin-up" time of a VM creates a reward ceiling.

**5\. Next Steps (Final Phase)**

* Manuscript Construction: Begin the "Results and Discussion" section of the IEEE paper, using the Generalization Gap as the primary narrative.  
* Final Tuning: Attempt a "Global Training" run where the model sees data from all 50 clusters during training to see if the Global MSE can be lowered.

**Links**  
Overleaf: [IEEE Template](https://www.overleaf.com/2426641163hqmwfhksfxxs#29cd37)  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Simulation\_engine.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/simulation_engine.py)  
Full\_sweep.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/full_sweep.py)  
