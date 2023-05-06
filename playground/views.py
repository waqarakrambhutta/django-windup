from django.core.mail import send_mail,mail_admins,BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        mail_admins('subject','message',html_message='messages')
        #mail admin require configuration in the settings.
    except BadHeaderError:
        pass # we can also show the error message.
    return render(request, 'hello.html', {'name': 'Mosh'})
