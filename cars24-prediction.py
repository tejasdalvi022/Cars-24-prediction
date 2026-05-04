# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import warnings
# import joblib

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# warnings.filterwarnings('ignore')
# sns.set_style('whitegrid')

# st.title("🚗 Cars24 Price Prediction Deployment")

# # -----------------------------
# # LOAD DATA
# # -----------------------------
# car_dataset = pd.read_csv('cars24_data.csv')

# st.subheader("Dataset Preview")
# st.write(car_dataset.head())

# st.subheader("Shape of Dataset")
# st.write(car_dataset.shape)

# st.subheader("Dataset Columns")
# st.write("Columns:", car_dataset.columns)

# # st.subheader("Dataset Information")
# # st.write(car_dataset.info())

# st.subheader("Dataset Description")
# st.write(car_dataset.describe())

# st.subheader("Missing Values")
# st.write(car_dataset.isnull().sum())

# # -----------------------------
# # HANDLE MISSING VALUES
# # -----------------------------
# cat_cols = car_dataset.select_dtypes(include='object').columns
# for col in cat_cols:
#     car_dataset[col].fillna(car_dataset[col].mode()[0], inplace=True)

# car_dataset.drop(['url', 'createdDate'], axis=1, inplace=True)

# st.subheader("Handled Missing Values")
# st.write(car_dataset.isnull().sum())


# # -----------------------------
# # VISUALIZATIONS
# # -----------------------------
# st.subheader("VISUALIZATIONS")
# st.subheader("Price Distribution")
# fig1, ax1 = plt.subplots()
# sns.histplot(car_dataset['price'], bins=30, kde=True, ax=ax1)
# st.pyplot(fig1)

# import matplotlib.pyplot as plt
# import streamlit as st

# st.subheader("Numerical Columns")
# num_cols = ['year', 'kilometerdriven', 'ownernumber', 'benefits', 'price', 'discountprice']
# fig, ax = plt.subplots(figsize=(12, 8))
# car_dataset[num_cols].hist(ax=ax)
# plt.tight_layout()
# st.pyplot(fig)

# st.subheader("Fuel Type Distribution")
# fig2, ax2 = plt.subplots()
# car_dataset['fueltype'].value_counts().plot(kind='bar', ax=ax2)
# st.pyplot(fig2)

# st.subheader("Transmission Type Distribution")
# fig1, ax1 = plt.subplots(figsize=(6,4))
# sns.countplot(x='transmission', data=car_dataset, ax=ax1)
# ax1.set_title("Transmission Type")
# st.pyplot(fig1)

# st.subheader("Body Type Distribution")
# fig2, ax2 = plt.subplots(figsize=(8,4))
# car_dataset['bodytype'].value_counts().plot(kind='bar', ax=ax2)
# ax2.set_title("Distribution of Car Body Types")
# ax2.set_xlabel("Body Type")
# ax2.set_ylabel("Count")
# plt.xticks(rotation=45)
# st.pyplot(fig2)

# st.subheader("Top 10 Car Brands")
# fig3, ax3 = plt.subplots(figsize=(8,4))
# car_dataset['model'].value_counts().head(10).plot(kind='bar', ax=ax3)
# ax3.set_title("Top 10 Car Brands")
# ax3.set_xlabel("Brand")
# ax3.set_ylabel("Number of Cars")
# plt.xticks(rotation=45)
# st.pyplot(fig3)

# import streamlit as st
# import matplotlib.pyplot as plt

# st.subheader("Top 10 Registration States")
# fig, ax = plt.subplots(figsize=(8,4))
# car_dataset['registrationstate'].value_counts().head(10).plot(kind='bar', ax=ax)
# ax.set_title("Top 10 Registration States")
# ax.set_xlabel("State")
# ax.set_ylabel("Count")
# plt.xticks(rotation=45)
# st.pyplot(fig)

# st.subheader("Price vs Year")
# fig3, ax3 = plt.subplots()
# sns.scatterplot(x='year', y='price', data=car_dataset, ax=ax3)
# st.pyplot(fig3)


