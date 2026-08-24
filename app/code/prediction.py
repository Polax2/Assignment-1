import joblib
import pandas as pd
import numpy as np

inference = joblib.load("car_price_model.pkl")


def predict_price(brand, year, km_driven, fuel, seller_type,
                  transmission, owner, mileage, engine, max_power, seats):

    data = pd.DataFrame({
        "brand": [brand],
        "year": [year],
        "km_driven": [km_driven],
        "fuel": [fuel],
        "seller_type": [seller_type],
        "transmission": [transmission],
        "owner": [owner],
        "mileage": [mileage],
        "engine": [engine],
        "max_power": [max_power],
        "seats": [seats]
    })

    data = pd.get_dummies(
        data,
        columns=["brand", "fuel", "seller_type", "transmission"]
    )

    data = data.reindex(columns=inference["columns"], fill_value=0)

    data["year"] = inference["scaler_year"].transform(data[["year"]])
    data["km_driven"] = inference["scaler_km"].transform(data[["km_driven"]])
    data["mileage"] = inference["scaler_mileage"].transform(data[["mileage"]])
    data["engine"] = inference["scaler_engine"].transform(data[["engine"]])
    data["max_power"] = inference["scaler_power"].transform(data[["max_power"]])
    data["seats"] = inference["scaler_seats"].transform(data[["seats"]])

    price = inference["model"].predict(data)
    price = np.exp(price)

    return price[0]