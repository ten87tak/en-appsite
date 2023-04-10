import streamlit as st

st.set_page_config(layout="wide")

column_1, column_2, column_3 = st.columns([5, 1, 6])

with column_1:
    st.header("GEOMETRY GAME")
    st.write("This is a CLI game where a player will be given random "
             "coordinates that make two points, which produces a rectangle.")
    st.write(
        "The player is then asked to type in a set of X and Y coordinates "
        "which they think is located within that rectangle. Also, the "
        "player will be asked to enter an area they guess. ")
    st.write("Finally, the program draws the rectangle and the guessed "
             "point in the graphic window.")

    st.write("")
    st.write("")
    st.write("")

    st.write("[Source Code](https://github.com/ten87tak/OOP_App1_GeoGame)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.image("images/astro_pic.jpg")

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.header("Astronomy Image of the Day 🌏")


with column_3:
    st.write("")
    st.image("images/OOP_App1.PNG")

    st.write("")
    st.write("")
    st.write("")

    st.header("Astronomy Image of the Day 🌏")
    st.write("You can check out the astronomy picture of the day. "
             "This is created with the NASA API.")

    st.write("")
    st.write("")

    st.write("[Source Code](https://github.com/ten87tak/Astronomy_Today)")
