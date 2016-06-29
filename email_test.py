#!/usr/bin/env python
# Module:   email_test.py
# Purpose:  send e-mail from Python
# Date:     N/A
# Notes:
# 1) This uses SMTPLIB to send e-mail.  It requires a
#    computer running sendmail and a valid E-MAIL account.
#    The default account is blank -- fill it in.
#
# Ref:  https://docs.python.org/2/library/smtplib.html
#
"""This uses SMTPLIB to send a test e-mail -- fix RECEIVERS below"""
import smtplib

SENDER = 'from@fromdomain.com'
RECEIVERS = ['junk@gmail.com']

def email_test():
    """Send test e-mail message"""
    message = """From: From Person <from@fromdomain.com>
To: To Person <araasch@gmail.com>
Subject: SMTP e-mail test
    
This is a test e-mail message.
    """

    try:
        smtp_obj = smtplib.SMTP('localhost')
        smtp_obj.sendmail(SENDER, RECEIVERS, message)
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"

if __name__ == "__main__":
    email_test()
