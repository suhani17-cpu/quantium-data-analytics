import pandas as pd

df = pd.read_csv("data/daily_sales_data_0.csv")

print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
print(df["quantity"].sum())
print(df["quantity"].mean())
print(df["quantity"].max())
print(df[df["quantity"] > 550])
print(df.sort_values(by="quantity", ascending=False))
import matplotlib.pyplot as plt

df["quantity"].plot()

plt.show()
df["quantity"].hist()

plt.show()
import matplotlib.pyplot as plt

plt.hist(df["quantity"])
plt.show()
df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)

print(df["price"].mean())
print(df.groupby("product")["quantity"].sum())
df.groupby("product")["quantity"].sum().plot(kind="bar")

plt.show()
sales = df.groupby("product")["quantity"].sum()

print(sales.idxmax())
print(sales.max())
df["revenue"] = df["price"] * df["quantity"]

print(df[["product", "revenue"]].head())

print(df.groupby("product")["revenue"].sum())
df.groupby("product")["revenue"].sum().plot(kind="pie", autopct="%1.1f%%")

plt.ylabel("")
plt.show()