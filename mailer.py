import smtplib
import mailer_config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message):
    try:
        mailer = smtplib.SMTP('smtp.office365.com:587')
        mailer.ehlo()
        mailer.starttls()
        mailer.login(mailer_config.ADDRESS, mailer_config.PASSWORD)
        message = 'message{0}\n\n{1}'.format(subject, message)
        mailer.sendmail(mailer_config.ADDRESS, 'deli@lantmansmarket.com', message)
        mailer.quit()
        print("Success: Email sent!")
        pass
    except:
        print("Email failed to send!")
        pass
subject = "Test"
message = "Good Morning,\n\nId like to add the following 2 items to the order for the NRG System delivery if possible:\n\nSmall sub, wheat bread, ham, pepper jack cheese, Honey Mustard, for veggies everything except onions.\nSmall soup, any soup is fine.\n\n\nThank you and have a great day,\n-Jon"
subject = "test"
if __name__ == '__main__':
    send_email(subject, message)
