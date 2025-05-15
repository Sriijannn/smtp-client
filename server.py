import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
print("This is the SMTP Service")
# Gmail credentials
FROM_EMAIL = "<Email>"
APP_PASSWORD = "<App Password>"


SUBJECT = "I wonder if I can work for you."
COMMON_BODY = """
Hi there,
I am Srijan Tripathi, a software developer based in India
"""

def send_email(to_email, greeting):
    full_body = f"{greeting}\n\n{COMMON_BODY}"

    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(full_body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(FROM_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {to_email}")
        return "Sent"
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")
        return "Failed"


df = pd.read_csv("emails.csv")
if 'Status' not in df.columns:
    df['Status'] = ""
for index, row in df.iterrows():
    if df.at[index, 'Status'] != "Sent":  
        status = send_email(row['Email'], row['Greeting'])
        df.at[index, 'Status'] = status
df.to_csv("emails.csv", index=False)
print("✅ Updated CSV with email statuses.")
