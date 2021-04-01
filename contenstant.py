import fp as fp
import gmail as gmail

from sweepstakes import NotaWinnerMessage
from sweepstakes import WinnerMessage
import smtplib

from email import EmailMessage


class Contestant:

    def __init__(self, name, email, registration_number):
        self.first_name = name
        self.last_name = name
        self.email = email
        self.registration_number = ()

    def notify_winner(self, message):
        print(f'{self.name} got message {WinnerMessage}')

    def notify_losers(self, message):
        print(f'{self.name} got message {NotaWinnerMessage}')


msg = EmailMessage()
msg.set_content(fp.read())

msg['Subject'] = f'You won!'
msg['From'] = rmck6701@gmail.com
msg['To'] = rmck6701@gmail.com

s = smtplib.SMTPs.send_message(msg)
s.quit()
