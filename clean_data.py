import pandas as pd


df = pd.read_csv("retail_store_sales.csv")
print("Original data shape:", df.shape)


df = df.dropna(subset=["Item", "Price Per Unit", "Quantity", "Total Spent"])
df["Discount Applied"] = df["Discount Applied"].fillna(False)


df = df.drop_duplicates()


df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors='coerce')
df["transaction_date"] = df["transaction_date"].dt.strftime('%d-%m-%Y')
df["quantity"] = df["quantity"].astype(int)
df["price_per_unit"] = df["price_per_unit"].astype(float)
df["total_spent"] = df["total_spent"].astype(float)


df.to_csv("cleaned_retail_data.csv", index=False)

print("\nCleaned data shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
