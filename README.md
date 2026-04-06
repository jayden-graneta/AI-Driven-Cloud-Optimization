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

```

###2. Data Preparation
The simulation requires aggregated subscription traces. If the processed files are not present in the /data directory, run the aggregation script:

```bash
python data/preprocess_traces.py
```

### 3. Training the Proactive LSTM
To retrain the model using the parameters cited in the research paper (10% Dropout, Early Stopping, and Min-Max Normalization):

```bash
python src/proactive_lstm.py --train --epochs 100 --batch_size 32

```
*This script will save the `best_model.pth` in the `/models` directory and log the final Mean Squared Error (MSE) to the console.*

### 4. Executing the Scaling Simulation
To evaluate the trained model against the 300-second provisioning lag and calculate the final System Reward:

```bash
python src/simulation_engine.py --model_path models/best_model.pth --latency 300
```
**Outputs:** The engine will calculate the Average System Reward (-7.8848) and generate a visualization plot (`results_plot.png`) comparing actual demand vs. allocated capacity.

---

## 🔍 Systematic Literature Search Log
To ensure scholarly rigor, a systematic search was executed across major academic databases.

| Database | Query String | Papers Used |
| :--- | :--- | :--- |
| **Google Scholar** | “AI-driven autoscaling Microsoft Azure VM traces workload” | 8 |
| **IEEE Xplore** | "AI" AND "cloud autoscaling" AND "VM" | 2 |
| **Course Materials** | N/A (Manual Uploads / Dr. Daraghmeh) | 2 |

---

## 🎯 Research Gap Identification
This study addresses four specific gaps identified in current literature:

* **The Stability-Accuracy Gap:** Most models minimize RMSE but ignore "jitter." We introduce **Scaling Stability** as a primary metric.
* **Dataset Realism Gap:** Moving beyond the 2011 Google traces to modern **2019/2021 Microsoft Azure VM traces**.
* **Provisioning Latency Realism:** Unlike many simulations, we incorporate a **fixed $L=300s$ delay** and cooldown periods to mirror real-world VM spin-up times.
* **Baseline Fairness:** Comparing AI against optimized statistical baselines rather than arbitrary thresholds.

---
