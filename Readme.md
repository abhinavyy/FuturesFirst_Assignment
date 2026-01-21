# Stock Price Prediction using Machine Learning
## Python Developer Intern  – 2026
## Machine Learning Assignment – Stock Price Prediction

## Problem Statement

This project focuses on predicting the next day’s stock price using only the provided datasets, as per the assignment requirements.

## Datasets Provided

### Data Dataset – Independent variable(s)

### StockPrice Dataset – Dependent variable representing stock prices

## Objective

To build a Python-based machine learning model that predicts the next day’s stock price, explicitly modeling how day-over-day changes in the Data dataset influence stock price movements.

---

## Core Assumptions 

### 1.Primary Influence
The next day’s stock price is primarily influenced by the change in the Data dataset from the previous day.

### 2.Scope Limitation

- No macroeconomic indicators
- No external market variables
- No news, sentiment, or technical indicators
- Only the relationship between the provided datasets is modeled.

## Datasets Used

- **Data 2.csv**
  - Columns: Date, Data
  - Represents the independent signal

- **StockPrice.csv**
  - Columns: Date, Price
  - Represents the dependent variable (stock price)

---
## Project Structure

INTERNSHIPASSIGNMENT/
│
├── datasets/                # Original raw data files
├── outputs/                 # Generated results
│   ├── merged_features.csv  # Final dataset used for training
│   ├── performance.txt      # Model evaluation metrics
│   └── predictions.csv      # Actual vs Predicted values
│
├── .gitignore               # Prevents pycache, env, and large files from being pushed
├── DatasetAnalysis.ipynb    # Exploratory Data Analysis (EDA)
├── main.py                  # Entry point to run the entire pipeline
├── prepare_merge_data.py    # Data cleaning and feature engineering logic
├── train_and_validate.py    # Model training and evaluation script
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

## How to Run the Project

1. Clone the Repository

Bash
git clone <your-repository-link>
cd INTERNSHIPASSIGNMENT

2. Create a Virtual Environment

Bash
# Windows
python -m venv myenv

# macOS/Linux
python3 -m venv myenv

3. Activate the Environment

Bash
# Windows
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate

4. Install Dependencies

Bash
pip install -r requirements.txt

5. Run the Pipeline
The main.py script executes the data preparation, training, and evaluation in sequence.

Bash
python main.py

All results will be saved automatically in the outputs/ directory.

---

## Approach

Instead of directly predicting price changes, this project models the next-day stock price level using today’s observable information, including:

- **Current stock price**

- **Data value and its day-over-day change**

- **Short-term rolling trends**

### This approach balances:

- Assignment compliance

- Statistical stability

- Interpretability

---

## Workflow Overview

1.Load and merge datasets

2.Perform exploratory data analysis (EDA)

3.Engineer features that capture:

    - Level effects
    - Day-over-day changes
    - Short-term trends

4.Define next-day stock price as the prediction target

5.Train a Linear Regression model

6.Evaluate performance using multiple metrics

7.Generate prediction and performance reports

---

## Data Preparation

- Merged datasets on Date
- Sorted chronologically
- Engineered features without future leakage
- Created next-day price as the target variable

### Merged Dataset Structure
The final merged dataset contains:

| Column           | Description                                |
| ---------------- | ------------------------------------------ |
| Date             | Trading date                               |
| Data             | Independent dataset value                  |
| Price            | Current stock price                        |
| Data_Change      | Day-over-day change in Data                |
| Price_Change     | Day-over-day change in Price               |
| Data_RollMean_3  | 3-day rolling mean of Data                 |
| Price_RollMean_3 | 3-day rolling mean of Price                |
| Target_Price     | Next day’s stock price (prediction target) |

---

## Feature Engineering

The following features were used to model the relationship effectively:

### 1. Data

    - Captures the absolute level of the independent variable
    - Helps model long-term influence on price

### 2. Data_Change

    - Explicitly models the assignment’s core assumption
    - Represents how day-over-day changes in Data affect price

### 3. Price

    - Stock prices exhibit strong continuity
    - Yesterday’s price is a strong baseline for tomorrow

### 4. Price_Change

    - Captures short-term momentum effects

### 5. Rolling Means (3-day)

    - Smooth short-term noise
    - Represent short-term trends instead of single-day spikes

### These features ensure:
Assignment compliance
Stability
Interpretability

---

## Model Selection

**Linear Regression** was chosen due to:

1.**Interpretability**: Directly shows the impact of Data_Change on price.
2.**Stability**: High $R^2$ of **0.9935** indicates excellent fit for time-series continuity.Efficiency: Avoids overfitting on small-to-medium datasets.

---

## Training Strategy

- Time-based split:
  - 80% training
  - 20% testing
- Preserves chronological order
- Prevents data leakage
- Reflects real-world forecasting conditions

---

## Model Evaluation

### Core Regression Metrics

| Metric | Value  | Interpretation                    |
| ------ | ------ | --------------------------------- |
| MAE    | 38.23  | Average prediction error          |
| RMSE   | 49.88  | Penalizes larger errors           |
| R²     | 0.9935 | Explains 99.35% of price variance |

### Accuracy Interpretation Metrics

| Metric               | Meaning                        |
| -------------------- | ------------------------------ |
| MAPA (Accuracy %)    | 99.21% average accuracy        |
| NRMSE                | 1.01% relative error           |
| Directional Accuracy | 48.82%                         |

---

## Interpretation

- The model explains **over 99% of price variance**
- Average error is low relative to stock price levels
- Predictions are stable and consistent

---

## Outputs Generated

1.`predictions.csv`
  - Date
  - Actual_Price
  - Predicted_Price
  - Error 
  - Absolute_Error
  - Percentage_Error

2.`model_performance.txt`
  - Dataset split details
  - All evaluation metrics
  - Stability analysis

---

## Limitations

- Linear assumptions may miss non-linear effects
- Performance depends on historical stability

---

## Conclusion

This project delivers a **clean, interpretable, and assignment-aligned** solution for next-day stock price prediction.
The approach balances statistical rigor, model simplicity, and explicit compliance with the problem’s core assumptions.
