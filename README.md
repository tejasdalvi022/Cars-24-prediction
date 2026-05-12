# Car-Price-Prediction-cars-24-Dataset
Live Link - 

# 🚗 Cars24 Price Prediction
This project predicts used car prices based on features such as car name, year, location, fuel type, drive type, distance driven, and ownership details.
The dataset was sourced from Cars24 data, cleaned, and analyzed before training a Linear Regression model.

## 📌 Project Workflow

1. Data Preparation
Loaded dataset cars24_data.csv
Cleaned and preprocessed the data:
Handled categorical columns (Car Name, Location, Fuel, Drive, Type, Owner)
2. Exploratory Data Analysis (EDA)
Boxplots for categorical features (Fuel, Drive, Type, Owner)
Identified outliers in price distribution
3. Outlier Removal
Applied IQR-based filtering within groups:
Fuel type
Drive type
Car type
Owner
4. Model Building
Features (X): All columns except Price
Target (y): Price
Preprocessing:
One-hot encoded categorical features
Model: Linear Regression
 model training
5. Model Evaluation
Metrics used:
R² Score
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
Example Results:
MAE: ~ (value depends on dataset)
RMSE: ~ (value depends on dataset)
6. Model Deployment
Final trained model saved as:
RandomForestRegressor
🛠️ Tech Stack
Python 🐍
Pandas, NumPy – Data manipulation
Matplotlib, Seaborn – Visualization
Scikit-learn – Preprocessing & ML model
Pickle – Model saving
📂 Project Structure
├── Cars 24 Prediction.ipynb     # Jupyter Notebook with full code
├── cars24_data.csv         # Dataset (not included here)
├── car_prediction_model.pkl  # Saved trained model
└── README.md                    # Project documentation
🚀 How to Run
Clone this repository:

git clone https://github.com/your-username/cars24_price_prediction.git
cd cars24-price-prediction
Install dependencies:

pip install -r requirements.txt
Run the notebook or script to train the model:

jupyter notebook "Cars24_Prediction.ipynb"
Use the saved model (car_prediction_model.pkl) for predictions:

import pickle

model = pickle.load(open('car_prediction_model.pkl', 'rb'))
prediction = model.predict([your_input_features])
print(prediction)
📊 Example Visualization
Year vs Price trend
Distance vs Price regression
Fuel/Drive/Type vs Price distributions
(visuals available in the notebook)

### Deployment Model 
After succesfull trained and saved the model 
Run the deployment for the cars24_prediction.py
It will direct you to the web browser from streamlit and the model deployment is hosted on the localhost for the cars24_prediction


