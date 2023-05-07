from django.core.mail import EmailMessage,BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name':'WAQAR'}            
        )
        message.send(['to@domain.com'])
    except BadHeaderError:
        pass # we can also show the error message.
    return render(request, 'hello.html', {'name': 'Waqar'})
