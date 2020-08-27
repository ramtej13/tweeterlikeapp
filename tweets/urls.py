
from .views import index,tweets_detailed_view,tweeter_list_view,tweet_create_view
from django.urls import path,include

urlpatterns = [
    path('',index, name="index"),
    path('create-tweet', tweet_create_view, name="tweet_create_view"),
    path('tweets', tweeter_list_view, name="tweeter_list_view"),
    path('<id>/', tweets_detailed_view, name="tweets_detailed_view")

]