import pandas as pd

df = pd.read_csv("../data/airline_operations.csv")

print("=== AeroPulse Data Quality Check ===")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate Flight_ID:", df["Flight_ID"].duplicated().sum())
print("\nDate range:", df["Flight_Date"].min(), "to", df["Flight_Date"].max())
print("\nFlight status:")
print(df["Flight_Status"].value_counts())
print("\nAirlines:")
print(df["Airline"].value_counts())
