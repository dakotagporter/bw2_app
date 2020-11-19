# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load

pipeline = load("assets/pipeline.joblib")

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Year'),
        dcc.Slider(
            id='year',
            min=1990,
            max=2017,
            step=1,
            value=2020,
            marks={n: str(n) for n in range(1990,2017,20)},
            className='mb-5',
        ),
        dcc.Markdown('#### Make'),
        dcc.Dropdown(
            id='Make',
            options = [
                {'label': 'Africa', 'value': 'Africa'},
                {'label': 'Americas', 'value': 'Americas'},
                {'label': 'Asia', 'value': 'Asia'},
                {'label': 'Europe', 'value': 'Europe'},
                {'label': 'Oceania', 'value': 'Oceania'},
            ],
            value = 'Africa',
            className='mb-5',
        ),
    ],
)

layout = dbc.Row([column1, column2])
