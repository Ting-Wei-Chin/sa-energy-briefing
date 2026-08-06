import urllib.request
import urllib.error
import json
import os
from datetime import datetime

with open("briefing.txt", "r", encoding="utf-8") as f:
    content = f.read()

today = datetime.now().strftime("%d %B %Y")
api_key = os.environ["RESEND_API_KEY"]

payload = json.dumps({
    "from": "SA Energy Briefing <onboarding@resend.dev>",
    "to": ["jordan.chin@southenergy.com.au"],
    "subject": "SA Energy Daily Briefing - " + today,
    "text": content
}).encode("utf-8")

req = urllib.request.Request(
    "https://api.resend.com/emails",
    data=payload,
    headers={
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
)

try:
    with urllib.request.urlopen(req) as response:
        print("Email sent: " + response.read().decode())
except urllib.error.HTTPError as e:
    print("Failed: " + str(e.code) + " " + e.read().decode())
    exit(1)
except Exception as e:
    print("Failed: " + str(e))
    exit(1)
