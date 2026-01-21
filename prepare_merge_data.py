import pandas as pd

def prepare_and_merge(data_path, price_path, output_path):
    data = pd.read_csv(data_path)
    price = pd.read_csv(price_path)

    data.columns = ["Date", "Data"]
    price.columns = ["Date", "Price"]

    data["Date"] = pd.to_datetime(data["Date"])
    price["Date"] = pd.to_datetime(price["Date"])
    df = pd.merge(data, price, on="Date", how="inner")
    df = df.sort_values("Date").reset_index(drop=True)
    df["Data_Change"] = df["Data"].diff()
    df["Price_Change"] = df["Price"].diff()

    df["Data_RollMean_3"] = df["Data"].rolling(3).mean()
    df["Price_RollMean_3"] = df["Price"].rolling(3).mean()

    df["Target_Price"] = df["Price"].shift(-1)

    df = df.dropna().reset_index(drop=True)

    df.to_csv(output_path, index=False)
    print(f"Merged feature file saved to {output_path}")

    return df
