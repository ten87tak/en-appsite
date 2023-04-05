import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="form"):
    email_address = st.text_input("Please enter your email address:")

    raw_message = st.text_area("Your message:")
    message = f"""\
    Subject: New email from {email_address}
    
    From: {email_address}
    {raw_message}
    """

    submit_button = st.form_submit_button("Submit")
    print(submit_button)

    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully.")

    st.write("If you have an error after pressing on the Submit button, "
             "please directly send your message to ten87tak@gmail.com from "
             "your email client.")