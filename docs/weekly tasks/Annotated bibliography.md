**Annotated bibliography**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**01/16/26**  
**Dr. Mustafa Daraghmeh**

1\. Lawrence, E. (2024). "AI-Powered Cloud Resource Management: Machine Learning for Dynamic Autoscaling and Cost Optimization."

* Problem Addressed: The inefficiency of static, rule-based autoscaling in handling the "bursty" nature of modern cloud traffic, leading to significant financial waste and performance degradation.  
* Methodology: The paper explores supervised learning models, specifically Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks, to perform time-series forecasting of resource demand.  
* Evaluation Setup: Conducted using simulated cloud environments with historical traffic data to compare predictive AI against reactive thresholds.  
* Metrics Used: Cost savings (%), CPU utilization efficiency, and prediction accuracy (RMSE).  
* Key Limitations/Trade-offs: The primary trade-off identified is the computational overhead of training deep learning models. While accuracy is high, the energy and compute cost to maintain the model can offset some of the cloud savings if not optimized.  
* Relevance to Project: Directly supports the "Proactive AI" tier of my taxonomy. It provides a blueprint for how LSTMs can outperform the threshold-based baseline I am building.

### 2\. IJAIDSML. (2024). "AI-Driven Resource Management in Cloud Environments: Predictive Models for Performance and Scalability."

* Problem Addressed: The challenge of maintaining "Quality of Service" (QoS) in multi-tenant cloud environments where resource contention is common.  
* Methodology: A comparative analysis of predictive models, focusing on Linear Regression for simple trends and Random Forests for multi-dimensional resource signals (CPU, Memory, and I/O).  
* Evaluation Setup: Utilized public cloud datasets to test model scalability as the number of virtual instances increases.  
* Metrics Used: Throughput, Latency (Response Time), and SLA compliance rates.  
* Key Limitations/Trade-offs: The study notes a "Generalization Gap"—models trained on one type of workload (e.g., web serving) perform poorly when applied to another (e.g., big data processing) without retraining.  
* Relevance to Project: This paper is crucial for my "System Assumptions" section. It highlights why using the Azure dataset (which has diverse workloads) is more robust than using synthetic data.

### 3\. Yenugula, M. (2024). "Monitoring Performance Computing Environments and Autoscaling Using AI."

* Problem Addressed: The disconnect between real-time monitoring tools and the decision-making logic of autoscalers.  
* Methodology: Proposes an integrated framework where AI acts as a "Monitoring Agent" that filters noise from system logs before triggering the scaling logic.  
* Evaluation Setup: Tested in High-Performance Computing (HPC) clusters where workload fluctuations are extreme.  
* Metrics Used: Mean Time to Repair (MTTR), Monitoring overhead (CPU% used by the AI itself), and scaling precision.  
* Key Limitations/Trade-offs: Found a significant Trade-off in Granularity: finer monitoring (second-by-second) increases scaling accuracy but consumes significant system resources, potentially slowing down the applications it aims to protect.  
* Relevance to Project: Informs my "Scaling Stability" metric. It helps justify why I will use 5-minute granularity in the Azure traces rather than 1-second data to avoid system "jitter."

### 4\. SSRN 5267834\. (2025). "Harnessing AI for Enhanced Cloud Autoscaling: A Reinforcement Learning Approach."

* Problem Addressed: The inability of predictive models to account for the *consequences* of their actions (e.g., how a scale-down event might affect latency in the next time step).  
* Methodology: Utilizes Deep Reinforcement Learning (DRL), specifically Deep Q-Networks (DQN), to learn an optimal scaling policy through a reward function that balances cost and SLA violations.  
* Evaluation Setup: Trace-driven simulation comparing RL agents against standard Kubernetes-style Horizontal Pod Autoscalers (HPA).  
* Metrics Used: Cumulative Reward, Number of SLA Violations, and Total Resource Cost.  
* Key Limitations/Trade-offs: Highlights the "Cold Start" problem. The RL agent requires an initial "exploration phase" where it makes suboptimal decisions (causing SLA violations) before it becomes smarter than the baseline.  
* Relevance to Project: This represents the "Hybrid/RL" category of my taxonomy. It provides the mathematical basis for the "SLA vs. Cost" reward function I will discuss in my final methodology.

Here is the next set of four papers for your **Annotated Bibliography**. I have synthesized the key technical details from these sources to ensure they provide a strong scholarly foundation for your Week 02 requirements.

### 5\. Ramamoorthi, V. (2024). "AI-Driven Resource Management in Cloud Computing: A Review."

* Problem Addressed: The increasing complexity of manual resource management in heterogeneous cloud environments, where human operators cannot keep up with the millisecond-level fluctuations in demand.  
* Methodology: This is a comprehensive Systematic Review that categorizes various AI techniques, including Recurrent Neural Networks (RNNs) for demand forecasting and Reinforcement Learning (RL) for autonomous decision-making.  
* Evaluation Setup: A qualitative synthesis and meta-analysis of existing experimental studies from 2018–2024.  
* Metrics Used: Reliability, cost-effectiveness, energy efficiency, and resource utilization rates.  
* Key Limitations/Trade-offs: Identifies the "Scalability Bottleneck": as the number of VMs grows, the complexity of AI-driven managers increases exponentially, often leading to slower decision times.  
* Relevance to Project: This paper is essential for the Taxonomy Construction task. It provides the high-level definitions for "Predictive vs. Reactive" methods that I am using to categorize my research.

