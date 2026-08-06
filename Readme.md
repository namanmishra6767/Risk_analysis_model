# 🏥 Healthcare Risk Stratification & Clinical Outcome Analysis

A machine learning application that predicts patient risk levels (High Risk vs. Low Risk) and risk probabilities based on clinical parameters, diagnostic data, laboratory results, and hospital outcomes. The project includes data processing, model training, and an interactive web dashboard built with Streamlit.

---

## 🌟 Features

* **Interactive Risk Prediction:** Calculate patient risk in real-time by entering clinical parameters such as age, length of stay, and treatment cost.
* **Risk Probability Score:** Outputs both a categorical prediction (`High Risk` / `Low Risk`) and a calibrated probability score.
* **Comprehensive Patient Data Integration:** Preprocessing pipelines that merge patient demographics, diagnoses, laboratory test results, and clinical outcomes.
* **Jupyter Notebook Analysis:** Complete machine learning workflow including data exploration, feature engineering, model training, and performance evaluation.

---

## 📁 Repository Structure

```text
├── Riskmodel1.ipynb          # Notebook for data cleaning, EDA, and model training
├── Riskanalysismodel.py      # Streamlit web application script
├── patients.csv              # Patient demographic and admission data
├── labs.csv                  # Patient laboratory test results
├── diagnosis.csv             # Patient medical diagnosis history
├── outcomes.csv              # Patient discharge status and clinical outcomes
├── .gitignore                # Specifies intentionally untracked files
└── README.md                 # Project documentation

```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### 1. Clone the Repository

```bash
git clone [https://github.com/namanmishra6767/Risk_analysis_model.git](https://github.com/namanmishra6767/Risk_analysis_model.git)
cd Risk_analysis_model

```

### 2. Set Up a Virtual Environment

* **On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate

```


* **On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```



### 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn streamlit matplotlib

```

---

## 💻 Running the Streamlit App

Run the following command in your terminal to launch the web dashboard:

```bash
streamlit run Riskanalysismodel.py

```

Once executed, Streamlit will automatically open the application in your default web browser (typically at `http://localhost:8501`).

---

## 📊 Dataset & Model Architecture

The predictive modeling pipeline combines four primary data sources:

* **Demographics & Admissions:** `patients.csv`
* **Lab Results:** `labs.csv` (used for calculating abnormal lab counts)
* **Medical History:** `diagnosis.csv`
* **Clinical Outcomes:** `outcomes.csv` (used to establish target ground truth for risk levels)

Model performance is evaluated using **Precision**, **Recall**, **F1-Score**, and **ROC-AUC** metrics to ensure reliable performance on imbalanced clinical datasets.

---

## 🛠️ Built With

* **[Python](https://www.python.org/)** - Core programming language
* **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
* **[Scikit-Learn](https://scikit-learn.org/)** - Machine learning modeling and evaluation
* **[Streamlit](https://streamlit.io/)** - Interactive web framework for ML apps

---