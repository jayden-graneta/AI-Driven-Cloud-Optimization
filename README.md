Here is the updated README.md in a raw Markdown format, incorporating your Week 8 breakthroughs including the subscription-level aggregation, the proactive simulation architecture, and current performance benchmarks.

Markdown
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
* **Deep Learning:** PyTorch (LSTM Architectures)
* **Data Manipulation:** Pandas, NumPy
* **Documentation:** LaTeX (IEEE Tran), Overleaf
* **Environment:** Virtual Environments (`venv`), Git/GitHub

---

## 📊 Dataset & Metrics
### **Dataset: Microsoft Azure Public VM Traces (v2)**
The project utilizes real-world production traces from Microsoft Azure. This dataset is ideal for systems research as:
* It reflects **realistic cloud workload behavior** from large-scale environments.
* It supports **autoscaling decisions** based on multi-dimensional resource demand.
* **Current Status:** Traces have been aggregated into **51 synthetic subscription clusters** to simulate multi-tenant workload behavior and reduce telemetry "jitter".

### **Key Metrics**
* **SLA Violations:** Occurrences where CPU demand exceeds allocated capacity.
* **Resource Utilization:** Mean/peak CPU usage to identify over-provisioning.
* **Scaling Stability:** The frequency of scale-up/down events to measure system "flapping".
* **System Reward ($R$):** A formal reward function incorporating waste, a -10 penalty for SLA violations, and a stability penalty ($\zeta$).

---

## 📂 Repository Structure
```text
├── data/                 # Trace processing and cleaning scripts
│   └── task7_subscription_aggregated.csv # Aggregated cluster data
├── docs/                 # Course documentation and reports
│   ├── reports/          # Weekly Research Reports
│   └── manuscript/       # IEEE Research Paper (LaTeX/Overleaf)
├── src/                  # Simulation engine and AI model code
│   ├── simulation_engine.py # Discrete-event simulator with SelectionModule
│   └── proactive_lstm.py    # PyTorch LSTM implementation
├── BIBLIOGRAPHY.md       # Annotated bibliography (12+ papers)
└── README.md             # Project landing page
```

Here is the updated Week 8 status and the remaining sections of your project documentation, formatted in clean Markdown.

Markdown
---

## 📈 Current Project Status (Week 08)
The project has successfully transitioned from reactive baseline testing to a **Proactive Selection** framework.

### **Proactive Selection Logic**
To mitigate the inherent provisioning delay ($L=300s$), the system utilizes a **Selection Module** that evaluates predicted demand ($\hat{D}_{t+L}$) to trigger scaling actions pre-emptively.



### **Model Performance Benchmarks**
| Model | Metric | Value |
| :--- | :--- | :--- |
| **ARIMA** | MSE | 1.8138 |
| **LSTM (Baseline)** | MSE | 515.9697 (Overfitting identified) |
| **Simulation** | Avg. Reward | -7.8848 (Subscription Average) |

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

## 🎯 Research Gap Identification
Based on the synthesis of the 12 retained papers, I have identified four specific research gaps that my study will address:

1. **The Stability-Accuracy Gap:** Most proactive models optimize for prediction accuracy (minimizing RMSE). However, high accuracy often leads to "jitter" (rapid scaling events). This project introduces **Scaling Stability** as a primary success metric.
2. **Dataset Realism Gap:** Much of the existing Reinforcement Learning literature relies on the 2011 Google Borg traces. This project addresses the gap by evaluating policies against the modern **2019/2021 Microsoft Azure VM traces**.
3. **The Provisioning Latency Realism Gap:** Many simulations assume instant resource availability. My evaluation incorporates **fixed provisioning delays ($L=300s$) and cooldowns** to test the robustness of AI under real-world constraints.
4. **Baseline Fairness Gap:** AI models are often compared to weak, unoptimized baseli

---

### **Summary of Updates**
* **Metrics:** Added the formal **System Reward ($R$)** definition to match your new simulation logic.
* **Status:** Added a "Week 08" status section to highlight the **Proactive Selection Logic** and the $L=300s$ delay.
* **Benchmarks:** Integrated the actual results from your latest `simulation_engine.py` run and the ARIMA/LSTM comparison.
