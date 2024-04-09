import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Turn fan on"
sender = "arshsinghalt@gmail.com"
recipient = "arshmain24@gmail.com"
password = "kbzx epve kvim erhm"
emailStatus = False
receiveStatus = False

def send_email(temperature):
    global sender, password, recipient, subject, emailStatus
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    body = f'The current temperature is {temperature}. Would you like to turn on the fan?'
    msg.attach(MIMEText(body, 'plain'))

    try:
        if emailStatus:
            raise Exception("Email has already been sent.")
        elif temperature > 23 and not emailStatus:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            text = msg.as_string()
            emailStatus = True
            server.sendmail(sender, recipient, text)
            server.quit()
            return "Email sent successfully!"
    except Exception as e:
        return "Error sending email:", str(e)

# send = send_email(24)
# print(send)
# send_email(24)

def receive_email():
    global sender, password, recipient, receiveStatus
    body = ''
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(sender, password)
        mail.select("inbox")

        result, data = mail.search(None, "FROM", recipient)
        ids = data[0]
        id_list = ids.split()

        latest_email_id = id_list[-1]

        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]

        email_message = email.message_from_bytes(raw_email)
        print("Subject:", email_message['Subject'])
        print("From:", email_message['From'])
        print("Body:")
        for part in email_message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if "text/plain" in content_type:
                body = part.get_payload(decode=True)
                # print(body.decode('utf-8'))
                if 'yes' in body.decode('utf-8'):
                    receiveStatus = True
                else:
                    receiveStatus = False
                return receiveStatus
        mail.close()
        mail.logout()
    except Exception as e:
        receiveStatus = False
        return "Error receiving email:", str(e)

# Usage: Replace 'sender', 'password', and 'recipient' with your Gmail credentials
# r = receive_email()
# print(r)
