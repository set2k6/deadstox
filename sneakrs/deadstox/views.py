# from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404, render, HttpResponse
# from django.views import generic
from .models import *
from django.contrib.auth.models import User
from rest_framework import viewsets
# from django.shortcuts import HttpResponse
from deadstox.serializers import ClosetsSerializer, SneakersSerializer
import datetime

class ClosetsViewSet(viewsets.ModelViewSet):
    queryset = Closets.objects.all()
    serializer_class = ClosetsSerializer


class SneakersViewSet(viewsets.ModelViewSet):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer


# # Create your views here.
# def index(request):
# # class IndexView(generic.ListView):
#   # template_name = 'nessie/index.html'
#   # context_object_name = 'all_events'
#   return HttpResponse("Hello, world. You're at the deadstox index.")

#   def get_queryset(request):
#     return Closet.objects.all()
#     return Sneaker.objects.all()

# def closetCreate(request):
#     model = Closets
#     return HttpResponse("this is closet create view.")

# def in_closet(request):
#     pass

# def sneakerCreate(request):
#     model = Sneakers
#     return HttpResponse("This is the sneaker create view")

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
