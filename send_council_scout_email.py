import smtplib
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

with open("council-scout.txt", "r", encoding="utf-8") as f:
    content = f.read()

today = datetime.now().strftime("%d %B %Y")
gmail_user = "jordan20130315@gmail.com"
app_password = os.environ["GMAIL_APP_PASSWORD"]

council_match = re.search(r"^Council:\s*(.+)$", content, re.MULTILINE)
council_name = council_match.group(1).strip() if council_match else "Unknown"

msg = MIMEMultipart()
msg["Subject"] = f"Council Scout: {council_name} — {today}"
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
