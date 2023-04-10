import streamlit as st
import requests


api_key = "a5hHzb5AVOqRmaTjDiZY1bKxKsbeJewlR3ehzYDl"

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
st.image("image.jpg")
st.write(content["explanation"])

