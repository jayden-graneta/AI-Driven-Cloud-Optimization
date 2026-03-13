**Weekly Report \#9: Experimental Evaluation I**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**03/13//26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives:**

* Execute the first phase of Experimental Evaluation comparing Reactive, ARIMA, and LSTM models.  
* Conduct a Failure Analysis on the initial LSTM prototype to address the high MSE identified in Milestone 02 feedback.  
* Implement Regularization (Dropout & Early Stopping) to stabilize the proactive scaling logic.  
* Bridge the forecasting results with the simulation\_engine.py to evaluate the impact on System Reward (R).

### **Updates:**

* Data Aggregation: Successfully verified the 51 subscription-level clusters as the primary testing environment.  
* Model Refinement: Modified src/proactive\_lstm.py to include a 10% Dropout layer and a reduced Learning Rate (0.0005) to prevent memorization of Azure traces.  
* Ablation Study: Tested three versions of the LSTM (Initial, Regularized, and Tuned) to identify the "Sweet Spot" between bias and variance.  
* Simulation Integration: Updated compare\_models.py to programmatically ingest JSON results, ensuring a reproducible evaluation pipeline.

### **Key Results**

The primary breakthrough this week was the successful stabilization of the LSTM model. Early stopping triggered at Epoch 52, preventing the model from falling back into the "Memorization Trap" (MSE \> 400).

Terminal:

```

(venv) PS ...\\cp395\> python src/compare\_models.py

\--- Comparative Results (Baseline vs Proactive) \---

Moving Average MSE: 36.3726

ARIMA MSE:          1.8138

Proactive LSTM MSE: 69.5495 (Regularized)
```

* Improvement: Achieved a 91.2% reduction in MSE compared to the previous regularized attempt (797.8 \-\> 69.5).  
* Stability: The model now generalizes across the 20% test split of Subscription 0 without losing the signal of workload bursts.

**Model Comparison:**

| Model | MSE | Status |
| :---- | :---- | :---- |
| Arima  | 1.8138 | Strong Baseline |
| Moving Average  | 36.3726 | Weak Baseline |
| Proactive LSTM (v1) | 443.3997 | Fail: Overfitting |
| Proactive LSTM (v2) | 797.8412 | Fail: Underfitting |
| Proactive LSTM (v3) (Current) | 69.5495 | Optimized/Stable |

### **Issues & Next Steps**

* Issues Resolved:  
  * Overfitting/Underfitting Loop: Resolved by balancing Dropout (0.1) and Patience (50) to allow the model to learn without memorizing.  
  * Execution Policy: Standardized the use of Set-ExecutionPolicy \-Scope Process to ensure a consistent research environment.  
* Next Week (Evaluation II):  
  * Full Cluster Sweep: Run the optimized LSTM across all 51 clusters (not just ID: 0\) to verify global stability.  
  * Manuscript Completion: Draft the "Results & Discussion" section of the IEEE manuscript, including the MSE comparison table generated this week.

**Links**

Overleaf: [IEEE Template](https://www.overleaf.com/2426641163hqmwfhksfxxs#29cd37)  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Proactive\_lstm.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/proactive_lstm.py)  
Simulation\_engine.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/simulation_engine.py)  
Compare\_models.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/compare_models.py)

