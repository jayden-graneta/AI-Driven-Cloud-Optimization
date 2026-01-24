**Weekly Report \#3 Data Engineering & Workload Characterization**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**01/20/25**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives and Status**  
Objectives:

* Fix GitHub Project/Repo links and upload previous weekly files and milestones in markdown format.  
* Implement a reproducible data ingestion, and also create a cleaning pipeline for Microsoft Azure Trace v2.  
* Perform an EDA analysis to highlight workload dynamics.  
* Define input features and prediction targets for the upcoming modelling phase.

Status:

* Uploaded all reports, milestones and weekly tasks to GitHub in markdown format.  
* Processed a predefined preprocessing workflow (src/preprocess.py) capable of managing unrefined vmtable.csv information.    
* Developed an automated exploratory analysis tool (src/eda.py) for creating usage distribution visuals.  

**Decisions Made**  
**Data Ingestion & Cleaning Pipeline:**

* **Subset Selection:**  Opted for the "vmtable.csv" extract from Azure Public Dataset V2 (2019). Its comprehensive snapshot of resource setups and typical workloads makes it excellent for analyzing demand patterns. Its compact size was advantageous: rapid processing and simple transfer on my local machine.    
* **Data Type Enforcement:** Applied pd.to\_numeric, setting errors='coerce' to manage non-numeric anomalies in the initial CSV. This keeps the workflow repeatable and fully automated.    
* **Normalization:** Scaled the avg\_cpu values from percentage (0–100) to decimal (0–1), aligning with neural network input needs.  

**Feature & Label Definition:**

* **Input Features (X):** The model will initially consider vcpu and vmem as fixed features. Later versions may incorporate moving averages to reflect temporal spikes.    
* **Prediction Target (Y):**  The focus is on cpu\_norm, the transformed average CPU use.  
* **Windowing Strategy:** Suggest grouping data in 5-minute chunks to match the Azure trace's original interval.  

**Key EDA Findings:**

* **Figure 1:** The CPU usage histogram reveals extreme left skew. Most values bunch under 8%.    
* **Bimodal Load Skew:** A noticeable secondary surge near 33% hints at a distinct cluster of busier workloads compared to largely dormant "ghost" instances.    
* **Implications:** The overwhelming bulk of idle VMs (the dominant portion versus sporadic activity) implies rigid, rule-based scaling would waste enormous resources.  

**Issues/Risks & Assumptions**  
**Assumptions:** 

* The vmtable aggregate metrics are taken as reflective of wider time-based shifts. Might not hold. Variances exist. Hidden factors at play.  
* Normalizing to a (\[0, 1\]) range assumes that the peak values in the trace represent the maximum possible physical capacity for those specific VM instances.

**Issues:** 

* **Data Inconsistency:** Data types were not the same in the raw CSV file, which threw some errors into the script that I made, but was fixed by adding a line that switches the data type from string to float, which then allowed the rest of the script in [preprocess.py](http://preprocess.py) to function smoothly.  
* **Project Over-scoping:** There is a risk of over-complicating the project with excessive models; this is mitigated by limiting evaluation to one baseline (Random Forest) and one AI-driven method next week.  
* **Sampling Bias:** The vmtable snapshot may hide extreme short-term bursts; this will be mitigated by calculating peak-to-mean ratios in time-series analysis during Week 04\.

**Next Week Plan:**

* **Baseline Choice:** To address the bimodal load skew found in Task 2, choose a Random Forest Regressor as the first baseline model.
* **Model Implementation:** Implement the baseline in src/model.py and establish evaluation metrics.  
* **Time-Series Analysis:** Expand the EDA to include time-series plots of VM arrivals and execution durations to refine the prediction window.

**Links:**  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Exploratory Data Analysis: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/eda.py)  
Preprocessing Script: [Script](https://github.com/jayden-graneta/cp395/blob/main/src/preprocess.py)  
EDA Histogram: [Figure 1](https://github.com/jayden-graneta/cp395/blob/main/figures/eda_figure1.png)
