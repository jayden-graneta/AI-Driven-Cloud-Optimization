# AI-Driven Cloud Optimization (CP395)
### **Directed Study | Wilfrid Laurier University**

**Student:** Jayden Rey Graneta  
**Supervisor:** Dr. Mustafa Daraghmeh  
**Term:** Winter 2026  

---

## 🚀 Project Overview
This research project focuses on the development and evaluation of **AI-driven autoscaling policies** for cloud virtual machines. By moving beyond traditional reactive thresholds, this study explores proactive machine learning models capable of anticipating workload "bursts" to optimize the critical trade-off between operational cost and service reliability.

### 🎯 Research Problem
**Primary Question:** *"Can an AI-driven autoscaling policy reduce SLA violations and resource over-provisioning compared to a threshold-based baseline when evaluated using Microsoft Azure public workload traces?"*

---

## 🛠 Tech Stack
* **Language:** Python 3.11+
* **Deep Learning:** PyTorch (LSTM Architectures)
* **Data Science:** Pandas, NumPy, Matplotlib (Visualization)
* **Research Tools:** LaTeX (IEEE Tran), Overleaf, Git
* **Simulation:** Custom Discrete-Event Simulation Engine

---

## 📊 Dataset & Metrics
### **Dataset: Microsoft Azure Public VM Traces (v2)**
The project utilizes real-world production traces from Microsoft Azure. This dataset is ideal for systems research as it reflects realistic, "bursty" cloud workload behavior from large-scale environments.
* **Current Status:** Traces have been aggregated into **51 discrete subscription clusters** to simulate multi-tenant behavior and reduce telemetry "jitter."

### **Key Performance Indicators (KPIs)**
* **SLA Violation Rate:** Percentage of time steps where CPU demand exceeds allocated capacity.
* **Resource Utilization:** Mean/peak CPU usage to identify over-provisioning (waste).
* **Scaling Stability:** Frequency of scale-up/down events to measure system "flapping."
* **System Reward ($R$):** A formal reward function calculating:
    $$R = -(Waste) - (10 \times \text{SLA Penalty}) - (\zeta \times \text{Stability Penalty})$$

---

## 📂 Repository Structure
```text
├── data/                 # Trace processing and cleaning scripts
│   └── task7_subscription_aggregated.csv # Aggregated cluster data
├── docs/                 # Course documentation and reports
│   ├── reports/          # Weekly Research Reports (Week 01 - 12)
│   └── manuscript/       # IEEE Research Paper (LaTeX Source)
├── src/                  # Simulation engine and AI model code
│   ├── simulation_engine.py # Discrete-event simulator 
│   └── proactive_lstm.py    # PyTorch LSTM implementation
├── BIBLIOGRAPHY.md       # Annotated bibliography (12+ papers)
└── README.md             # Project landing page
```

---

## 📈 Final Project Benchmarks (Week 12)
The project successfully transitioned from reactive baseline testing to a **Proactive Selection Framework** to mitigate the inherent **300-second (L=300s)** provisioning delay.

### **Model Performance Comparison**
| Model | Metric | Value | Note |
| :--- | :--- | :--- | :--- |
| **ARIMA (5,1,0)** | MSE | 1.8138 | Strong statistical fit for single traces. |
| **Optimized LSTM** | MSE | 69.54 | Achieved via 10% Dropout & Early Stopping. |
| **Baseline (MA)** | MSE | 36.37 | High error during sudden burst cycles. |
| **Final Simulation** | **Avg. Reward** | **-7.8848** | Limited by physical 300s provisioning lag. |

---

## 🚀 How to Rerun Core Experiments
This repository is designed for full reproducibility. Follow the steps below to set up the environment, train the proactive model, and execute the scaling simulation.

### 1. Environment Setup
Ensure you have Python 3.11+ installed. Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/jayden-graneta/CP395-Cloud-Optimization.git](https://github.com/jayden-graneta/CP395-Cloud-Optimization.git)
cd CP395-Cloud-Optimization

# Create and activate virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate  

pip install -r requirements.txt

``
