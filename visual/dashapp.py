"""
    Dash http service for get tickers values
"""
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dataget import get_data_ticker

# Dash application for visualisation http data
app = dash.Dash(__name__, prevent_initial_callbacks=True)

# Labels and values for dropdown list
opts = [{'label': 'ticker_' + f'{i:02}', 'value': i} for i in range(100)]

# Greating http view layout
app.layout = html.Div(children=[
    dcc.Dropdown(
        id='ticker-dropdown',
        options=opts,
        value=0,
        clearable=False,
        className="dropdown",
    ),
    dcc.Graph(
        id='price-graph',
        figure={
            'layout': {
                'title': 'Data Price'
            }
        }
    ),
    dcc.Interval(
        id='graph-update',
        interval=1*1000,
        n_intervals=0
    )
])


@app.callback(Output('price-graph', 'figure'),
              [Input('ticker-dropdown', 'value'),
               Input('graph-update', 'n_intervals')
               ]
              )
def update_graph(value, n_intervals):
    """* Callback function for update Graph from GET response """
    Y = get_data_ticker(value, 0)
    X = list(range(len(Y)))
    graphic = go.Figure(data=[go.Scatter(x=X, y=Y)])
    return graphic


if __name__ == "__main__":
    # Run dash http service with default values
    # host = os.getenv("HOST", "127.0.0.1"), port = os.getenv("PORT", "8050")
    app.run(debug=True)
