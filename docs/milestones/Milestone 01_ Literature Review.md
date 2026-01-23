**Milestone 01: Literature Review**  
**CP395: AI-Driven Cloud Optimization**  
**Jayden Rey Graneta**  
**01/18/26**  
**Dr. Mustafa Daraghmeh**

**Introduction**  
Current-day workload patterns are now more unpredictable than ever as we transition towards cloud native architectures. Reactive scaling is where the system only uses resources that have been allocated towards it after reaching a certain threshold or baseline, such as 80% CPU usage and is one of the mainstays of traditional resource management. However, using this method leads to lag in modern systems when traffic arrives in large burst patterns. Performance has already declined by the time a new VM has been prepared, resulting in SLA violations. Many cloud providers use over-provisioning in order to avoid this issue, which results in a waste of resources.

This study looks at how AI-driven autoscaling can replace the reactive baseline guessing. We can determine how predictive models can create a balance between cost savings and dependability using real-world Microsoft Azure Traces. This review covers different academic scholarly papers used to gain insights, and research gaps to help improve the problem statement: "Can an AI-driven autoscaling policy reduce SLA violations and resource over-provisioning compared to a threshold-based baseline when evaluated using Microsoft Azure public workload traces?"

## **Background**

"Elasticity" in cloud computing refers to the system's capacity to adapt to its workload \[9\]. We specifically concentrate on VM-level elasticity in this study.

A virtual machine (VM) takes minutes to boot up because it must initialize an entire operating system, in contrast to containers, which can scale in seconds \[7\]. The main issue is this physical delay, also known as orchestration lag. The scaling action will always be too late if a model does not "see" a spike several minutes in advance.

## **Taxonomy of Research Approaches**

Based on decision-making processes, we can classify current research into three major groups.

Heuristics for Reaction (The Baseline)

These are the typical "if-then" guidelines that are employed in the current industry. They are fundamentally backward-looking, despite being straightforward and inexpensive to operate \[1\]. They are ineffective at anticipating abrupt traffic spikes because they respond to what has just occurred.

Forecasting and Proactive Supervised Learning

These models attempt to forecast the future by using historical data.

* Models of Statistics: Excellent for consistent trends but ineffective in erratic spikes \[2\].  
* When it comes to identifying patterns in time series data, deep learning (LSTM/RNN) performs far better \[1\]. Although they offer a proactive advantage, their training and upkeep can be costly.

### Autonomous Reinforcement Learning (RL)

By approaching scaling as a game, Autonomous Reinforcement Learning (RL) adopts a different strategy. A "reward" is given to an "agent" according to how well it strikes a balance between cost and performance \[4\]. Despite their strength, these models have a Cold Start issue, which causes them to make bad choices early on while they are still getting to know their surroundings.

***Table 1: Comparison of Scaling Logic***

| Category | Logic | Input Data | Main Trade-off |
| :---- | :---- | :---- | :---- |
| Reactive | Thresholds | Real-time CPU | Simple but slow to react |
| Predictive | LSTM / AI | Historical Traces | Accurate but high overhead |
| Autonomous | RL Policy | System State | Optimal but slow to learn |

## 

## **Discussion of Key Trade-offs**

A major theme in recent research is the conflict between granularity and stability. Yenugula \[3\] points out that if you monitor a system too closely, such as every second, the AI might become "jittery," scaling up and down constantly in response to noise. This "flapping" wastes resources. This justifies our decision to use 5-minute data intervals, which provide enough detail without causing system instability.

**Identified Research Gaps**

Three particular areas still require improvement, according to my analysis of the recent literature:

1. The Stability-Accuracy Gap: The majority of researchers are only concerned with the accuracy of their predictions. They frequently overlook the possibility that the model makes the infrastructure "jitter." We require a Scaling Stability metric.  
2. Unrealistic Expectations of Speed: Many studies make the assumption that resources are instantaneous. In actuality, everything changes in the few minutes it takes for a virtual machine to boot up. Simulations that impose a set provisioning delay are required.  
3. The Training Gap: Research on the safe transition from a simple rule-based system to a smart AI system without causing the service to crash during the learning phase is lacking.

## **Project Positioning**

The Stability and Delay gaps are directly addressed by this project. I'll test whether an LSTM-based model can anticipate long enough to overcome the provisioning lag using a custom simulation environment and contemporary Azure traces. In contrast to earlier research, I will penalize the model for excessive scaling in order to guarantee that the final solution is sufficiently stable for practical application \[10\].

