Here is the complete, formatted code for your README.md file. You can copy everything from the box below and paste it directly into your GitHub repository.

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
├── SEARCH_LOG.md       # Documented database search strategy
└── README.md           # Project landing page
