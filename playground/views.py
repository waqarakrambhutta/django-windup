from django.core.cache import cache
from django.shortcuts import render
import requests

def say_hello(request):
    key = 'httpbin_result'  # we can set it anything.
    if cache.get(key) is None:
        response = requests.get('http://httpbin.org/delay/2')
        data = response.json()
        cache.set(key,data)    # cache.set(key,data, 10 * 60) for setting time to 10 minutes

    return render(request, 'hello.html', {'name': cache.get(key)})
