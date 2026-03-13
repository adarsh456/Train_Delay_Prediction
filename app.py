import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("train_delay_model.pkl","rb"))

st.title("🚆 Train Delay Prediction System")

distance = st.number_input("Distance Between Stations (km)")
weather = st.selectbox("Weather Conditions", ["Clear","Rainy","Foggy","Snowy"])
day = st.selectbox("Day of Week", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
time = st.selectbox("Time of Day", ["Morning","Afternoon","Evening","Night"])
train_type = st.selectbox("Train Type", ["Passenger","Express","Freight"])
delay = st.number_input("Historical Delay (min)")
congestion = st.selectbox("Route Congestion", ["No","Yes"])

weather_map = {'Clear':0,'Rainy':1,'Foggy':2,'Snowy':3}
day_map = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
time_map = {'Morning':0,'Afternoon':1,'Evening':2,'Night':3}
train_type_map = {'Passenger':0,'Express':1,'Freight':2}
congestion_map = {'No':0,'Yes':1}

if st.button("Predict"):

    data = pd.DataFrame([{
        'Distance Between Stations (km)': distance,
        'Weather Conditions': weather_map[weather],
        'Day of the Week': day_map[day],
        'Time of Day': time_map[time],
        'Train Type': train_type_map[train_type],
        'Delay (min)': delay,
        'Route Congestion': congestion_map[congestion]
    }])

    prediction = model.predict(data)

    label_map = {
        0:"On Time",
        1:"Slight Delay",
        2:"Heavy Delay"
    }

    st.success("Prediction: " + label_map[prediction[0]])