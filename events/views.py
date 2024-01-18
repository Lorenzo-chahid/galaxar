from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    print("CHIPPOS ")
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Create your views here.
def home(request):
    print("DEFLAGRATION")
    return HttpResponse("My calendar")