# st.subheader("Price vs Kilometer Driven")
# fig1, ax1 = plt.subplots(figsize=(6,4))
# sns.scatterplot(x='kilometerdriven', y='price', data=car_dataset, ax=ax1)
# ax1.set_title("Price vs Kilometer Driven")
# st.pyplot(fig1)

# st.subheader("Fuel Type vs Price")
# fig2, ax2 = plt.subplots(figsize=(6,4))
# sns.boxplot(x='fueltype', y='price', data=car_dataset, ax=ax2)
# ax2.set_title("Fuel Type vs Price")
# plt.xticks(rotation=45)
# st.pyplot(fig2)

# st.subheader("Before Removing Outliers")
# fig4, ax4 = plt.subplots(figsize=(6,4))
# sns.boxplot(y=car_dataset['price'], ax=ax4)
# ax4.set_title("Before Removing Outliers")
# st.pyplot(fig4)

# original_shape = car_dataset.shape

# Q1 = car_dataset['price'].quantile(0.25)
# Q3 = car_dataset['price'].quantile(0.75)
# IQR = Q3 - Q1

# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# car_dataset = car_dataset[
#     (car_dataset['price'] >= lower_bound) & 
#     (car_dataset['price'] <= upper_bound)
# ]

# # -----------------------------
# # After Removing Outliers
# # -----------------------------
# st.subheader("After Removing Outliers")
# fig5, ax5 = plt.subplots(figsize=(6,4))
# sns.boxplot(y=car_dataset['price'], ax=ax5)
# ax5.set_title("After Removing Outliers")
# st.pyplot(fig5)

# st.subheader("Dataset Size Change")
# st.write("Before:", original_shape)
# st.write("After:", car_dataset.shape)



# # -----------------------------
# # MODEL BUILDING
# # -----------------------------
# car_dataset['price_category'] = pd.qcut(car_dataset['price'], q=3, labels=[0,1,2])

# le = LabelEncoder()
# for col in car_dataset.select_dtypes(include='object').columns:
#     car_dataset[col] = le.fit_transform(car_dataset[col])

# X = car_dataset.drop(['price', 'price_category'], axis=1)
# y = car_dataset['price_category']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# rf = RandomForestClassifier(n_estimators=100)
# rf.fit(X_train, y_train)

# y_pred = rf.predict(X_test)

# # -----------------------------
# # MODEL RESULTS
# # -----------------------------
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
# models = {
#     "Logistic Regression": LogisticRegression(max_iter=1000),
#     "Decision Tree": DecisionTreeClassifier(),
#     "Random Forest": RandomForestClassifier(),
#     "KNN": KNeighborsClassifier(),
#     "SVM": SVC()
# }

# st.subheader("Model Accuracy Comparison")

# results = {}


# for name, model in models.items():
#     model.fit(X_train, y_train)
#     pred = model.predict(X_test)
#     acc = accuracy_score(y_test, pred)
#     results[name] = acc

# st.write(results)


# st.subheader("Selected Model Performance Accuracy (Random Forest)")

# accuracy = accuracy_score(y_test, y_pred)
# st.write(f"Accuracy: {accuracy*100:.2f}%")

# # st.subheader("Confusion Matrix")
# # st.write(confusion_matrix(y_test, y_pred))

# # st.subheader("Classification Report")
# # st.text(classification_report(y_test, y_pred))
# # -----------------------------
# # Classification Report as Table
# # -----------------------------
# st.subheader("Classification Report")
# report = classification_report(y_test, y_pred, output_dict=True)
# report_df = pd.DataFrame(report).transpose()
# report_df = report_df.round(2)  # round to 2 decimal places
# st.dataframe(report_df)

# st.subheader("Confusion Matrix")
# cm = confusion_matrix(y_test, y_pred)

# fig_cm, ax_cm = plt.subplots(figsize=(5,4))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax_cm)
# ax_cm.set_xlabel("Predicted")
# ax_cm.set_ylabel("Actual")
# st.pyplot(fig_cm)

