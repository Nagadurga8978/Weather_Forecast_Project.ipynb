import streamlit as st
import pandas as pd
import pickle

# Load PKL file
with open("weather_dataset.pkl", "rb") as file:
    df = pickle.load(file)

st.title("🌦 Weather Forecast Application")

# Select city
city = st.selectbox("Select City", df["City"].unique())

# Filter data
city_data = df[df["City"] == city]

st.subheader("Weather Data")
st.write(city_data)

# Show average temperature
avg_temp = city_data["Temperature_C"].mean()
st.success(f"Average Temperature in {city}: {avg_temp:.2f} °C")

# Plot temperature graph
st.line_chart(city_data["Temperature_C"])