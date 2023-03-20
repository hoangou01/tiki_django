from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

def index(request):
    return HttpResponse("hihi")
def welcome(request , year):
    return HttpResponse("hello" + str(year))

class TestView(View):
    def get(self , request):
        return HttpResponse("hihi")
    def post(self , request):
        pass
