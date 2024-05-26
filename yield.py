import streamlit as st
import pandas as pd
import pickle

# Load the DataFrame and the model
# df_pickle_filename = 'df-2.pkl'
# model_pickle_filename = 'model.pkl'

# with open(df_pickle_filename, 'rb') as df_file:
#     df = pickle.load(df_file)

# with open(model_pickle_filename, 'rb') as model_file:
#     model = pickle.load(model_file)

df = pickle.load(open('df-2.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

# Function to predict hg/ha_yield
def predict_yield(area, item, year, rainfall, pesticides, temperature):
    input_data = pd.DataFrame({
        'Area': [area],
        'Item': [item],
        'Year': [year],
        'average_rain_fall_mm_per_year': [rainfall],
        'pesticides_tonnes': [pesticides],
        'avg_temp': [temperature]
    })
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.title("Crop Yield Prediction")

# User inputs
area = st.selectbox("Area", df['Area'].unique())
item = st.selectbox("Item", df['Item'].unique())
year = st.number_input("Year", min_value=int(df['Year'].min()), max_value=int(df['Year'].max()), value=int(df['Year'].mean()))
rainfall = st.number_input("Average Rainfall (mm/year)", value=float(df['average_rain_fall_mm_per_year'].mean()))
pesticides = st.number_input("Pesticides (tonnes)", value=float(df['pesticides_tonnes'].mean()))
temperature = st.number_input("Average Temperature (°C)", value=float(df['avg_temp'].mean()))

if st.button("Predict Yield"):
    yield_prediction = predict_yield(area, item, year, rainfall, pesticides, temperature)
    st.success(f"Predicted Yield: {yield_prediction:.2f} hg/ha")

if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(df)

