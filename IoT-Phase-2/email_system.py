import smtplib
import imaplib
import email
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from email.utils import formatdate

# #Current
# current_datetime = datetime.now()
# formatted_current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted current:", formatted_current_datetime)
#
# #Email Time
# # Given string
# given_datetime_str = "Sun, 22 Apr 2024 14:24:39 -0400"
# # Parse the string into a datetime object
# given_datetime = datetime.strptime(given_datetime_str, "%a, %d %b %Y %H:%M:%S %z")
# # Format the datetime object
# formatted_email_datetime = given_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted datetime:", formatted_email_datetime)
#
# if  formatted_current_datetime < formatted_email_datetime:
#     print("email big")


subject = "Turn fan on"
sender = "arshsinghalt@gmail.com"
recipient = "arshmain24@gmail.com"
password = "kbzx epve kvim erhm"
emailStatus = False
receiveStatus = False
json_file_path = "/home/arsh/Documents/IoT-Projects/IoT-Phase-2/current_date.json"

def send_email(temperature):
    global sender, password, recipient, subject, emailStatus, json_file_path
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    body = f'The current temperature is {temperature}. Would you like to turn on the fan?'
    msg.attach(MIMEText(body, 'plain'))

    try:
        if emailStatus:
            raise Exception("Email has already been sent.")
        elif temperature > 22 and not emailStatus:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            text = msg.as_string()
            emailStatus = True
            server.sendmail(sender, recipient, text)

            # Get current datetime
            current_datetime = formatdate(localtime=True)
            given_datetime = datetime.strptime(current_datetime, "%a, %d %b %Y %H:%M:%S %z")
            # Format the datetime object
            formatted_email_datetime = given_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print("Formatted datetime:", formatted_email_datetime)
            # Save current datetime to JSON file
            data = {
                'current_datetime': formatted_email_datetime
            }

            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

            server.quit()
            return "Email sent successfully!"
    except Exception as e:
        return "Error sending email:", str(e)


# send = send_email(24)
# print(send)
# send_email(24)

def receive_email():
    global sender, password, recipient, receiveStatus, json_file_path
    print(receiveStatus)
    if receiveStatus:
        return receiveStatus
    body = ''
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(sender, password)
        mail.select("inbox")

        # Search for unseen or unread emails only
        result, data = mail.search(None, "UNSEEN", "FROM", recipient)

        # If there are no unseen emails, return False
        if not data[0]:
            return False

        ids = data[0]
        id_list = ids.split()

        # Fetch the first unseen email
        first_email_id = id_list[0]

        result, data = mail.fetch(first_email_id, "(RFC822)")
        raw_email = data[0][1]

        email_message = email.message_from_bytes(raw_email)
        print("Subject:", email_message['Subject'])
        print("From:", email_message['From'])
        print("Date:", email_message['Date'])

        # Parse the string into a datetime object
        email_datetime = datetime.strptime(email_message['Date'], "%a, %d %b %Y %H:%M:%S %z")

        # Format the datetime object
        formatted_email_datetime = email_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print("Formatted datetime:", formatted_email_datetime)

        # Reading data from the JSON file
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        # Extracting only the 'name' field
        current_datetime = data["current_datetime"]
        print("Formatted current datetime:", current_datetime)
        print(current_datetime > formatted_email_datetime)

        if current_datetime > formatted_email_datetime:
            print("Replied to an Email")
            return False

        print("Body:")
        for part in email_message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if "text/plain" in content_type:
                body = part.get_payload(decode=True)
                # Use 'a' mode for appending instead of 'w'
                # with open("/home/arsh/Documents/IoT-Projects/IoT-Phase-2/test.txt", 'a') as file:
                #     file.write(body.decode('utf-8') + '\n')  # Add a newline after each write
                lowercase_body = body.decode('utf-8').lower()
                print(lowercase_body)
                if 'yes' in lowercase_body:
                    receiveStatus = True
                    # mail.store(first_email_id, '+FLAGS', '\\Seen')
                    mail.store(first_email_id, '+FLAGS', '\\Deleted')
                else:
                    receiveStatus = False
        mail.close()
        mail.logout()
        return receiveStatus
    except Exception as e:
        receiveStatus = False
        return "Error receiving email:", str(e)



# Usage: Replace 'sender', 'password', and 'recipient' with your Gmail credentials
# r = receive_email()
# print(r)
