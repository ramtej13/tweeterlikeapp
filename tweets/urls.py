from .views import index_pure_django,tweets_detailed_view,tweeter_list_view,tweet_create_view,tweets_delete_view,tweets_action_view
from django.urls import path

urlpatterns = [
    path('',index_pure_django, name="index"),
    path('api/', tweeter_list_view, name="tweeter_list_view"),
    path('api/create/', tweet_create_view, name="tweet_create_view"),
    path('api/<id>/', tweets_detailed_view, name="tweets_detailed_view"),
    path('api/tweets/action/', tweets_action_view, name="tweets_action_view"),
    path('api/<id>/delete/', tweets_delete_view, name="tweets_delete_view")
]
