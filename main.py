import os
from prepare_merge_data import prepare_and_merge
from train_and_validate import train_predict_validate

def main():
    os.makedirs("outputs", exist_ok=True)

    merged_csv = "outputs/merged_features.csv"
    predictions_csv = "outputs/predictions.csv"
    performance_txt = "outputs/performance.txt"

    prepare_and_merge(
        "datasets/Data 2.csv",
        "datasets/StockPrice.csv",
        merged_csv
    )

    train_predict_validate(
        merged_csv,
        predictions_csv,
        performance_txt
    )

    print("\n PIPELINE COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    main()
