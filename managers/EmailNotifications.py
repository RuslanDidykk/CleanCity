import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import my_mail, my_password

class EmailNotifications():

    def sendUserRegistered(self, user_mail, login, password):
        try:
            content = 'You was registered: \n login: '+login+'\n password: '+password

            msg = MIMEMultipart()
            msg['From'] = my_mail
            msg['To'] = user_mail
            msg['Subject'] = 'Registration'

            msg.attach(MIMEText(content,'plain'))
            text = msg.as_string()

            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(my_mail, my_password)

            mail.sendmail(my_mail, user_mail, text)

            mail.close()
        except Exception as exc:
            print(exc)
            return exc

if __name__ == '__main__':
    obj = EmailNotifications()
    obj.sendUserRegistered('ruslanpk3@gmail.com','123','32123')


