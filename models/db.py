db = DAL('sqlite://storage.sqlite', pool_size=1, lazy_tables=True, migrate=True, adapter_args=dict(foreign_keys=False))
from gluon.tools import Auth
import datetime
auth = Auth(db)
auth.settings.extra_fields['auth_user']= [
  Field('phone_number', requires = IS_MATCH('^1?((-)\d{3}-?|\(\d{3}\))\d{3}-?\d{4}$', error_message='1-xxx-xxx-xxxx'))]
auth.define_tables(username=True)

db.auth_user.last_name.readable = db.auth_user.last_name.writable = False

#table for the posting after posted
db.define_table('Reminders',
   Field('reminder_message', 'text'),
   Field('reminder_start', 'date', default=request.now, required=True, requires = IS_DATE(format=("%m/%d/%Y"))),
   Field('reminder_end', 'date', default=request.now, required=True, requires = IS_DATE(format=("%m/%d/%Y"))),
   Field('reminder_type', requires = IS_IN_SET(("Daily", "Weekly", "One-Time"))),
   Field('disable', 'boolean'),
   Field('user'),
   format = '%(title)s')

db.Reminders.user.readable = db.Reminders.user.writable = False
db.Reminders.id.readable = False

import time
db.define_table('Archive',
    Field('reminder'),
    Field('filler'),
    format = '%(title)s')

db.define_table('Texts',
    Field('time_for_message_to_be_sent', 'time'),
    format = '%(title)s')

db.Texts.id.readable = False


db.Archive.reminder.readable = db.Archive.reminder.writable = False
