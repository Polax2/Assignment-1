from dash import Dash, html, dcc, Input, Output, State
from prediction import predict_price
import joblib

inference = joblib.load("car_price_model.pkl")

app = Dash(suppress_callback_exceptions=True)

page_style = {
    "backgroundColor": "#f3f3f3",
    "minHeight": "100vh",
    "padding": "30px"
}

container_style = {
    "maxWidth": "1100px",
    "margin": "auto"
}

section_style = {
    "backgroundColor": "white",
    "marginBottom": "15px",
    "padding": "25px 40px"
}

title_style = {
    "color": "#17365d",
    "marginBottom": "25px"
}

row_style = {
    "display": "grid",
    "gridTemplateColumns": "280px 1fr",
    "alignItems": "center",
    "gap": "30px",
    "marginBottom": "15px"
}

label_style = {
    "fontSize": "17px",
    "textAlign": "right"
}

field_style = {
    "width": "100%"
}

input_style = {
    "width": "100%",
    "height": "42px",
    "boxSizing": "border-box",
    "padding": "0 12px",
    "fontSize": "16px"
}

button_style = {
    "padding": "12px 35px",
    "fontSize": "17px",
    "backgroundColor": "#17365d",
    "color": "white",
    "border": "none",
    "borderRadius": "4px",
    "cursor": "pointer"
}

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(id="page")
])


home_page = html.Div(

    style={
        "backgroundColor": "#f5f5f7",
        "minHeight": "100vh",
        "padding": "50px 30px"
    },

    children=[

        html.H1(
            "Car's Price Reveal Party",
            style={
                "textAlign": "center",
                "fontSize": "48px",
                "marginBottom": "50px"
            }
        ),

        html.Div(

            style={
                "display": "flex",
                "justifyContent": "center",
                "gap": "70px",
                "maxWidth": "1100px",
                "margin": "auto"
            },

            children=[

                html.Div(

                    style={
                        "width": "450px",
                        "textAlign": "center"
                    },

                    children=[

                        html.Img(
                            src="/assets/instructions.jpg",
                            style={
                                "width": "100%",
                                "height": "250px",
                                "objectFit": "cover",
                                "borderRadius": "25px"
                            }
                        ),

                        html.H2("Instructions"),

                        html.P(
                            "Learn how to use the predictor",
                            style={
                                "fontSize": "18px",
                                "lineHeight": "1.5"
                            }
                        ),

                        dcc.Link(
                            "Read instructions ›",
                            href="/instructions",
                            style={
                                "fontSize": "18px",
                                "textDecoration": "none",
                                "color": "#3366cc"
                            }
                        )
                    ]
                ),

                html.Div(

                    style={
                        "width": "450px",
                        "textAlign": "center"
                    },

                    children=[

                        html.Img(
                            src="/assets/cars.jpg",
                            style={
                                "width": "100%",
                                "height": "250px",
                                "objectFit": "cover",
                                "borderRadius": "25px"
                            }
                        ),

                        html.H2("Predictor"),

                        html.P(
                            "Get your car's estimated selling price",
                            style={
                                "fontSize": "18px",
                                "lineHeight": "1.5"
                            }
                        ),

                        dcc.Link(
                            "Start prediction ›",
                            href="/predict",
                            style={
                                "fontSize": "18px",
                                "textDecoration": "none",
                                "color": "#3366cc"
                            }
                        )
                    ]
                )
            ]
        )
    ]
)

