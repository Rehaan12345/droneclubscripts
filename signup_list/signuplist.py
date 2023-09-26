import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from email.message import EmailMessage
import ssl

# df = pd.read_excel("sign_up_list.xlsx", usecols="c")

# df.to_csv("emails.csv", index=False)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

# Define email sender and receiver
email_sender = '25ranjaria@cpsd.us'
email_password = 'ojhyndncintdqecx'
email_receiver = 'rehaan1099@gmail.com'

# Set the subject and body of the email
subject = 'Welcome to Drone Club!'
body = """Hello Everyone!

Thank you for signing up to Drone Club today during your lunches! We are excited to have you all, as this is the first year of Drone Club.
If you haven't already, please follow this link to join our Google Classroom: https://classroom.google.com/c/NjIzODYzMzU3OTIw?cjc=3usnqjj

Our first day will be Wednesday, October 4th in the field house at 7:30 AM. There will be donuts and munchkins!

Thank you, and see you then,
Rehaan, Abel, Daniel

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())