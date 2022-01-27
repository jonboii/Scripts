import smtplib
import config
def send_email(subject, message):
    try:
        mailer = smtplib.SMTP('smtp.office365.com:587')
        mailer.ehlo()
        mailer.starttls()
        mailer.login(config.ADDRESS, config.PASSWORD)
        message = 'subject{0}\n\n{1}'.format(subject, message)
        mailer.sendmail(config.ADDRESS, 'email@gmail.com', message)
        mailer.quit()
        print("Success: Email sent!")
        pass
    except:
        print("Email failed to send!")
        pass
subject = "test"
message = "test"
if __name__ == '__main__':
    send_email(subject, message)
