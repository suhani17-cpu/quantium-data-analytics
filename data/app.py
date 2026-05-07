import pandas as pd

# Load CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all files
df = pd.concat([df1, df2, df3])

# Keep only pink morsel
df = df[df["product"] == "pink morsel"]

# Remove $ sign and convert price to float
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Create sales column
df["sales"] = df["price"] * df["quantity"]

# Keep only required columns
output = df[["sales", "date", "region"]]

# Save final output file
output.to_csv("data/formatted_output.csv", index=False)

print(output.head())
print("formatted_output.csv created successfully")