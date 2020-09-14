#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from depuydt import echo

import smtplib

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

class SMTP():

    user = ''
    password = ''
    server = ''
    port = 0

    @staticmethod
    def set_login(user: str, password: str):
        SMTP.user = user
        SMTP.password = password

    @staticmethod
    def set_server(server: str, port: int):
        SMTP.server = server
        SMTP.port = port

    def __init__(self, sender: str, recipients):
        self.sender = sender
        try:
            assert isinstance(recipients, list)            
            self.recipients = recipients
        except AssertionError:
            assert isinstance(recipients, str)
            self.recipients = [recipients]
            echo.warning("Recipients is a string")

    def send(self, subject: str, content: str):   
        message = MIMEMultipart()
        message['From'] = SMTP.user
        message['To'] = self.sender
        message['Date'] = formatdate(localtime=True)    
        message['Subject'] = subject
        message.attach(MIMEText(content))

        try:
            mailobj = smtplib.SMTP(SMTP.server, SMTP.port)
            mailobj.ehlo()
            mailobj.starttls()
            mailobj.login(SMTP.user, SMTP.password)
            mailobj.sendmail(self.sender, self.recipients, message.as_string())
            mailobj.quit()
            echo.debug("Successfully sent email")
        except Exception as e:
            echo.error("Error: unable to send email: " + str(e) )
        
        
    
        



