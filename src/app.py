import pandas as pd
import os

import settings

import dash
from dash.dependencies import Output, Input, State
from dash import dcc
from dash import html

import dash_bootstrap_components as dbc

app = dash.Dash(title=settings.TITLE,
                update_title=settings.UPDATE_TITLE, 
                external_stylesheets=[dbc.themes.LUX])
    
@app.callback(Output('output_div', 'children'),
                  [Input('submit-button', 'n_clicks')],
                  [State('user-input', 'value')],
                  )
def update_output(clicks, input_value):
    if (clicks and input_value) is not None:
        # os.system("./src/animate_simulation.sh {}".format(input_value))
        app.layout = get_app_layout() 

def get_app_layout():
    title = html.H1(children="Advection Simulation Through Expicit Time-Stepping:")

    graph_html = html.H3(children="Simulation Render:")
    sim_graph = html.Video(id='simulation-graph', src=settings.VIDEO_PATH, controls=True, style={'width': '1000px', 'height': '500px', 'justify-content': 'center', 'align-items': 'center'})

    input_html = html.H3(children="Input for the number of timesteps to run the simulation:")
    input = dcc.Input(id='user-input', type='number', placeholder='Integer Input', style={'width': '1000px', 'height': '50px', 'margin-left': '10px'})
    html_button = html.Div(children=[html.Button(id='submit-button', type='submit', children='Submit', style={'margin-top': '20px', 'margin-bottom': '20px', 'justify-content': 'right', 'align-items': 'right'})])
    print_ = html.Div(id='output_div')

    div_block_style = {'margin': '10px', 'margin-top': '20px', 'justify-content': 'left', 'align-items': 'left'}
    layout = dbc.Container(children=[
        dbc.Row(children=[title], style={'justify-content': 'center', 'align-items': 'center', 'margin': '10px'}), 
        dbc.Row(children=[
            input_html, 
            input, 
            html_button, 
            print_], style=div_block_style),
        dbc.Row(children=[graph_html, sim_graph], style=div_block_style)
        ], 
        className="m-4", 
        fluid=True)

    return layout

app.layout = get_app_layout()
  
if __name__ == '__main__':
    app.run_server(debug=settings.DEBUG, 
                   port=settings.PORT)