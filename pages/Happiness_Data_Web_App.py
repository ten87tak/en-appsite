import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")

st.write("")
x_choice = st.selectbox("Select the data for the X-axis:",
                      ("GDP", "Happiness", "Generosity"))

st.write("")
y_choice = st.selectbox("Select the data for the Y-axis:",
                      ("GDP", "Happiness", "Generosity"))

st.write("")
st.subheader(f"{x_choice} and {y_choice}")


if x_choice == "GDP":
    x_axis = df["gdp"]

elif x_choice == "Happiness":
    x_axis = df["happiness"]

elif x_choice == "Generosity":
    x_axis = df["generosity"]


if y_choice == "GDP":
    y_axis = df["gdp"]

elif y_choice == "Happiness":
    y_axis = df["happiness"]

elif y_choice == "Generosity":
    y_axis = df["generosity"]


figure = px.scatter(x=x_axis, y=y_axis, labels={"x": x_choice, "y": y_choice})
st.plotly_chart(figure)