# # -----------------------------
# # FEATURE IMPORTANCE
# # -----------------------------
# # Get feature importance
# importance = rf.feature_importances_

# # Create DataFrame
# feature_names = X.columns
# feature_importance = pd.DataFrame({
#     'Feature': feature_names,
#     'Importance': importance
# }).sort_values(by='Importance', ascending=False)

# # Plot
# fig, ax = plt.subplots(figsize=(8,6))
# ax.barh(feature_importance['Feature'], feature_importance['Importance'])
# ax.invert_yaxis()  # highest at top
# ax.set_title("Feature Importance")
# ax.set_xlabel("Importance")
# ax.set_ylabel("Features")

# st.pyplot(fig)
# # -----------------------------
# # SAVE MODEL BUTTON
# # -----------------------------
# if st.button("Save Model"):
#     joblib.dump(rf, "rf_model.pkl")
#     joblib.dump(scaler, "scaler.pkl")
#     st.success("✅ Model saved successfully!")
# Generated from: Cars24_Price_Prediction_Project.ipynb
# Converted at: 2026-04-26T05:35:00.432Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import streamlit as st

warnings.filterwarnings('ignore')

#Load_DataSets
df  = pd.read_csv('cars24_data.csv')

st.subheader("📊 Dataset Overview")

st.write("### First 5 Rows")
st.dataframe(df.head())

# Shape
st.write("### Shape of Dataset")
st.write(df.shape)

# Columns
st.write("### Columns")
st.write(list(df.columns))

# Info (special handling needed)
st.write("### Dataset Info")
import io
buffer = io.StringIO()
df.info(buf=buffer)
st.text(buffer.getvalue())

# Description
st.write("### Description")
st.dataframe(df.describe())

# Missing values
st.write("### Missing Values (Before)")
st.write(df.isnull().sum())

# Fill missing categorical values with mode
df['transmission'].fillna(df['transmission'].mode()[0], inplace=True)
df['bodytype'].fillna(df['bodytype'].mode()[0], inplace=True)

st.write("### Missing Values (After Initial Fill)")
st.write(df.isnull().sum())

#Check_Duplicates_values
st.write("### Duplicate Rows (Before)")
st.write(df.duplicated().sum())

#Remove_Duplicates_values
df.drop_duplicates(inplace=True,ignore_index=True)

#Again_Check_Duplicates
st.write("### Duplicate Rows (After Removing)")
st.write(df.duplicated().sum())

# Fill all categorical columns at once
cat_cols = df.select_dtypes(include='object').columns

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

df['transmission'].fillna('Unknown', inplace=True)
df['bodytype'].fillna('Unknown', inplace=True)

#drop unwanted columns

df.drop(['url', 'name'], axis=1, inplace=True)


st.write("### Remaining Columns")
st.write(list(df.columns))

# **VISUALIZATION**


# only numeric columns
num_cols = df.select_dtypes(include=['int64','float64']).columns
st.write("### Numerical Columns")
st.write(list(num_cols))

st.write("### Boxplots for Each Column")
for col in num_cols:
    st.write(f"Boxplot for: {col}")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, y=col, ax=ax)
    ax.set_title(col)
    st.pyplot(fig)