instructions_page = html.Div(

    style={
        "backgroundColor": "#f5f5f7",
        "minHeight": "100vh",
        "padding": "60px 30px"
    },

    children=[

        html.Div(

            style={
                "maxWidth": "1000px",
                "margin": "auto"
            },

            children=[

                html.H1(
                    "Instructions",
                    style={
                        "fontSize": "52px",
                        "marginBottom": "60px",
                        "color": "#17365d"
                    }
                ),

                html.H2(
                    "HOW TO USE THE PREDICTOR",
                    style={
                        "fontSize": "28px",
                        "color": "#17365d",
                        "marginBottom": "30px"
                    }
                ),
                
                html.Ol(

                    style={
                        "fontSize": "21px",
                        "lineHeight": "1.9",
                        "paddingLeft": "30px"
                    },

                    children=[
                        html.Li("Open the Car's Price Reveal Party predictor"),
                        html.Li("Enter the information about the car"),
                        html.Li("Fields marked with * are required"),
                        html.Li("Optional fields can be left empty"),
                        html.Li("Missing optional values will be automatically estimated"),
                        html.Li("If you decide to leave non-obligatory fields empty the estimations could be worse quality"),
                        html.Li("Click the Predict price button"),
                        html.Li("The estimated selling price will be displayed below the form")
                    ]
                ),

                html.Div(
                    style={
                        "marginTop": "50px",
                        "padding": "25px 30px",
                        "backgroundColor": "white",
                        "borderRadius": "15px"
                    },

                    children=[

                        html.H3(
                            "Important",
                            style={
                                "fontSize": "23px",
                                "marginTop": "0"
                            }
                        ),

                        html.P(
                            "The predicted price is an estimate generated by a machine learning model and may differ from the actual market price.",
                            style={
                                "fontSize": "19px",
                                "lineHeight": "1.6",
                                "marginBottom": "0"
                            }
                        )
                    ]
                ),

                html.Div(

                    style={
                        "marginTop": "45px",
                        "textAlign": "center"
                    },

                    children=[

                        dcc.Link(
                            "‹ Back to home",
                            href="/",
                            style={
                                "fontSize": "20px",
                                "textDecoration": "none",
                                "color": "#3366cc",
                                "marginRight": "40px"
                            }
                        ),

                        dcc.Link(
                            "Start prediction ›",
                            href="/predict",
                            style={
                                "fontSize": "20px",
                                "textDecoration": "none",
                                "color": "#3366cc"
                            }
                        )
                    ]
                )
            ]
        )
    ]
)


predict_page = html.Div(

    style=page_style,

    children=[

        html.Div(

            style=container_style,

            children=[

                html.Div(

                    style={
                        "backgroundColor": "white",
                        "padding": "20px 40px",
                        "marginBottom": "15px"
                    },

                    children=[

                        html.H1(
                            "Car's Price Reveal Party",
                            style={"color": "#17365d"}
                        ),

                        html.Div(
                            "Enter the information about the car. Fields marked with * are required.",
                            style={
                                "backgroundColor": "#f4f7fa",
                                "padding": "15px",
                                "fontSize": "16px"
                            }
                        )
                    ]
                ),


                html.Div(

                    style=section_style,

                    children=[

                        html.H2(
                            "Basic information",
                            style=title_style
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label("Brand *", style=label_style),

                                dcc.Dropdown(
                                    id="brand",
                                    options=[
                                        {"label": x, "value": x}
                                        for x in [
                                            "Mahindra", "Hyundai", "Toyota",
                                            "Maruti", "Tata", "Ford",
                                            "Nissan", "Honda", "Renault",
                                            "Datsun", "Chevrolet", "Skoda",
                                            "Audi", "Daewoo", "Fiat",
                                            "Kia", "BMW", "Volkswagen",
                                            "Jeep", "Mercedes-Benz",
                                            "Mitsubishi", "Jaguar", "MG",
                                            "Land", "Ambassador", "Ashok",
                                            "Volvo", "Opel", "Force",
                                            "Isuzu", "Peugeot", "Lexus"
                                        ]
                                    ],
                                    placeholder="Select brand",
                                    searchable=True,
                                    clearable=False,
                                    style=field_style
                                )
                            ]
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label("Year *", style=label_style),

                                dcc.Dropdown(
                                    id="year",
                                    options=[
                                        {"label": str(x), "value": x}
                                        for x in range(1990, 2027)
                                    ],
                                    placeholder="Select year",
                                    clearable=False,
                                    style=field_style
                                )
                            ]
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label(
                                    "Kilometers driven *",
                                    style=label_style
                                ),

                                dcc.Input(
                                    id="km_driven",
                                    type="number",
                                    placeholder="Enter kilometers driven",
                                    style=input_style
                                )
                            ]
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label("Fuel", style=label_style),

                                dcc.Dropdown(
                                    id="fuel",
                                    options=[
                                        {
                                            "label": "Diesel",
                                            "value": "Diesel"
                                        },
                                        {
                                            "label": "Petrol",
                                            "value": "Petrol"
                                        }
                                    ],
                                    placeholder="Select fuel or leave empty",
                                    clearable=True,
                                    searchable=False,
                                    style=field_style
                                )
                            ]
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label(
                                    "Seller type",
                                    style=label_style
                                ),

                                dcc.Dropdown(
                                    id="seller_type",
                                    options=[
                                        {
                                            "label": "Individual",
                                            "value": "Individual"
                                        },
                                        {
                                            "label": "Dealer",
                                            "value": "Dealer"
                                        },
                                        {
                                            "label": "Trustmark Dealer",
                                            "value": "Trustmark Dealer"
                                        }
                                    ],
                                    placeholder="Select seller type or leave empty",
                                    clearable=True,
                                    searchable=False,
                                    style=field_style
                                )
                            ]
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label(
                                    "Transmission *",
                                    style=label_style
                                ),

                                dcc.Dropdown(
                                    id="transmission",
                                    options=[
                                        {
                                            "label": "Manual",
                                            "value": "Manual"
                                        },
                                        {
                                            "label": "Automatic",
                                            "value": "Automatic"
                                        }
                                    ],
                                    placeholder="Select transmission",
                                    clearable=False,
                                    searchable=False,
                                    style=field_style
                                )
                            ]
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label("Owner", style=label_style),

                                dcc.Dropdown(
                                    id="owner",
                                    options=[
                                        {
                                            "label": "First Owner",
                                            "value": 1
                                        },
                                        {
                                            "label": "Second Owner",
                                            "value": 2
                                        },
                                        {
                                            "label": "Third Owner",
                                            "value": 3
                                        },
                                        {
                                            "label": "Fourth & Above Owner",
                                            "value": 4
                                        }
                                    ],
                                    placeholder="Select owner or leave empty",
                                    clearable=True,
                                    searchable=False,
                                    style=field_style
                                )
                            ]
                        )
                    ]
                ),


                html.Div(

                    style=section_style,

                    children=[

                        html.H2(
                            "Technical information",
                            style=title_style
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label(
                                    "Fuel efficiency (km/L)",
                                    style=label_style
                                ),

                                dcc.Input(
                                    id="mileage",
                                    type="number",
                                    placeholder="Enter fuel efficiency or leave empty",
                                    style=input_style
                                )
                            ]
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label(
                                    "Engine (CC) *",
                                    style=label_style
                                ),

                                dcc.Input(
                                    id="engine",
                                    type="number",
                                    placeholder="Enter engine size",
                                    style=input_style
                                )
                            ]
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label(
                                    "Max power (bhp) *",
                                    style=label_style
                                ),

                                dcc.Input(
                                    id="max_power",
                                    type="number",
                                    placeholder="Enter max power",
                                    style=input_style
                                )
                            ]
                        ),

                        html.Div(
                            style=row_style,
                            children=[
                                html.Label("Seats", style=label_style),

                                dcc.Dropdown(
                                    id="seats",
                                    options=[
                                        {
                                            "label": str(x),
                                            "value": x
                                        }
                                        for x in range(2, 15)
                                    ],
                                    placeholder="Select seats or leave empty",
                                    clearable=True,
                                    searchable=False,
                                    style=field_style
                                )
                            ]
                        )
                    ]
                ),


                html.Div(

                    style={
                        "backgroundColor": "white",
                        "padding": "25px 40px",
                        "textAlign": "center"
                    },

                    children=[

                        html.Button(
                            "Predict price",
                            id="predict_button",
                            style=button_style
                        ),

                        html.H2(
                            id="result",
                            style={
                                "color": "#17365d",
                                "marginTop": "25px"
                            }
                        ),

                        html.Br(),

                        dcc.Link(
                            html.Button("Back to home"),
                            href="/"
                        )
                    ]
                )
            ]
        )
    ]
)


