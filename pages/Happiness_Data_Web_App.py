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


match x_choice:
    case "GDP":
        x_axis = df["gdp"]

    case "Happiness":
        x_axis = df["happiness"]

    case "Generosity":
        x_axis = df["generosity"]


match y_choice:
    case "GDP":
        y_axis = df["gdp"]

    case "Happiness":
        y_axis = df["happiness"]

    case "Generosity":
        y_axis = df["generosity"]


figure = px.scatter(x=x_axis, y=y_axis, labels={"x": x_choice, "y": y_choice})
st.plotly_chart(figure)


