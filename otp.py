import smtplib
import random
import math

def generate_otp():
    digits = "0123456789"
    otp = ""
    for i in range(6):
        otp += digits[math.floor(random.random() * 10)]
    return otp

def send_email(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_generated_app_password")
    message = f"Subject: OTP Verification\n\nYour OTP is: {otp}"
    server.sendmail("your_email@gmail.com", email, message)
    server.quit()

email = "rosasjohnson10@gmail.com"
otp = generate_otp()
send_email(email, otp)