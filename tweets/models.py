from django.db import models
from django.conf import settings
import random
# Create your models here.
# User = settings.AUTH_
class Tweets(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    TweetImage = models.ImageField(blank=True,upload_to='tweets_images/')

    class Meta:
        ordering = ['-id']
    def serializer(self):
        return {
        "id": self.id,
        "content" : self.content,
        "likes" : random.randint(0,100)
        }