st.write("### Combined Boxplot")
fig, ax = plt.subplots(figsize=(10,5))
df.boxplot(ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

#Outlier_Capping

st.write("### Outlier Capping (IQR Method)")

def outlier_capping(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    st.write(f"{column} → Lower: {lower:.2f}, Upper: {upper:.2f}")

    df[column] = df[column].apply(
        lambda x: lower if x < lower else upper if x > upper else x
    )
    return df

for col in num_cols:
    if col != 'price':
        df = outlier_capping(df, col)
# Recalculate numeric columns
num_cols = df.select_dtypes(include=['int64','float64']).columns

# After Outlier Boxplot
st.write("### Boxplot After Outlier Capping")
fig, ax = plt.subplots(figsize=(10,5))
df[num_cols].boxplot(ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)


num_cols = df.select_dtypes(include=['int64','float64']).columns

st.write("### 📊 Numerical Columns After Capping")
st.write(num_cols)


# create correlation properly
num_df = df.select_dtypes(include=['int64','float64'])

# correlation
st.write("### Correlation Matrix")

num_df = df.select_dtypes(include=['int64','float64'])
num_df = num_df.loc[:, num_df.nunique() > 1]

corr = num_df.corr()

st.dataframe(corr)

# Heatmap
st.write("### Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)

#Feature Selection
st.write("### Feature Selection")

target = df[['price']]
features = df.drop(columns=['price'])

st.write("Features Preview")
st.dataframe(features.head())

st.write("Target Preview")
st.dataframe(target.head())


#Multicollinearity_Check_using_VIF
numerical_features = features.select_dtypes(include=[np.number])


#Scatter_plot_Bivariate
st.write("### Year vs Price")
fig, ax = plt.subplots()
sns.scatterplot(x=df['year'], y=df['price'], ax=ax)
st.pyplot(fig)

st.write("### Kilometer Driven vs Price")
fig, ax = plt.subplots()
sns.scatterplot(x=df['kilometerdriven'], y=df['price'], ax=ax)
st.pyplot(fig)

# **MODEL BUILDING and MODEL EVALUATION**
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import r2_score, mean_squared_error

# Encoding
st.subheader("🔤 Encoding Categorical Data")
le = LabelEncoder()

categorical_cols = df.select_dtypes(include='object').columns

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])
st.write("Encoded Columns:", categorical_cols)


# Feature Selection and Target

X = df.drop("price", axis=1)
y = df["price"]

# Train-Test Split


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

st.write("Train Shape:", X_train.shape)
st.write("Test Shape:", X_test.shape)

# Feature Scaling


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# MODELS


# Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR


import numpy as np
from sklearn.metrics import r2_score, mean_squared_error

def eval_model(name, y_train, y_train_pred, y_test, y_test_pred):
    st.write(f"### 📊 {name}")
    
    st.write({
        "Train R2": r2_score(y_train, y_train_pred),
        "Test R2": r2_score(y_test, y_test_pred),
        "Train RMSE": np.sqrt(mean_squared_error(y_train, y_train_pred)),
        "Test RMSE": np.sqrt(mean_squared_error(y_test, y_test_pred))
    })


# 1. Linear Regression


lr = LinearRegression()
lr.fit(X_train, y_train)

y_train_lr = lr.predict(X_train)
y_test_lr = lr.predict(X_test)

eval_model("Linear Regression", y_train, y_train_lr, y_test, y_test_lr)

# 2. K-Nearest Neighbors (KNN)


knn = KNeighborsRegressor()
knn.fit(X_train_scaled, y_train)

y_train_knn = knn.predict(X_train_scaled)
y_test_knn = knn.predict(X_test_scaled)

eval_model("K-Nearest Neighbors (KNN)", y_train, y_train_knn, y_test, y_test_knn)

# 3. Support Vectore Machine (SVM)


svm = SVR()
svm.fit(X_train_scaled, y_train)

y_train_svm = svm.predict(X_train_scaled)
y_test_svm = svm.predict(X_test_scaled)

eval_model("Support Vector Regressor", y_train, y_train_svm, y_test, y_test_svm)

# 4. Decision Tree
dt = DecisionTreeRegressor(max_depth=5, random_state=42)
dt.fit(X_train, y_train)

y_test_dt = dt.predict(X_test)

eval_model("Decision Tree", y_train, dt.predict(X_train), y_test, y_test_dt)


#5. Random RandomForestRegressor
rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

y_test_rf = rf.predict(X_test)

eval_model("Random Forest", y_train, rf.predict(X_train), y_test, y_test_rf)


# DEEP LEARNING MODEL - ANN


from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore


ann = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1)
])

ann.compile(optimizer='adam', loss='mse')

history = ann.fit(
    X_train_scaled, y_train,
    epochs=50,
    validation_split=0.2,
    verbose=0
)

# Predictions
y_train_ann = ann.predict(X_train_scaled).flatten()
y_test_ann = ann.predict(X_test_scaled).flatten()

