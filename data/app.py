import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all files
df = pd.concat([df1, df2, df3])

# Keep only pink morsel
df = df[df["product"] == "pink morsel"]

# Clean price column
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Create sales column
df["sales"] = df["price"] * df["quantity"]

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Group by date
sales_data = df.groupby("date")["sales"].sum().reset_index()

# Create line chart
fig = px.line(
    sales_data,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

# Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)