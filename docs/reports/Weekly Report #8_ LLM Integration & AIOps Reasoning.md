**Weekly Report \#8: LLM Integration & AIOps Reasoning**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**03/08//26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives:**

* Transition the simulation from individual VM traces to 51 subscription-level clusters to reflect realistic multi-tenant cloud environments.  
* Integrate the Proactive Selection Module into the simulation engine to utilize t+300s look-ahead predictions.  
* Resolve critical NameError and KeyError bugs within the simulation\_engine.py logic.  
* Formalize the mathematical System Model and reward function within the IEEE Overleaf manuscript.

**Updates:**

* Developed and successfully integrated a SelectionModule class that triggers "Scale Up" or "Scale Down" actions based on predicted demand rather than current telemetry.  
* Implemented a robust data-handling loop in the simulation engine that uses index-based enumeration to resolve column naming conflicts like time\_step.  
* Updated the IEEE Overleaf project to include the formal reward function R and the piecewise logic for proactive scaling decisions.  
* Documented the transition to subscription-level aggregation, which provides the high-fidelity signals necessary for the AI controller to beat the provisioning delay.

Key Results:

* Successfully verified the integration of the proactive controller. The simulation now processes all 51 subscription clusters and outputs a unified performance metric:
```bash
PS C:\\Users\\jayde\\...\\cp395\> python src/simulation\_engine.py  
\--- Task 8: Proactive Simulation Complete \---  
Average System Reward: \-7.8848
```

* System Reward Benchmarking: The reward of \-7.8848 serves as the new baseline for the aggregated environment.  
* Lead-Time Accuracy: Verified that the simulator correctly enforces the 300s provisioning delay while receiving **t+1** predictions from the selection module.  
* Forecasting Comparison: Established initial MSE benchmarks: ARIMA reached 1.8138, while the high-epoch LSTM recorded 515.9697, signalling a need for regularization.

Issues & Next Steps:

* Issues resolved this week:  
  * NameError: SelectionModule: Resolved by modularizing the selection logic directly within the engine script.  
  * KeyError: 'time\_step': Fixed by implementing a safe enumerator that handles diverse CSV headers in the aggregated dataset.  
  * Author Metadata: Cleaned the Overleaf template by removing placeholder "Michael Shell" comments and generic "Starter File" text.  
* Next week:  
  * Optimize LSTM Performance: Implement Dropout layers and Early Stopping to address the current overfitting (MSE 515.9) and bring the reward closer to zero.  
  * Result Visualization: Generate a comparative MSE/Reward table in the LaTeX manuscript to visualize the improvement of the proactive AI over the reactive baseline.

**Links**

Overleaf: [IEEE Template](https://www.overleaf.com/2426641163hqmwfhksfxxs#29cd37)  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Proactive\_lstm.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/proactive_lstm.py)  
Selection\_module.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/selection_module.py)  
Simulation\_engine.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/simulation_engine.py)  
Week 8 Outcomes: [Data](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/data/task8_proactive_results.csv)

