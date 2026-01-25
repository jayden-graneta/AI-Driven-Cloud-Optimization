# AI-Driven Cloud Optimization (CP395)
### Directed Study | Wilfrid Laurier University
**Student:** Jayden Rey Graneta  
**Supervisor:** Dr. Mustafa Daraghmeh  
**Semester:** Winter 2026

---

## 🚀 Project Overview
This research project focuses on the development and evaluation of AI-driven autoscaling policies for cloud virtual machines. By moving beyond traditional reactive thresholds, this study explores proactive machine learning models capable of anticipating workload bursts to optimize the trade-off between operational cost and service reliability.

### 🎯 Research Problem
**Problem Statement:** *"Can an AI-driven autoscaling policy reduce SLA violations and resource over-provisioning compared to a threshold-based baseline when evaluated using Microsoft Azure public workload traces?"*

### 🛠 Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Environment:** Virtual Environments (`venv`), Git/GitHub

---

## 📊 Dataset & Metrics
### **Dataset: Microsoft Azure Public VM Traces (v2)**
The project utilizes real-world production traces from Microsoft Azure. This dataset is ideal for systems research as:
* It reflects **realistic cloud workload behavior** from large-scale environments.
* It supports **autoscaling decisions** based on multi-dimensional resource demand.
* It allows for high-fidelity evaluation of **SLA violations** and efficiency.
* It is a **widely cited benchmark**, ensuring the study is rigorous and reproducible.

### **Key Metrics**
* **SLA Violations:** Occurrences where CPU demand exceeds allocated capacity.
* **Resource Utilization:** Mean/peak CPU usage (identifying over-provisioning).
* **Scaling Stability:** The frequency of scale-up/down events (measuring system "jitter" or flapping).
* **Estimated Cost:** Derived from VM instance uptime and resource allocation.

---

## 📂 Repository Structure
```text
├── data/               # Trace processing and cleaning scripts
├── docs/               # Course documentation and reports
│   ├── reports/        # Weekly Research Reports
│   └── milestones/     # Literature Review and Final Papers
├── src/                # Simulation engine and AI model code
├── BIBLIOGRAPHY.md     # Annotated bibliography (12+ papers)
├── venv/               # Local virtual environment (ignored)
├── SEARCH_LOG.md       # Documented database search strategy
└── README.md           # Project landing page

```
---

### 2. Taxonomy Overview
Existing literature in the field of cloud resource management is categorized by the **Control Logic** used to make decisions and the **Temporal Mode** in which those decisions are executed. My project specifically targets the transition from Reactive Heuristics to Proactive Learning.



**Table 1: Summary of Representative Approaches in Literature**
| Approach Category | Control Logic | Required Inputs | Primary Metrics | Key Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Reactive** | Heuristic Thresholds | Real-time CPU % | SLA Violation Rate | **Provisioning Lag:** Cannot preemptively handle bursts. |
| **Proactive (AI)** | Supervised (LSTM) | Historical Traces | Accuracy (RMSE) | **Stability Gap:** Models may trigger excessive scaling. |
| **Autonomous** | Policy Agents (RL) | System State | Cumulative Reward | **Convergence:** Requires long training/exploration times. |
| **Cloud-Native** | Micro-scaling | Container Metrics | Response Time | **Noisy Neighbor:** Performance interference on shared CPUs. |

---

## 🔍 Systematic Literature Search Log
To ensure scholarly grounding and rigor, a systematic search strategy was executed across major academic databases. This log tracks the queries and results used to build the project's foundational bibliography.

**Table 2: Systematic Literature Search Log**

| Database | Query String | Date Searched | Results | Papers Used |
| :--- | :--- | :--- | :--- | :--- |
| **Google Scholar** | `“AI-driven autoscaling Microsoft Azure VM traces workload.”` | 01/17/26 | 2,100 | 8 |
| **IEEE Xplore** | `"AI" AND "cloud autoscaling" AND "VM"` | 01/17/26 | 412 | 1 |
| **Professor / MyLS**| `n/a (Course Materials / Uploads)` | 01/18/26 | 1 | 1 |

---

### 4. Research Gap Identification
Based on the synthesis of the 12 retained papers, I have identified four specific research gaps that my study will address:

1.  **The Stability-Accuracy Gap:** Most proactive models optimize for prediction accuracy (minimizing RMSE). However, high accuracy often leads to "jitter" (rapid scaling events). This project introduces **Scaling Stability** as a primary success metric.
2.  **Dataset Realism Gap:** Much of the existing Reinforcement Learning literature relies on the 2011 Google Borg traces. This project addresses the gap by evaluating policies against the modern **2019/2021 Microsoft Azure VM traces**.
3.  **The Provisioning Latency Realism Gap:** Many simulations assume instant resource availability. My evaluation will incorporate **fixed provisioning delays and cooldowns** to test the robustness of AI under real-world constraints.
4.  **Baseline Fairness Gap:** AI models are often compared to weak, unoptimized baselines. I will implement a **tuned reactive baseline** to establish a more rigorous and defensible performance gain.

---

