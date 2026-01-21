import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_predict_validate(input_csv, pred_csv, report_txt):
    df = pd.read_csv(input_csv)
    FEATURES = [
        "Data",
        "Price",
        "Data_Change",
        "Price_Change",
        "Data_RollMean_3",
        "Price_RollMean_3"
    ]
    X = df[FEATURES]
    y = df["Target_Price"]

    split = int(len(df) * 0.8)

    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = np.round(model.predict(X), 2)


    out = pd.DataFrame({
        "Date": df["Date"],
        "Actual_Price": y,
        "Predicted_Price": predictions
    })

    out["Error"] = out["Actual_Price"] - out["Predicted_Price"]
    out["Absolute_Error"] = out["Error"].abs()
    out["Percentage_Error"] = (out["Absolute_Error"] / out["Actual_Price"]) * 100

    out.to_csv(pred_csv, index=False)


    test_df = out.iloc[split:].copy()

    mae = mean_absolute_error(y_test, predictions[split:])
    rmse = np.sqrt(mean_squared_error(y_test, predictions[split:]))
    r2 = r2_score(y_test, predictions[split:])

    mapa = 100 - test_df["Percentage_Error"].mean()

    nrmse = (rmse / test_df["Actual_Price"].mean()) * 100
    actual_direction = np.sign(test_df["Actual_Price"].diff())
    predicted_direction = np.sign(test_df["Predicted_Price"].diff())
    directional_accuracy = (actual_direction == predicted_direction).mean() * 100

    error_std = test_df["Error"].std()
    report = f"""
MODEL PERFORMANCE REPORT
==================================================

DATA SPLIT
--------------------------------------------------
Training Samples : {split}
Testing Samples  : {len(df) - split}

CORE REGRESSION METRICS
--------------------------------------------------
MAE   (Average Error)        : {mae:.2f}
RMSE  (Error Magnitude)     : {rmse:.2f}
R²    (Explained Variance)  : {r2:.4f}

ACCURACY INTERPRETATION
--------------------------------------------------
MAPA (Accuracy %)           : {mapa:.2f}%
NRMSE (Relative Error %)    : {nrmse:.2f}%
Directional Accuracy        : {directional_accuracy:.2f}%

MODEL STABILITY
--------------------------------------------------
Error Std Deviation         : {error_std:.2f}

"""

    with open(report_txt, "w", encoding="utf-8") as f:
        f.write(report)

    print("Predictions CSV generated")
    print("Accuracy report generated")
