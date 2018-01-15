# -*- coding: utf-8 -*-

def task():
    from gluon.tools import Mail
    mail = Mail()
    mail.settings.server = 'smtp.gmail.com:587'
    mail.settings.sender = 'weslylim94@gmail.com'
    mail.settings.login = 'weslylim94@gmail.com:edvrygzm'
    s = "weslylim94@gmail.com"              #T-Mobile
    from gluon.contrib.sms_utils import SMSCODES, sms_email
    if mail.send(to='1415658-1151@tmomail.net',
        subject='Reminders:',
        message= 'test'):
        response.flash = mail.result
    else:
        response.flash = mail.error
    h = 'hello'
    return locals()

from gluon.scheduler import Scheduler
Scheduler(db, tasks = dict(task = task))