@app.callback(
    Output("page", "children"),
    Input("url", "pathname")
)
def show_page(pathname):

    if pathname == "/instructions":
        return instructions_page

    if pathname == "/predict":
        return predict_page

    return home_page


@app.callback(
    Output("result", "children"),

    Input("predict_button", "n_clicks"),

    State("brand", "value"),
    State("year", "value"),
    State("km_driven", "value"),
    State("fuel", "value"),
    State("seller_type", "value"),
    State("transmission", "value"),
    State("owner", "value"),
    State("mileage", "value"),
    State("engine", "value"),
    State("max_power", "value"),
    State("seats", "value")
)
def predict(n_clicks, brand, year, km_driven, fuel, seller_type,
            transmission, owner, mileage, engine, max_power, seats):

    if n_clicks is None:
      return ""

    if brand is None or year is None or km_driven is None or \
      transmission is None or engine is None or max_power is None:
      return "Please fill in all required fields."

    if km_driven < 0 or engine <= 0 or max_power <= 0:
      return "Please enter valid positive values."

    if mileage is not None and mileage < 0:
      return "Please enter a valid mileage value."

    

    if fuel is None:
        fuel = inference["mode_fuel"]

    if seller_type is None:
        seller_type = inference["mode_seller_type"]

    if owner is None:
        owner = inference["mode_owner"]

    if mileage is None:
        mileage = inference["mean_mileage"]

    if seats is None:
        seats = inference["median_seats"]

    price = predict_price(
        brand,
        year,
        km_driven,
        fuel,
        seller_type,
        transmission,
        owner,
        mileage,
        engine,
        max_power,
        seats
    )

    return f"Predicted price: {price:.2f} $"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)