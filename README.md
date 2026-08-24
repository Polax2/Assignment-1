# Car Price Prediction- Car's Price Reveal Party

## About the project

The project is built based on the provided Car Price dataset. It contains the full data preprocessing, modelling and then, based on the chosen model, a simple web application was built and deployed.

## Machine Learning

Four Machine Learning models were tested: Linear Regression, Random Forest, Decision Tree and SVM. Their performance was evaluated using MSE, RMSE and R² metrics. Linear Regression was chosen as the final model used for the web application.

## Repository

The repository contains the Jupyter Notebook with the full data investigation, preprocessing, model training and evaluation. It also contains the `app` folder with all files needed to run the web application.

## Running the application

The application can be run using the `app` folder. One should prompt:
docker compose up --build

After building and starting the container, the application is available at:
http://127.0.0.1:8050

To stop the application one should run:
docker compose down

## Web Application

The web application contains three main pages: the home page, the instruction page and the prediction page. From the home page the user can navigate either to the instructions or directly to the predictor.

On the prediction page, some fields are required and some can be left empty.
Required fields:

- Brand
- Year
- Kilometers driven
- Transmission
- Engine
- Max power

Optional fields:

- Fuel
- Seller type
- Owner
- Mileage
- Seats

If an optional field is left empty, the application fills the missing value using the imputation values calculated from the training data or the most common mode of the featire withing the training set.
The application also contains basic input validation. Required fields cannot be left empty and negative values for numerical features are rejected before the prediction is made.

## Used tools

The project was developed using Python, Pandas, Scikit-learn and Dash. Docker was used to containerize the final web application.
