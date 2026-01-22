**Weekly Report \#1 Foundations & Research Scoping**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**01/15/26**  
**Dr. Mustafa Daraghmeh**

**Weekly Objectives and Status:**  
Objectives:

* Set up a version-controlled GitHub Repository for the course.  
* Create a GitHub Project Section to track progress, tasks, and roadmap for the semester.  
* Define and create an initial research problem scope and evaluation metrics  
* Identify a suitable public cloud workload dataset

Status:

* Created and initialized the GitHub Repository with a filled ReadMe File   
* Filled out the Project Board, Roadmap and Priority board on GitHub.  
* Picked a suitable database and created an initial problem statement and scope

**Decisions Made:**  
Problem Scope   
The project will focus on AI-driven autoscaling for cloud virtual machines. Autoscaling was chosen over the other options, scheduling and anomaly detection, because it was a common core cloud system problem and is supported by public traces, thus allowing for clear evaluations. The project will utilize offline, trace-driven simulation rather than a live cloud deployment for feasibility purposes.

Problem Statement: "Can an AI-driven autoscaling policy reduce SLA violations and resource over-provisioning compared to a threshold-based baseline when evaluated using Microsoft Azure public workload traces?"

Dataset Selection  
The dataset chosen for this project was the Microsoft Azure public VM workload trace. This dataset is ideal for this research project, as it contains data on VM-level CPU utilization collected from real production Azure virtual machines, making it ideal, as it will reflect realistic cloud behaviour and support autoscaling. 

Metrics:

* SLA Violations: CPU demand exceeding allocated capacity.  
* Resource Utilization: Mean/peak CPU usage. (How efficiently the allocated resources are used.)  
* Estimated Cost: Calculated based on VM size and active time.  
* Scaling stability: number of scale-up and scale-down events

Baseline Method: A reactive, threshold-based autoscaling policy (scaling up when CPU \> 80% and scaling down when CPU \< 20%) will serve as the comparison point.

**Issues/Risks & Assumptions:**  
Assumptions

* CPU utilization is assumed to be a sufficient signal for autoscaling decisions in this study.  
* The trace data is assumed to be representative of typical cloud workloads.  
* Resource allocation changes are assumed to take effect instantly in the simulation (no real-world provisioning delay).

Early Observations: Initial inspection of the dataset indicates significant variability and burstiness in CPU demand, which suggests that simple threshold-based autoscaling may lead to either over-provisioning or SLA violations.

Risks and Mitigation

* Risk: Dataset noise or missing values may affect evaluation accuracy.  
* Mitigation: Perform preprocessing and filtering before simulation.  
* Risk: Over-scoping the project with too many models or metrics.  
* Mitigation: Limit evaluation to one baseline and one AI-driven method.

**Next week's plans:**

* Literature Synthesis: Conduct a systematic search for papers on cloud resource management and ML-based autoscaling.  
* Taxonomy Building: Categorize existing AI approaches (e.g., predictive vs. reactive, RL-based vs. heuristic).  
* Deliverable: Submit the Literature Review

**Links:**  
Project Board: [GitHub Project Board](https://github.com/users/jayden-graneta/projects/6)  
Github Repository: [Repo](https://github.com/jayden-graneta/cp395)   
Dataset Source: [Microsoft Azure VM Trace](https://github.com/Azure/AzurePublicDataset)  
Problem Statement Draft: [Doc](https://docs.google.com/document/d/1KTfZ4SNzFqNn7WqOOLX753fxQSHxDGjkWysJ-T8aOeY/edit?usp=sharing)

