import streamlit as st

st.set_page_config(layout="wide")

column_1, column_2, column_3 = st.columns([5, 0.8, 5])

with column_1:
    st.title("GEOMETRY GAME")
    st.subheader("This is a CLI game where a player will be given random "
             "coordinates that make two points, which produces a rectangle.")
    st.write(
        "The player is then asked to type in a set of X and Y coordinates "
        "which they think is located within that rectangle. Also, the "
        "player will be asked to enter an area they guess. ")
    st.write("Finally, the program draws the rectangle and the guessed "
             "point in the graphic window.")

    st.write("")
    st.image("images/OOP_App1.PNG")
    st.write("[Source Code](https://github.com/ten87tak/OOP_App1_GeoGame)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.title("Happiness Data App")
    st.subheader("The app shows the relativity between GDP, happiness, and "
             "generosity:)")

    st.write("")
    st.write("")
    st.write("")
    st.image("images/happiness_app.PNG")
    st.write("[Source Code](https://github.com/ten87tak/New_Happiness_Data_App)")
    st.write("[Web App](https://ten87tak-new-happiness-data-app-main-7i0xd2.streamlit.app/)")


with column_3:
    st.title("Astronomy Image of the Day 🌏")
    st.subheader("Look into the 'Astronomy Pic Of Day' tab:) "
             "This is created with the NASA API.")

    st.write("")
    st.image("images/astro_pic.jpg")
    st.write("[Source Code](https://github.com/ten87tak/Astronomy_Today)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.title("Diary Tone")
    st.subheader("This program analyzes your mood out of text in your diary. 📓")

    st.write("")
    st.write("")
    st.write("")
    st.image("images/diary_tone.PNG")
    st.write("[Source Code](https://github.com/ten87tak/Visualizing_Moods_from_Diary)")


