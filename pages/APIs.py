import streamlit as st

st.set_page_config(layout="wide")

column_1, column_2, column_3 = st.columns([5, 1, 6])

with column_1:
    st.title("Dictionary API")
    st.subheader("Run it in your terminal. Copy and paste the format in the "
                 "URL address bar, type in a word you like in place of 'word', "
                 "and then you get the word and its definition in a dictionary! :)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.title("Weather API")
    st.subheader("(Also introduced in the Home tab)")
    st.subheader("Run it in your terminal. Copy and paste one of the three "
                 "formats in the address bar of your browser. Type in a "
                 "Station ID, and then you get the weather data 🌞⛅☔ :)")
    st.write("")
    st.write("[Source Code](https://github.com/ten87tak/Weather_API)")


with column_3:
    st.write("")
    st.write("")
    st.write("")
    st.image("images/dict_api_urlbar.PNG")
    st.image("images/dict_api.PNG")

    st.write("[Source Code](https://github.com/ten87tak/Dictionary_API)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.image("images/weather_api_home.PNG")
