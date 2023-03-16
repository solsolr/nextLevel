from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("hello raspberryPI")


def mqttTest(request):
    return render(request, 'raspberrypi/mqtt.html')

def socketTest(request):
    return render(request, 'raspberrypi/socket.html')