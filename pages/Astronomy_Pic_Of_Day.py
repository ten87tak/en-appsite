import streamlit as st
import requests

st.set_page_config(layout="wide")

# Sign up for NASA, get your own API key, and assign it to the variable.
api_key = "a5hHzb5AVOqRmaTjDiZY1bKxKsbeJewlR3ehzYDl"

url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

response_1 = requests.get(url)

content = response_1.json()

try:
    img_url = content["hdurl"]
    response_2 = requests.get(img_url)
    # print(response.content)

    with open("image.jpg", "wb") as file:
        file.write(response_2.content)

    st.title(content["title"])
    st.image("image.jpg", width=700)
    st.write(content["explanation"])

except KeyError:
    st.subheader("Get your own API key at NASA and assign it to the 'api_key' "
                 "variable! :)")

    st.subheader("And you'll see a new, incredible astronomic pic every day! "
                 "🌏🌞🌕")

