import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# গিটহাব সিক্রেট থেকে সেন্ডার ইনফো নেওয়া
sender_email = os.environ.get("SENDER_EMAIL")
sender_password = os.environ.get("MAIL_SERVER_PASSWORD")

# গিটহাব ফর্ম (Workflow Input) থেকে ডাটাগুলো রিসিভ করা
raw_recipients = os.environ.get(
    "INPUT_RECIPIENTS", "customer1@example.com"
)
subject = os.environ.get("INPUT_SUBJECT", "Default Subject")
body = os.environ.get("INPUT_BODY", "Default Body")

# কমা দিয়ে আলাদা করা ইমেলগুলোকে লিস্টে রূপান্তর করা
recipient_emails = [email.strip() for email in raw_recipients.split(",")]

# SMTP সার্ভার কনফিগারেশন
smtp_server = "smtp.gmail.com"
smtp_port = 587

# লूप চালিয়ে একে একে সবার কাছে মেইল পাঠানো
for receiver_email in recipient_emails:
  if not receiver_email:
    continue
  try:
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

    print(f"Successfully sent email to {receiver_email}")
  except Exception as e:
    print(f"Failed to send email to {receiver_email}: {e}")
