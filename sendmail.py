from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from accountinfo import username, password


def send(recipients, subject, message):

    emails = ",".join([email for email in recipients.values()])

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username, password)

        # for name, email in recipients.items():
        #     edited_subject = subject.replace("<>", name)
        #     edited_message = message.replace("<>", name)

        mail = MIMEMultipart()
        mail['from'] = 'Tomas W'
        mail['to'] = emails
        mail['subject'] = subject
        mail.attach(MIMEText(message, "plain"))
        smtp.send_message(mail)
