import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ইমেল কনফিগারেশন
sender_email = os.environ.get("SENDER_EMAIL")
sender_password = os.environ.get("MAIL_SERVER_PASSWORD")

# জিমেইল সার্ভার বা আপনার কোম্পানির SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587

# যাদের কাছে মেইল পাঠাবেন তাদের লিস্ট
recipient_emails = ["recipient@example.com"]

# ইমেল কন্টেন্ট (আপনার স্টোরের প্রমোশন)
subject = "Special Offer from Our Store!"
body = """
হ্যালো,
আমাদের স্টোরের নতুন কালেকশন এবং অফার দেখতে ভিজিট করুন।
ধন্যবাদ!
"""

# মেইল কম্পোজ করে পাঠানো
for receiver_email in recipient_emails:
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
