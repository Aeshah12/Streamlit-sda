from textwrap import fill
import pickle
import requests
import json
import streamlit as st
import pandas as pd


html_temp = """
<div >
<h2 style="color:black;text-align:center;font-family: Arial">Welcome to my Car Price Prediction Application</h2>
</div>"""

image = st.image('https://imgd.aeplcdn.com/664x374/n/cw/ec/54399/swift-exterior-right-front-three-quarter-64.jpeg?isig=0&q=80', use_column_width=True)
st.markdown(html_temp,unsafe_allow_html=True)
st.write("\n")

st.sidebar.write("<h2 style='color: red;'text-align:center;font-family: Arial>To help us estimate the price of your car, please enter the following information:</h2>",unsafe_allow_html=True)

car_model=st.sidebar.selectbox("Select the Car Model ", ('Audi A1', 'Audi A2', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))
age=st.sidebar.selectbox("What is the age of the car:",(0,1,2,3))
gears=st.sidebar.selectbox("How many gears in the car?",(5,6,7,8))
hp=st.sidebar.slider("What is the hp_kw of the car?", 40, 294, step=5)
km=st.sidebar.slider("What is the km of the car", 0,317000, step=1000)
st.write("")

my_dict = {
    "age": age,
    "hp_kW": hp,
    "km": km,
    'Gears':gears,
    "make_model": car_model
    
}

df = pd.DataFrame.from_dict([my_dict])

st.write("<h5 style='padding-right: 20px;color: gray;text-align:center;font-family: Arial;'>The configuration of your car is below</h2>",unsafe_allow_html=True)
st.write("")
#st.header("The configuration of your car is below")
st.table(df.style.set_properties(**{'font-size': '16px', 'text-align': 'center'}).\
    set_table_styles([{'selector': 'thead', 'props': 'background-color: #b8a39e; color: white;'},
                     {'selector': 'tbody', 'props': 'background-color: #f2f2f2;'},
                     {'selector': 'td', 'props': 'padding: 10px;'}]))

# To load machine learning model
import pickle
filename = "Final_model"
model = pickle.load(open(filename, "rb"))


# Prediction with user inputs
predict = st.button("Click to Predict")
result = model.predict(df)
if predict :
    st.success("The estimated price of your car is {} ".format(int(result[0])))
