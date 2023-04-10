import streamlit as st
import requests


# Sign up for NASA, get your own API key, and assign it to the variable.
api_key = "NASA_API"

url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

response_1 = requests.get(url)

content = response_1.json()

img_url = content["hdurl"]
response_2 = requests.get(img_url)
# print(response.content)

with open("image.jpg", "wb") as file:
    file.write(response_2.content)


st.title(content["title"])
st.image("image.jpg", width=700)
st.write(content["explanation"])

