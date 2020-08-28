from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from django.utils.http import is_safe_url

import random

from .models import Tweets
from .forms import TweetForm
from django.conf import settings
from rest_framework.response import Response
from .serializers import Tweetserializers, TweetActionSerializers,TweetsCreateSerializers


from rest_framework.decorators import api_view, permission_classes  #authentication_classes
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication





@api_view(["POST"])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    data = request.POST
    serializers = TweetsCreateSerializers(data=data)
    if serializers.is_valid(raise_exception=True):
        serializers.save(user=request.user)
        print(serializers.data)
        return Response(serializers.data,status=201)
    return Response({},status=400)

@api_view(["GET"])
def tweeter_list_view(request):
    tweets = Tweets.objects.all()
    serializersTweets = Tweetserializers(tweets,many=True)
    return Response(serializersTweets.data, status=200)

@api_view(["GET"])
def tweets_detailed_view(request, id, *args, **kwargs):
    tweet = Tweets.objects.filter(id=id)
    if not tweet.exists():
        return Response({},status=400)
    obj = tweet.first()
    serializersTweets = Tweetserializers(obj)
    return Response(serializersTweets.data, status=200)

@api_view(["DELETE","POST"])
@permission_classes([IsAuthenticated])
def tweets_delete_view(request, id, *args, **kwargs):
    tweet = Tweets.objects.filter(id=id)
    if not tweet.exists():
        return Response({},status=400)
    tweet = tweet.filter(user=request.user)
    if not tweet.exists():
        return Response({"message":"u are not allowed to delete"}, status=401)
    obj = tweet.first()
    obj.delete()
    return Response({"message":"tweet has been removed"}, status=200)



@api_view(["POST","DELETE"])
@permission_classes([IsAuthenticated])
def tweets_action_view(request, *args, **kwargs):
    serializer = TweetActionSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get("id")
        action = data.get("action")
        content = data.get("content")
        tweet = Tweets.objects.filter(id=tweet_id)
        if not tweet.exists():
            return Response({},status=404)
        obj = tweet.first()
        if action == "like":
            obj.likes.add(request.user)
            serializers = Tweetserializers(obj)
            return Response(serializers.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializers = Tweetserializers(obj)
            return Response(serializers.data, status=200)
        elif action == "retweet":
            new_tweet = Tweets.objects.create(
                user=request.user,
                parent=obj,
                content=content,
            )
            serializers = Tweetserializers(new_tweet)
            return Response(serializers.data, status=201)
    return Response({"message":"u liked the tweet"}, status=200)



def index_pure_django(request, *args, **kwargs ):
    if request.user.is_authenticated:
        username = request.user.username
    return render(request ,"tweets/templates/index.html",{"username":username})

def tweet_create_view_pure_django(request, *args, **kwargs):
    print(request.user)
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax:
            return JsonResponse({},status=401)
        return redirect(settings.LOGIN_URL)

    form = TweetForm(request.POST or None )
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user ##  or None only use it when user in not nessory to login
        obj.save()
        if request.is_ajax:
            return JsonResponse(obj.serializer(),status=201)
        if next_url != None and is_safe_url(next_url, settings.ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax:
            return JsonResponse(form.errors,status=400)

    return render(request, "tweets/templates/components/form.html",context={"form":form})


def tweeter_list_view_pure_django(request):
    tweets = Tweets.objects.all()

    # one way to chage django object to python dictionary
    # tweets_list =  [{"id":x.id,"content":x.content,"likes":random.randint(0,100)}for x in tweets]

    #way2
    tweets_list = [(x.serializer())for x in tweets]
    data = {
        "response":tweets_list
    }
    return JsonResponse(data,status=200)





def tweets_detailed_view_pure_django(request, id, *args, **kwargs):
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