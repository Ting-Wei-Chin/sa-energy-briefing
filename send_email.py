import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

with open("briefing.txt", "r", encoding="utf-8") as f:
    content = f.read()

today = datetime.now().strftime("%d %B %Y")
gmail_user = "jordan20130315@gmail.com"
app_password = os.environ["GMAIL_APP_PASSWORD"]

msg = MIMEMultipart()
msg["Subject"] = "SA Energy Daily Briefing - " + today
msg["From"] = gmail_user
msg["To"] = "jordan.chin@southenergy.com.au"
msg.attach(MIMEText(content, "plain", "utf-8"))

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(gmail_user, app_password)
        server.sendmail(gmail_user, "jordan.chin@southenergy.com.au", msg.as_string())
        print("Email sent successfully")
except Exception as e:
    print("Failed: " + str(e))
    exit(1)
