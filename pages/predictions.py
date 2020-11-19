# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Imports from this application
from app import app
from joblib import load

pipeline = load("assets/pipeline.joblib")

@app.callback(
    Output('prediction-content', 'children'),
    [Input('make', 'value')
    Input('year', 'value'),
    Input('engine_fuel_type', 'value'),
    Input('engine_hp', 'value'),
    Input('engine_cylinders', 'value'),
    Input('transmission_type', 'value'),
    Input('driven_wheels', 'value'),
    Input('number_of_doors', 'value'),
    Input('vehicle_size', 'value'),
    Input('vehicle_style', 'value'),
    Input('highway_mpg', 'value'),
    Input('city_mpg', 'value'),
    Input('popularity', 'value')],
)
def predict(make, year, engine_fuel_type, engine_hp, engine_cylinders, transmission_type, driven_wheels, number_of_doors, vehicle_size, vehicle_style, highway_mpg, city_mpg, popularity):
    df = pd.DataFrame(
        columns=['make',
                'year',
                'engine_fuel_type',
                'engine_hp',
                'engine_cylinders',
                'transmission_type',
                'driven_wheels', 'number_of_doors',
                'vehicle_size',
                'vehicle_style',
                'highway_mpg',
                'city_mpg',
                'popularity'],
        data=[[make, year, engine_fuel_type, engine_hp, engine_cylinders, transmission_type, driven_wheels, number_of_doors, vehicle_size, vehicle_style, highway_mpg, city_mpg, popularity]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'${y_pred:.2f}'

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions

            Answer the following questions to get your price!

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Make'),
        dcc.Dropdown(
            id='make',
            options = [
                {'label': 'Chevrolet', 'value': 'chevrolet'},
                {'label': 'Toyota', 'value': 'toyota'},
                {'label': 'Dodge', 'value': 'dodge'},
                {'label': 'Ford', 'value': 'ford'},
                {'label': 'Volkswagen', 'value': 'volkswagen'},
                {'label': 'Other', 'value': 'other'},
            ],
            value = 'Chevrolet',
            className='mb-5',
        ),
        dcc.Markdown('#### Year'),
        dcc.Slider(
            id='year',
            min=1990,
            max=2017,
            step=1,
            value=1990,
            marks={n: str(n) for n in range(1990,2017,20)},
            className='mb-5',
        ),
        dcc.Markdown('### Fuel Type'),
        dcc.Dropdown(
            id='engine_fuel_type',
            options = [
                {'label': 'Regular Unleaded', 'value': 'regular unleaded'},
                {'label': 'Premium Unleaded', 'value': 'premium unleaded (recommended)'},
                {'label': 'Premium Unleaded (required)', 'value': 'premium unleaded (required)'},
                {'label': 'Flex-Fuel', 'value': 'flex-fuel (unleaded/e85)'},
                {'label': 'Flex-Fuel Premium', 'value': 'flex-fuel (premium unleaded recommended/e85)'},
                {'label': 'Flex-Fuel Premium (required)', 'value': 'flex-fuel (premium unleaded required/e85)'},
                {'label': 'Flex-Fuel Natural Gas', 'value': 'flex-fuel (unleaded/natural gas)'},
                {'label': 'Diesel', 'value': 'diesel'},
                {'label': 'Electric', 'value': 'electric'},
                {'label': 'Natural Gas', 'value': 'natural gas'},
            ],
            value = 'Regular Unleaded',
            className='mb-5',
        ),
        dcc.Markdown('#### Horsepower'),
        dcc.Slider(
            id='engine_hp',
            min=55,
            max=707,
            step=1,
            value=55,
            marks={n: str(n) for n in range(55,707,20)},
            className='mb-5',
        ),
        dcc.Markdown('#### Cylinders'),
        dcc.Slider(
            id='engine_cylinders',
            min=0,
            max=12,
            step=1,
            value=0,
            marks={n: str(n) for n in range(0,12,2)},
            className='mb-5',
        ),
        dcc.Markdown('### Transmission'),
        dcc.Dropdown(
            id='transmission_type',
            options = [
                {'label': 'Automatic', 'value': 'automatic'},
                {'label': 'Manual', 'value': 'manual'},
                {'label': 'Automated Manual', 'value': 'automated_manual'},
                {'label': 'Direct Drive', 'value': 'direct_drive'},
                {'label': 'Unknown', 'value': 'unknown'},
            ],
            value = 'Automatic',
            className='mb-5',
        ),
        dcc.Markdown('### Wheel Drive'),
        dcc.Dropdown(
            id='driven_wheels',
            options = [
                {'label': 'Front Wheel Drive', 'value': 'front wheel drive'},
                {'label': 'Rear Wheel Drive', 'value': 'rear wheel drive'},
                {'label': 'All Wheel Drive', 'value': 'all wheel drive'},
                {'label': 'Four Wheel Drive', 'value': 'four wheel drive'},
            ],
            value = 'Front Wheel Drive',
            className='mb-5',
        ),
        dcc.Markdown('#### Doors'),
        dcc.Slider(
            id='number_of_doors',
            min=2,
            max=4,
            step=1,
            value=2,
            marks={n: str(n) for n in range(2,4,1)},
            className='mb-5',
        ),
        dcc.Markdown('### Vehicle Size'),
        dcc.Dropdown(
            id='vehicle_size',
            options = [
                {'label': 'Compact', 'value': 'compact'},
                {'label': 'Midsize', 'value': 'midsize'},
                {'label': 'Large', 'value': 'Large'},
            ],
            value = 'Compact',
            className='mb-5',
        ),
        dcc.Markdown('### Vehicle Style'),
        dcc.Dropdown(
            id='vehicle_style',
            options = [
                {'label': 'Sedan', 'value': 'sedan'},
                {'label': '4 Door SUV', 'value': '4dr suv'},
                {'label': 'Coupe', 'value': 'coupe'},
                {'label': '4 Door Hatchback', 'value': '4dr hatchback'},
                {'label': 'Crew Cab Pickup', 'value': 'crew cab pickup'},
                {'label': 'Extended Cab Pickup', 'value': 'extended cab pickup'},
                {'label': 'Wagon', 'value': 'wagon'},
                {'label': 'Convertible', 'value': 'convertible'},
                {'label': '2 Door Hatchback', 'value': '2dr hatchback'},
                {'label': 'Passenger Minivan', 'value': 'passenger minivan'},
                {'label': 'Regular Cab Pickup', 'value': 'regular cab pickup'},
                {'label': '2 Door SUV', 'value': '2dr suv'},
                {'label': 'Passenger Van', 'value': 'passenger van'},
                {'label': 'Cargo Van', 'value': 'cargo van'},
                {'label': 'Cargo Minivan', 'value': 'cargo minivan'},
                {'label': 'Convertible SUV', 'value': 'convertible suv'},
            ],
            value = 'Sedan',
            className='mb-5',
        ),
        dcc.Markdown('#### Highway MPG'),
        dcc.Slider(
            id='highway_mpg',
            min=12,
            max=354,
            step=1,
            value=12,
            marks={n: str(n) for n in range(12,354,10)},
            className='mb-5',
        ),
        dcc.Markdown('#### City MPG'),
        dcc.Slider(
            id='city_mpg',
            min=10,
            max=137,
            step=1,
            value=10,
            marks={n: str(n) for n in range(10, 137, 10)},
            className='mb-5',
        ),
        dcc.Markdown('#### Popularity'),
        dcc.Slider(
            id='popularity',
            min=21,
            max=5657,
            step=1,
            value=21,
            marks={n: str(n) for n in range(21,5657,10)},
            className='mb-5',
        ),
        dcc.Markdown('### Luxury'),
        dcc.Dropdown(
            id='luxury',
            options = [
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0},
            ],
            value = 'No',
            className='mb-5',
        ),
    ],
)

layout = dbc.Row([column1, column2])
