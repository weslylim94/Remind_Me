# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################



## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Reminder List'), False, URL('default', 'index')),
    (T('Create Reminder'), False, URL('default', 'reminder_create')),
    (T('Text Message'), False, URL('default', 'text_message')),
    (T('Archive'), False, URL('default', 'archive')),
    (T('Profile'), False, URL('default', 'user/profile')),
    (T('Logout'), False, URL('default', 'logout')),
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################



if "auth" in locals(): auth.wikimenu()
