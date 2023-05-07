from django.core.mail import EmailMessage,BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage('subject','message','waqar@domain.com',['qasim@domain.com'])
        message.attach_file('playground/static/images/Mosque.jpg')
        message.send()
    except BadHeaderError:
        pass # we can also show the error message.
    return render(request, 'hello.html', {'name': 'Mosh'})
