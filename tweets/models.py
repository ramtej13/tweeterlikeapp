from django.db import models
from django.conf import settings
import random
# Create your models here.
User = settings.AUTH_USER_MODEL

class TweetLikes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweets",on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweets(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="tweet_likes",blank=True,through=TweetLikes)
    content = models.TextField(blank=True,null=True)
    TweetImage = models.ImageField(blank=True,upload_to='tweets_images/',null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_retweet(self):
        return self.parent != None

    def serializer(self):
        '''
        :return: feel free to delete old method
        '''
        return {
        "id": self.id,
        "content" : self.content,
        "likes" : self.likes
        }