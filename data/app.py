import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine data
df = pd.concat([df1, df2, df3])

# Filter pink morsel
df = df[df["product"] == "pink morsel"]

# Clean price column
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Create sales column
df["sales"] = df["price"] * df["quantity"]

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Dash app
app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Soul Foods Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#ff4b8b",
            "padding": "20px"
        }
    ),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={
            "textAlign": "center",
            "paddingBottom": "20px"
        }
    ),

    dcc.Graph(id="sales-chart")

], style={
    "backgroundColor": "#f5f5f5",
    "padding": "30px"
})


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    filtered_df = df

    if selected_region != "all":
        filtered_df = df[df["region"] == selected_region]

    sales_data = filtered_df.groupby("date")["sales"].sum().reset_index()

    fig = px.line(
        sales_data,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.title()} Region"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f5f5f5",
        font=dict(size=14)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)