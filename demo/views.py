from django.shortcuts import render,HttpResponse,redirect
from .models import test
# Create your views here.
from hello.settings import LOGIN_URL

def index(request):
    hello = test.objects.all()
    return render(request,"demo/templates/index.html", {"hello":hello})

def pets(request):
    dell = request.user
    if not request.user.is_authenticated:
        return redirect(LOGIN_URL)