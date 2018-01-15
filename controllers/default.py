# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------



# import time
import _ssl
@auth.requires_login()
def index():
    reminder = db(db.Reminders).select(db.Reminders.ALL)
    text = db(db.Texts).select(db.Texts.ALL)
    form = SQLFORM(db.Texts).process()
    from gluon.tools import Mail
    mail = Mail()
    mail.settings.server = 'smtp.gmail.com:587'
    mail.settings.sender = 'weslylim94@gmail.com'
    mail.settings.login = 'weslylim94@gmail.com:edvrygzm'
    s = "weslylim94@gmail.com"              #T-Mobile
    """
    from gluon.contrib.sms_utils import SMSCODES, sms_email
    if mail.send(to='1415658-1151@tmomail.net',
        subject='test',
        message= 'just work please'):
        response.flash = mail.result
    else:
        response.flash = mail.error
    """
    import json
    import urllib2
    url = 'http://api.openweathermap.org/data/2.5/weather?zip=94132,us&appid=2879ca2ea905f3cabb636b5e0b71ad48'
    info = json.load(urllib2.urlopen(url))
    response.flash = (9*(info['main']['temp'])/5) - 459.4
    return locals()

@auth.requires_login()
def reminder_create():
    form = SQLFORM(db.Reminders).process()
    if form.process().accepted:
        redirect(URL('index'))
    return locals()

@auth.requires_login()
def reminder_edit():
    record = db.Reminders(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.Reminders, record, deletable=True)
    if form.process().accepted:
        redirect(URL('index'))
    return locals()

@auth.requires_login()
def text_create():
    form = SQLFORM(db.Texts).process()
    if form.process().accepted:
        redirect(URL('index'))
    return locals()

@auth.requires_login()
def text_edit():
    record = db.Texts(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.Texts, record)
    if form.process().accepted:
        redirect(URL('index'))
    return locals()

@auth.requires_login()
def archive():
    reminder = db(db.Reminders).select(db.Reminders.ALL)
    form = SQLFORM(db.Archive).process()
    return locals()

@auth.requires_login()
def text_message():
    reminder = db(db.Reminders).select(db.Reminders.ALL)
    return locals()

def user():
    return dict(form=auth(), auth=auth)


@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()

def logout():
    auth.logout()
    return locals()
