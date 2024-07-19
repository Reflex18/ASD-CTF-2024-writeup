import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from datetime import datetime, timedelta

# SMTP server configuration
smtp_server = 'futuremail.ctfchallenges.net'
smtp_port = 465
smtp_username = 'seaton@futuremail.ctfchallenges.net'
smtp_password = 'R]Xea4Le"=3GGv91'

# Email content
from_email = 'seaton@futuremail.ctfchallenges.net'
to_email = 'flag@futuremail.ctfchallenges.net'
subject = 'Email from the Future'
body = 'This is a test email.'

# Create a future date
future_date = datetime.now() + timedelta(days=7)
formatted_date = formatdate(future_date.timestamp())

# Create the MIMEText object
msg = MIMEText(body)
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg['Date'] = formatted_date

# Send the email
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, msg.as_string())
