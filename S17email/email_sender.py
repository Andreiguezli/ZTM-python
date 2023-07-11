import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("S17email/index.html").read_text())
email = EmailMessage()
email["from"] = "Andre Pedroso"
email["to"] = "andreiguezli@gmail.com"
email["subject"] = "This is a test!"

email.set_content(html.substitute({"name": "Tom"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sendertest25@gmail.com", "gudwaxezvbklzqgs")
    smtp.send_message(email)
    print("finished!")
