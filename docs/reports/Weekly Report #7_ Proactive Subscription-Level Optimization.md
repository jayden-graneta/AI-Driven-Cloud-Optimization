**Weekly Report \#7: Proactive Subscription-Level Optimization**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**02/15//26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives:**

* Aggregate VM traces into Subscription-level data to meet the "cluster environment" requirements from Milestone 02 feedback.  
* Initialize the formal IEEE Research Manuscript on Overleaf to begin the documentation of the proactive scaling model.  
* Develop a Proactive LSTM Prototype in PyTorch to predict demand 5 minutes ($t+1$) in advance.  
* Resolve environment-specific library conflicts (PyTorch DLL errors) to ensure the research environment is stable for training.

**Updates:**

* Built a data transformation pipeline that maps individual VMs into 51 synthetic subscription clusters, summing resource usage for a more realistic tenant-level workload.  
* Designed a 2-layer LSTM architecture with a 12-step (60-minute) lookback window to forecast the next 5-minute interval.  
* Integrated the new aggregated dataset into the project structure to serve as the training baseline for the upcoming AI controller.  
* Set up the IEEE Overleaf Project with the standard two-column conference layout, including the initial System Model and Problem Formulation.

**Key Results:**

Successfully verified the data aggregation and the AI model initialization. Console output confirms the environment is locked and the model is ready for training:

PowerShell  
(venv) PS ...\\cp395\> python src/data\_aggregation\_v2.py  
Mapping VMs to synthetic Subscription clusters...  
Success\! Created 51 subscription clusters.  
File saved to: data/task7\_subscription\_aggregated.csv

(venv) PS ...\\cp395\> python src/proactive\_lstm.py  
Model initialized: Ready to predict t+1 (5-minute lead time)  
\--- Task 7 Preliminary: Environment Stable with Seed 42 \---

* 51 Unique Workload Signals: Provides the high-fidelity data needed to move beyond the current \-1.23 reward baseline.  
* Verified Lead-Time: The model is mathematically aligned to the 300s (5-minute) provisioning delay, enabling "pre-emptive" scaling.

**Issues & Next Steps:**

**Issues resolved this week:**

* PyTorch DLL Load Failure: Fixed by performing a clean reinstall of torch using the CPU-specific Windows wheel within the venv.  
* Subscription Metadata Gap: Resolved by implementing categorical numeric mapping for vmid to create subscription groups.  
* Execution Policy: Re-applied Set-ExecutionPolicy to allow the virtual environment to handle the new AI library dependencies.

**Next week:**

* Train the LSTM model on the 51 subscription clusters and evaluate prediction accuracy (MSE).  
* Bridge the AI and Simulator: Pass the LSTM's $t+1$ predictions into the simulation\_engine.py to replace reactive threshold logic and reduce resource waste.

**Links:**

Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Data\_aggregation\_v2.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/data_aggregation_v2.py)  
Proactive\_lstm.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/proactive_lstm.py)

