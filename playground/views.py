
from django.shortcuts import render
from rest_framework.views import APIView
import logging
import requests

logger = logging.getLogger(__name__) # __name__ means playground.views, now we can use logger.info,debug,error or warning and so on.

class HelloView(APIView):
    def get(self,request):
        
        try:
            logger.info('Calling httpbin')
            response = requests.get('http://httpbin.org/delay/2')
            logger.info('Received the response ')
            data = response.json()

        except requests.ConnectionError:
            logger.critical('Logger is offline.')
        return render(request, 'hello.html', {'name': 'Waqar'})