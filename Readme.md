
# Stock Price Prediction using Machine Learning

### Python Developer Intern – 2026 | Machine Learning Assignment

## 📌 Problem Statement

This project focuses on predicting the next day’s stock price using only the provided datasets. The goal is to build a Python-based machine learning model that explicitly captures how day-over-day changes in the independent signal influence stock price movements.

## 📊 Datasets Provided

* **Data 2.csv**: Independent variable (The Signal).
* **StockPrice.csv**: Dependent variable (Stock Price).

## ⚙️ Core Assumptions

1. **Primary Influence**: The next day’s stock price is primarily driven by the change in the independent dataset from the previous day.
2. **Scope Limitation**: To ensure compliance with the assignment, the model excludes macroeconomic indicators, news sentiment, and external market variables.

---

## 📂 Project Structure

```text
INTERNSHIPASSIGNMENT/
│
├── datasets/                # Original raw data files
├── outputs/                 # Generated results
│   ├── merged_features.csv  # Final dataset used for training
│   ├── performance.txt      # Model evaluation metrics
│   └── predictions.csv      # Actual vs Predicted values
│
├── .gitignore               # Prevents pycache and environment files from being pushed
├── DatasetAnalysis.ipynb    # Exploratory Data Analysis (EDA)
├── main.py                  # Entry point to run the entire pipeline
├── prepare_merge_data.py    # Data cleaning and feature engineering logic
├── train_and_validate.py    # Model training and evaluation script
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd INTERNSHIPASSIGNMENT

```

### 2. Setup Environment

**Windows:**

```bash
python -m venv myenv
myenv\Scripts\activate

```

**macOS/Linux:**

```bash
python3 -m venv myenv
source myenv/bin/activate

```

### 3. Install & Execute

```bash
pip install -r requirements.txt
python main.py

```

---

## 🛠️ Workflow & Methodology

1. **Data Preparation**: Merged datasets on `Date` and sorted chronologically to prevent data leakage.
2. **Feature Engineering**:
* `Data_Change`: Captures day-over-day volatility.
* `Price_RollMean_3`: Smooths noise using a 3-day rolling window.
* `Target_Price`: Shifted price column to represent the "Next Day."


3. **Model**: **Linear Regression** was selected for its high interpretability and efficiency in time-series continuity.

### Model Performance

| Metric | Value | Interpretation |
| --- | --- | --- |
| **MAE** | 38.23 | Average prediction error |
| **RMSE** | 49.88 | Penalizes larger errors |
| **** | 0.9935 | Explains 99.35% of price variance |
| **Accuracy** | 99.21% | MAPA based accuracy |

---

## 📈 Conclusion

The model delivers a stable and highly accurate prediction () by focusing on the relationship between price continuity and the provided independent signal. It fulfills all assignment requirements regarding data usage and feature modeling.

---
