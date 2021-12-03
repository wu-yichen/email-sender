import smtplib
from pathlib import Path
from string import Template
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'what?'
email['to'] = '@gmail.com'
email['subject'] = 'love letter'

html = Template(Path('index.html').read_text())
email.set_content(html.substitute({'name': ''}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('@gmail.com', '')
    smtp.send_message(email)
