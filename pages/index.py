# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Regress the Price!

            Avoid the pushy salesmen and time-consuming trips of car shopping and try your hands at this know-before-you-go opportunity. If you have an idea of the car your looking for, this tool can give you an idea of how much money you're going to spend before you step foot outside.

            ✅ Get a price in minutes by answering only a few questions!

            ❌ No hassel and no wasted resources. Give it a shot!

            """
        ),
        dcc.Link(dbc.Button('Get My Price', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
