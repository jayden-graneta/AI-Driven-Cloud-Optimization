**Weekly Report \#11**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**03/27//26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives:**

* Transition experimental data into the formal IEEE Manuscript structure.  
* Select and generate high-impact Data Visualizations to illustrate the "Generalization Gap."  
* Draft the Methodology and Results sections based on the 51-cluster sweep conducted in Week 10\.

### **Technical Progress: Manuscript Development**

This week was dedicated to the primary "Writing Phase" of the directed study. Key sections updated in the LaTeX template include:

* Methodology (IV): Documented the final LSTM architecture, including the specific dropout rate (0.1) and the early stopping logic that stabilized the model at Epoch 52\.  
* Evaluation Plan (V): Outlined the trace-driven simulation environment and the 300s provisioning latency constraint.  
* Results & Discussion (VI): Synthesized the comparative data between ARIMA, Moving Average, and the localized vs. global LSTM performance.

### **Selected Figures & Visualizations**

I have identified and generated three primary figures to be included in the final paper:

* Figure 1: Workload Prediction vs. Actual (Sub 0): A time-series plot showing how the Optimized LSTM accurately tracks the diurnal cycles of Subscription ID 0\.  
* Figure 2: The Generalization Gap (Bar Chart): A side-by-side comparison of the Localized MSE (69.5) vs. the Global Average MSE (2247.5), visually demonstrating the "Specialist vs. Generalist" problem.  
* Figure 3: System Reward Plateau: A graph illustrating how the System Reward (R) stays stagnant at $-7.88 despite improvements in MSE, proving that provisioning latency is the dominant system bottleneck.

### **Key Results Summary** 

| Metric | Value | Significance |
| :---- | :---- | :---- |
| Localized MSE (v3) | 69.5495 | Validates architecture on specific targets. |
| Global MSE (Sweep) | 2247.5204 | Highlights the need for cluster-specific weights. |
| Avg. System Reward | \-7.8848 | Defines the impact of 300s hardware latency. |

### 

### **Issues & Next Steps**

* Issues: Balancing the technical depth of the LSTM architecture with the page constraints of the IEEE template.  
* Next Week (Week 12): \* Finalize the Conclusion and Future Work sections.  
  * Conduct a final pass on citations and bibliography.  
  * Prepare the Final Research Report and GitHub repository for submission.

**Links**  
Overleaf: [IEEE Template](https://www.overleaf.com/2426641163hqmwfhksfxxs#29cd37)  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Simulation\_engine.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/simulation_engine.py)  
Full\_sweep.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/full_sweep.py)

