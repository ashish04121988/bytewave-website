import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

TO_EMAILS = ["bytewavedigi@gmail.com", "ashish.0412@gmail.com"]

def send_enquiry_email(name, email, company, phone, requirement, message):
    # Try Render environment variables first, fall back to Streamlit secrets (local dev)
    sender = os.environ.get("EMAIL_SENDER")
    password = os.environ.get("EMAIL_PASSWORD")
    if not sender or not password:
        try:
            sender = st.secrets["email"]["sender"]
            password = st.secrets["email"]["password"]
        except Exception:
            return False, "email_not_configured"

    subject = f"New Enquiry from {name} — Bytewave Digital Website"

    body = f"""
<html>
<body style="font-family: Arial, sans-serif; background:#f4f4f4; padding:0; margin:0;">
  <div style="max-width:600px; margin:30px auto; background:white; border-radius:12px; overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,0.1);">
    <div style="background:linear-gradient(135deg,#2563EB,#7C3AED); padding:28px 32px;">
      <h2 style="color:white; margin:0; font-size:22px;">⚡ New Website Enquiry</h2>
      <p style="color:rgba(255,255,255,0.8); margin:6px 0 0; font-size:14px;">Bytewave Digital — bytewavedigital.com</p>
    </div>
    <div style="padding:32px;">
      <table style="width:100%; border-collapse:collapse;">
        <tr>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:13px; color:#6b7280; width:130px; font-weight:600;">Name</td>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:14px; color:#111827;">{name}</td>
        </tr>
        <tr>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:13px; color:#6b7280; font-weight:600;">Email</td>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:14px; color:#111827;">{email}</td>
        </tr>
        <tr>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:13px; color:#6b7280; font-weight:600;">Company</td>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:14px; color:#111827;">{company}</td>
        </tr>
        <tr>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:13px; color:#6b7280; font-weight:600;">Phone</td>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:14px; color:#111827;">{phone or "Not provided"}</td>
        </tr>
        <tr>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:13px; color:#6b7280; font-weight:600;">Interested In</td>
          <td style="padding:10px 0; border-bottom:1px solid #f0f0f0; font-size:14px; color:#111827;">{requirement}</td>
        </tr>
      </table>
      <div style="margin-top:24px;">
        <div style="font-size:13px; color:#6b7280; font-weight:600; margin-bottom:8px;">Message</div>
        <div style="background:#f9fafb; border-radius:8px; padding:16px; font-size:14px; color:#374151; line-height:1.6;">{message}</div>
      </div>
    </div>
    <div style="background:#f9fafb; padding:20px 32px; text-align:center;">
      <p style="font-size:12px; color:#9ca3af; margin:0;">This enquiry was submitted via bytewavedigital.com</p>
    </div>
  </div>
</body>
</html>
"""

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = ", ".join(TO_EMAILS)
        msg["Reply-To"] = email
        msg.attach(MIMEText(body, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, TO_EMAILS, msg.as_string())

        return True, "sent"
    except Exception as e:
        return False, str(e)
