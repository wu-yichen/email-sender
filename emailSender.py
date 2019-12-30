import smtplib
from pathlib import Path
from string import Template
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'yichen'
email['to'] = 'takehisa1900@gmail.com'
email['subject'] = 'love letter'

html = Template(Path('index.html').read_text())
email.set_content(html.substitute({'name': 'zexi'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('wuyichen1987@gmail.com', 'Wyc8430507208')
    smtp.send_message(email)
