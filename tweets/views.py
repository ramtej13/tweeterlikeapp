from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from django.utils.http import is_safe_url

import random

from .models import Tweets
from .forms import TweetForm
from django.conf import settings


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


# Create your views here.
def index(request, *args, **kwargs ):
    tweets = Tweets.objects.all()
    return render(request ,"tweets/templates/index.html",{"data":tweets})

def tweet_create_view(request, *args, **kwargs):
    print("ajax:", request.is_ajax())
    form = TweetForm(request.POST or None )
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax:
            return JsonResponse(obj.serializer(),status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax:
            return JsonResponse(form.errors,status=400)

    return render(request, "tweets/templates/components/form.html",context={"form":form})

def tweeter_list_view(request):
    tweets = Tweets.objects.all()

    # one way to chage django object to python dictionary
    # tweets_list =  [{"id":x.id,"content":x.content,"likes":random.randint(0,100)}for x in tweets]

    #way2
    tweets_list = [(x.serializer())for x in tweets]
    data = {
        "response":tweets_list
    }
    return JsonResponse(data,status=200)


def tweets_detailed_view(request, id, *args, **kwargs):
    print(args,kwargs)
    data = {
        "id":id
    }
    status = 200
    try:
        tweets = Tweets.objects.get(id=id)
        data['content'] = tweets.content
        print(tweets)
    except:
        data['message'] = "notfound"
        status = 404
    return JsonResponse(data,status=status)