### 6\. Nuthalapati, A. (2025). "Scaling AI Applications on the Cloud toward Optimized Cloud-Native Architectures."

* Problem Addressed: Traditional VM-based scaling often introduces too much latency for "Cloud-Native" AI applications that require near-instantaneous scaling.  
* Methodology: Focuses on Model Efficiency and Workload Distribution using containerized microservices and automated load balancers.  
* Evaluation Setup: Case studies using Kubernetes (K8S) clusters to measure the efficiency of scaling containerized AI inference engines.  
* Metrics Used: Model inference speed, cost per request, and resource overhead.  
* Key Limitations/Trade-offs: Highlights a "Density Trade-off": packing more containers into a single VM improves cost but significantly increases the risk of "noisy neighbour" interference and SLA violations.  
* Relevance to Project: Useful for my "Non-Goals" and "Scope" definitions. It helps me explain why I am focusing on VM-level traces (Azure) rather than container/serverless orchestration.

### 7\. IGI Global (2024). "AI Workload Automation and Orchestration in Cloud Environments."

* Problem Addressed: The "Automation Gap"—even when demand is accurately predicted, the actual orchestration (the process of turning on/off resources) is often too slow or poorly coordinated.  
* Methodology: Proposes an AI-driven Orchestration Layer that uses policy-based automation to bridge the gap between workload prediction and resource provisioning.  
* Evaluation Setup: Theoretical framework and simulation of orchestration workflows in large-scale data center environments.  
* Metrics Used: Operational efficiency, deployment response time, and automation level (%).  
* Key Limitations/Trade-offs: The main limitation is the "Orchestration Lag": even with perfect AI, the physical time it takes for a cloud provider to spin up a VM creates a "blind spot" in the scaling policy.  
* Relevance to Project: Informs my "System Assumptions." It justifies why I must assume a fixed provisioning delay (cooldown) in my simulation to maintain realism.

### 8\. Anbalagan, K. (2024). "AI in Cloud Computing: Enhancing Services and Performance."

* Problem Addressed: General performance bottlenecks and the lack of proactive "Self-Healing" capabilities in cloud service delivery.  
* Methodology: Investigates the use of AI Agents for proactive performance tuning and anomaly-aware response.  
* Evaluation Setup: Empirical study of AI's impact on cloud service availability using real-world enterprise use cases.  
* Metrics Used: Downtime reduction (%), availability (uptime), and user satisfaction scores.  
* Key Limitations/Trade-offs: Identifies "False Positives" in AI detection as a major risk—scaling up unnecessarily due to "noisy" monitoring signals can lead to massive cost spikes.  
* Relevance to Project: Directly supports the "SLA Violation" metric. It provides the argument for why a high SLA is critical for user experience, even if it comes at a slightly higher resource cost.

### 9\. Al-Dhuraibi, Y., et al. (2018). "Elasticity in Cloud Computing: State of the Art and Research Challenges."

* Problem Addressed: The lack of a precise, unified definition and taxonomy for cloud elasticity, particularly the absence of comprehensive research addressing the then-emergent trend of container-based virtualization.  
* Methodology: The authors provide an extensive systematic review and analysis of classical and modern elasticity solutions, proposing a new taxonomy categorized by configuration, scope, purpose, mode, and architecture.  
* Evaluation Setup: A meta-analysis of tools (e.g., Kubernetes, CloudFoundry) and platforms used in existing literature to evaluate both Virtual Machine (VM) and container elasticity.  
* Metrics Used: Key metrics identified include Reaction Time (time to trigger and provision), Precision (avoiding over/under-provisioning), and the trade-off between Quality of Service (QoS) and provider profit.  
* Key Limitations/Trade-offs: The study highlights the "Orchestration Lag" and the "Cold Start" problem (time to boot resources), noting that even proactive AI models struggle with the physical delay of resource provisioning.  
* Relevance to Project: This is a foundational survey that provides the "Taxonomy of Approaches" required for your Week 2 report. It helps justify the distinction between Reactive (threshold-based) and Proactive (AI-driven) modes in your research scoping.

### 10\. Addu, S. (2026). "AI-Driven Autoscaling and Load Balancing for Enterprise Cloud Infrastructure."

* Problem Addressed: Traditional rule-based (reactive) scaling mechanisms are insufficient for managing the dynamic, complex workloads of modern enterprise cloud environments, leading to high latency and operational costs.  
* Methodology: The paper proposes an AI-integrated framework that leverages Machine Learning and intelligent analytics to predict workload patterns and automate resource scaling and load balancing proactively.  
* Evaluation Setup: Simulated or real-world enterprise cloud architecture focused on integrating AI into infrastructure management for real-time response.  
* Metrics Used: SLA Compliance, Operational Costs, Latency, and Resource Utilization Efficiency.  
* Key Limitations/Trade-offs: A major challenge identified is the Model Sensitivity: the system's effectiveness is heavily dependent on the quality of training data and the ability of the model to generalize across diverse enterprise application behaviours.  
* Relevance to Project: This paper is extremely current (Jan 2026\) and directly mirrors your research question. It provides recent proof that AI-driven proactive decision-making is the "strategic enabler" for reducing costs and improving SLA compliance in modern clouds.

*\* Note: AI was used to summarize and log papers after reading for documentation purposes \**

