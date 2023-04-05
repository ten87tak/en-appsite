import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # This is an environment variable. Enter your email address here.
    username = "EMAIL"

    # This is an environment variable. Create an app password and type it in here.
    password = "PASSWORD"

    # This is an environment variable. Enter your email address here.
    receiver = "EMAIL"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

