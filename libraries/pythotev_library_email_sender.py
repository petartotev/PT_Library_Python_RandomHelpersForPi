import smtplib
import email.message
import imghdr

somethingWentWrong = "Something went wrong while "

def set_message(subject, content, receiverEmail):
    try:
        msg = email.message.EmailMessage()
        msg.set_content(content)
        msg['Subject'] = subject
        msg['To'] = receiverEmail
        return msg
    except:
        print(somethingWentWrong + "setting the message.")
    
def attach_csv_file_to_message(msg, filePath):
    try:
        fileData = open(filePath, 'rb').read()
        msg.add_attachment(fileData, maintype='image', subtype=imghdr.what(None, fileData))
    except:
        print(somethingWentWrong + "attaching the image.")
    
def send_email(msg, senderGmail, passwordGmail):
    try:
        msg['From'] = senderGmail
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(senderGmail, passwordGmail)
        session.send_message(msg)
        session.quit()
        print("Message successfully sent!")
    except:
        print(somethingWentWrong + "sending the email.")