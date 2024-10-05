import time 
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def picture(subject):
    if subject=="Birthday":
        attachment_path = "C:\\Users\\SATHISH K\\Documents\\sem2\\samplepython\\templates\\birthday.png"
    else:
        attachment_path = "C:\\Users\\SATHISH K\\Documents\\sem2\\Pytproject\\templates\\Designer.png"
    return attachment_path

def send_email(message, recipient_email, subject, body, attachment_path):

    sender_email = "sathishksv2003@gmail.com"
    
    recipient_email=str(recipient_email)
    subject =str(subject)
    message =str(message)

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
            msg.attach(part)

        # Set up the SMTP server
        smtp_username = "sathishksv2003@gmail.com"


        # Connect to the server and send the email
        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            server.login(smtp_username,"zczdmmddvfslrihe")
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("email send succesfully")
    except:
        print("Unable to send!")

def ctb():
    f=open("member.txt",'r')
    today = time.strftime('%m%d')
    flag =0
    for line in f:
        if today in line:
            line = line.split(' ')
            flag=1
            message="hello"
            subject=line[1]
            recipient_email =line[3]
            attachment_path=picture(subject)
            body = "Happy "+line[1].strip()+" my dear "+line[2].strip()+"  I wish you all the very best on this special day. May you be blessed today, tomorrow, and in the upcoming days to come. May you have a wonderful birthday and many more to come. " "\n Greated By \n\n\n "+line[4].strip()
            
            send_email(message, recipient_email, subject, body, attachment_path)
    if flag ==0:
        print("no_events")
        message=None
    return message


     

schedule_time="12:07"
schedule.every().day.at(schedule_time).do(ctb)


if __name__ == "__main__":
   while True:
    schedule.run_pending()
    time.sleep(2)

