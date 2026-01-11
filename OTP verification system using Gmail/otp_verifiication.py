import smtplib
import random
import ssl

# -------- EMAIL DETAILS --------
sender_email = "your_email@gmail.com" # Enter your email
app_password = "your_app_password"    # Enter your app password
receiver_email = input("Enter your Gmail: ")

# -------- OTP GENERATION --------
otp = random.randint(100000, 999999)

# -------- EMAIL MESSAGE --------
message = f"""
Subject: OTP Verification

Your OTP is: {otp}

Do not share this OTP with anyone.
"""

# -------- SEND EMAIL --------
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message)
        print("✅ OTP sent successfully to your email")

except Exception as e:
    print("❌ Error sending email:", e)
    exit()

# -------- OTP VERIFICATION --------
user_otp = input("Enter the OTP received: ")

if user_otp == str(otp):
    print("🎉 OTP Verified Successfully")
else:
    print("❌ Invalid OTP")
