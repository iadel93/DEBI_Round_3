from dash import Dash, dcc, html
from plotly import express as px    
from plotly import graph_objects as go

data = px.data.iris()
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Iris Data Visualization with Dash'),
    dcc.Graph(
        id='iris-scatter',
        figure=px.scatter(data, x='sepal_width', y='sepal_length', color='species', title='Iris Sepal Dimensions')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)