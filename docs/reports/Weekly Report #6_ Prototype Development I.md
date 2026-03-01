**Weekly Report \#6: Prototype Development I**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**02/15//26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives:**

* Set up a reliable experiment simulator using the VM data identified in Week 04  
* Create a central configuration file (config.yaml) to track all experiment settings  
* Add real-world timing constraints: 5-minute provisioning delay and 10-minute cooldown period  
* Fix environment setup issues and lock down project dependencies for Milestone 02

**Updates:**

* Built a system that replays cloud demand data row-by-row to simulate real-time conditions  
* Added a 5-minute delay between scaling decisions and actual capacity changes to match real provisioning times  
* Set a minimum capacity of 1.0 to prevent resources from incorrectly going negative  
* Moved all settings (thresholds, random seeds, system values) into a single config.yaml file for easier tracking and reproducibility

**Key Results:**

* Successfully verified the experiment simulator. Console output shows the system processed the bursty trace data and generated baseline performance metrics:  
  * (venv) PS ...\\cp395\> python src/simulation\_engine.py  
  * \--- Task 6 Complete: Results Saved with Seed 42 \---  
  *   
  * (venv) PS ...\\cp395\> python src/analyze\_results.py  
  * \--- Analysis for Progress Report 1 \---  
  * Total Records Processed: 19114  
  * SLA Violation Rate: 0.00%  
  * Average System Reward: \-1.23  
* Processed 19,114 data points from the Azure dataset  
* Achieved 0.00% SLA violations (system is safe but not optimized)  
* Average reward of \-1.23 shows resource waste during idle periods, which is the target for improvement

**Issues & Next Steps:**  
**Issues resolved this week:**

* PowerShell blocked virtual environment activation → Fixed using Set-ExecutionPolicy RemoteSigned  
* Config file caused errors → Fixed indentation and structure in config.yaml

**Next week:**

* Submit Progress Report 1 (Milestone 02\) with this week's metrics  
* Start Task 7: Build an LSTM model to predict demand spikes 5 minutes ahead and reduce the \-1.23 reward deficit

**Links:**  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Simulation\_engine.py: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/simulation_engine.py)  
Analyze\_results.py: [Script](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/src/analyze_results.py)  
Config.yaml: [file](https://github.com/jayden-graneta/AI-Driven-Cloud-Optimization/blob/main/config.yaml)  
