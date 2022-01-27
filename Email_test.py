import smtplib
import pylint

def send_email():
    try:
        subject = test
        msg = test
        mailer = smtplib.SMTP('smtp.office365.com:587')
        mailer.ehlo()
        mailer.starttls()
        mailer.login('email@email.com', 'pass')
        message = 'subject{0}\r\n{1}\r\n'.format(subject, msg)
        mailer.sendmail('email@email.com', 'email@gmail.com', message)
        mailer.quit()
        print("Success: Email sent!")
        subject = test
        msg = test
        pass
    except:
        print("Something went wrong!")
        pass
    finally:
        print("Success: Email sent!")
        if __name__ == '__main__':
            send_email()
