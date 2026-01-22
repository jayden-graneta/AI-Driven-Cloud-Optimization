**Problem Statement Draft**   
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**01/15/26**  
**Dr. Mustafa Daraghmeh**

**Problem Context**  
One common problem with cloud computing is managing resources. This is where you have to choose between cost-effectiveness and service reliability. The "Over-provisioning vs. SLA Violation" problem is something that cloud providers and users often have to deal with. Most current autoscaling methods use static, reactive rules (like scaling up when CPU usage goes over 80%). But these methods don't work well when there are long periods of high workload or when traffic suddenly spikes. This leads to violations of the Service Level Agreement (SLA) during times of high demand that are not planned for, or waste of resources (and higher costs) during times of low demand. AI will help us figure out how much demand there will be and change the capacity to fix this problem.

**Research Question**  
"Can an AI-driven autoscaling policy reduce SLA violations and resource over-provisioning compared to a threshold-based baseline when evaluated using Microsoft Azure public workload traces?"

**System Assumptions**  
To ensure the project is feasible within the 12-week term, the following assumptions are made:

* Signal Representation: It is assumed that CPU usage is the best way to tell how busy a system is and how healthy it is.  
* Trace-Driven Simulation: Evaluation will occur through offline trace replay within a local simulation environment instead of a live production cluster.  
* Provisioning Latency: The simulation will use a standard, fixed provisioning delay to keep the focus on the scaling logic, even though real-world VM startup times can vary.  
* Workload Independence: The behaviour of the workload is fixed (determined by the trace) and is not influenced by the scaling actions themselves (open-loop simulation).

**4\. Success Metrics**  
The performance of the AI policy against the baseline will be measured using:

* SLA Violation Rate: The percentage of time steps when the actual demand for CPU power is higher than the total capacity that has been set aside.  
* Resource Utilization Efficiency: The average and highest CPU usage across all active VMs. A higher average usage without violations means better efficiency.  
* Scaling Stability: The total number of times the system has to scale up or down (to measure "flapping" and the extra work that comes with it).  
* Estimated Cost: A calculated number that comes from multiplying the number of active VMs by how long they have been active.

**Constraints**

* Timeline: This research will last only 12 weeks from January to April 2026\.  
* Budget: There will be no access to paid-for services such as cloud resources unless provided. The project will use local compute instead.   
* Cooldown times: In order to minimize excessive system oscillation and preserve realism, scaling actions will be limited by "cooldown" times.

**6\. Anticipated Challenges**

* Data Quality: Azure traces are large and may contain noise, missing values, or outliers that require significant preprocessing.  
* Model Selection: Balancing the complexity of the AI model (e.g., LSTM vs. simpler forecasting) against the 12-week development timeline.  
* Evaluation Bias: Ensuring the baseline is "strong" enough to provide a meaningful comparison so that AI improvements are legitimate and not inflated.

**7\. Non-Goals**  
During this project, we will not be attempting to do the following:

* We will not attempt to do real-time deployments on Azure VMs and live containers  
* This study will focus on VM clusters   
* This research will focus on VM autoscaling and will be serverless 