eval_model("ANN", y_train, y_train_ann, y_test, y_test_ann)

# ANN- LOSS Graph
# Loss Graph
fig, ax = plt.subplots()
ax.plot(history.history['loss'])
ax.set_title("ANN Loss")
st.pyplot(fig)


st.subheader("📊 ANN: Actual vs Predicted")

fig, ax = plt.subplots()

ax.scatter(y_test, y_test_ann)
ax.set_xlabel("Actual Values")
ax.set_ylabel("Predicted Values")
ax.set_title("ANN: Actual vs Predicted")

st.pyplot(fig)


results = [
    ["Linear Regression", r2_score(y_test, y_test_lr), np.sqrt(mean_squared_error(y_test, y_test_lr))],
    ["Decision Tree", r2_score(y_test, y_test_dt), np.sqrt(mean_squared_error(y_test, y_test_dt))],
    ["Random Forest", r2_score(y_test, y_test_rf), np.sqrt(mean_squared_error(y_test, y_test_rf))],
    ["KNN", r2_score(y_test, y_test_knn), np.sqrt(mean_squared_error(y_test, y_test_knn))],
    ["SVM", r2_score(y_test, y_test_svm), np.sqrt(mean_squared_error(y_test, y_test_svm))]
]



st.subheader("📊 Model Performance")
results_df = pd.DataFrame(results, columns=["Model", "R2 Score", "RMSE"])

st.dataframe(results_df)

print(f"{'Model':<20} {'R2 Score':<10} {'RMSE':<10}")
print("-"*40)

for model, r2, rmse in results:
    print(f"{model:<20} {round(r2,4):<10} {round(rmse,2):<10}")

import matplotlib.pyplot as plt

st.subheader("📈 Model Performance (R2 Score)")

models = [r[0] for r in results]
scores = [r[1] for r in results]

fig, ax = plt.subplots()
ax.bar(models, scores)

for i in range(len(models)):
    ax.text(i, scores[i], str(round(scores[i]*100,1)) + "%", ha='center')

ax.set_title("Model Performance")
ax.set_xlabel("Models")
ax.set_ylabel("R2 Score")
plt.xticks(rotation=30)

st.pyplot(fig)

# Best based on R2 (higher is better)
best_r2_index = results_df["R2 Score"].idxmax()

# Best based on RMSE (lower is better)
best_rmse_index = results_df["RMSE"].idxmin()

st.subheader("🏆 Final Model Selection")

st.write("Best Model based on R2 Score:",
         results_df["Model"][best_r2_index])

st.write("Best Model based on RMSE:",
         results_df["Model"][best_rmse_index])

if best_r2_index == best_rmse_index:
    final_model = results_df["Model"][best_r2_index]
else:
    final_model = results_df.sort_values(
        by=["R2 Score", "RMSE"],
        ascending=[False, True]
    ).iloc[0]["Model"]

st.success(f"✅ Final Selected Best Model: {final_model}")


import matplotlib.pyplot as plt
st.subheader("📊 Random Forest: Actual vs Predicted")

fig, ax = plt.subplots()

ax.scatter(y_test, y_test_rf)

# Perfect prediction line
ax.plot([y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        'r--')

ax.set_xlabel("Actual Price")
ax.set_ylabel("Predicted Price")
ax.set_title("Random Forest Performance")

st.pyplot(fig)

# # Feature Importance

st.subheader("🌟 Feature Importance (Random Forest)")

# Create DataFrame (only once)
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
}).sort_values(by="Importance", ascending=False)

# Show table
st.dataframe(feature_importance)

# Plot
fig, ax = plt.subplots()

ax.barh(feature_importance["Feature"], feature_importance["Importance"])
ax.invert_yaxis()
ax.set_title("Feature Importance (Random Forest)")
ax.set_xlabel("Importance")
ax.set_ylabel("Features")
st.pyplot(fig)

#SAVE THE MODEL 
import joblib
joblib.dump(rf, "rf_model.pkl")
joblib.dump(scaler, "scaler.pkl")

st.success("✅ Model trained and saved successfully!")