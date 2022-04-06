import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
app = dash.Dash()
df = pd.read_csv(
    "rajalakshmi.csv"
)
fig = px.bar(df, x="age", y="covid19_deaths", color="gender", hover_name="gender", hover_data=["age", "covid19_deaths", "data_as_of", "start_date", "end_date", "total_deaths"])
app.layout = html.Div([
    html.H4('COVID19 deaths by age'),
    dcc.Graph(id="graph", figure=fig)
])
if __name__ == '__main__':
    app.run_server(debug=False)
