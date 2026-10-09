import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ইমেল কনফিগারেশন (গিটহাব সিক্রেট থেকে ভ্যালুগুলো রিড করবে)
sender_email = os.environ.get("SENDER_EMAIL")
sender_password = os.environ.get("MAIL_SERVER_PASSWORD")

# SMTP সার্ভার সেটিংস (জিমেইলের ক্ষেত্রে এটি অপরিবর্তিত থাকবে)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# যাদের কাছে মেইল পাঠাবেন তাদের ইমেল লিস্ট (এখানে আপনার কাস্টমারদের ইমেলগুলো বসাবেন)
recipient_emails = [
    "customer1@example.com",
    "customer2@example.com",
    # আরও ইমেল লাগলে কমা দিয়ে এখানে যোগ করতে পারেন
]

# ইমেল সাবজেক্ট বা বিষয়
subject = "আপনার কোম্পানির স্টোর প্রমোশন ও স্পেশাল অফার!"

# ইমেল বডি বা মূল কন্টেন্ট (এখানে আপনার প্রচারণামূলক লেখা লিখবেন)
body = """
আসসালামু আলাইকুম / হ্যালো,

আমাদের স্টোরের নতুন কালেকশন এবং দারুণ সব অফার এখন লাইভ! 
আপনার পছন্দের পণ্যটি লুফে নিতে আজই ভিজিট করুন আমাদের স্টোরে।

ধন্যবাদান্তে,
আপনার কোম্পানি
"""

# লুপ চালিয়ে একে একে সবার কাছে মেইল পাঠানো
for receiver_email in recipient_emails:
  try:
    # মেইল অবজেক্ট তৈরি
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # বডি যুক্ত করা
    message.attach(MIMEText(body, "plain"))

    # সার্ভারের সাথে কানেক্ট করে মেইল শুট করা
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

    print(f"Successfully sent email to {receiver_email}")
  except Exception as e:
    print(f"Failed to send email to {receiver_email}: {e}")
