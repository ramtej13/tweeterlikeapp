from rest_framework import serializers

from .models import Tweets

from django.conf import settings

class TweetActionSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validated_action(self, value):
        value = value.lower().strip()
        if not value in settings.TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("this is not a valid action for tweets")
        return value


class TweetsCreateSerializers(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweets
        fields = ['content','id','likes']

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self,value):
        if len(value) > settings.MAX_TWEET_LENGTH:
            raise serializers.ValidationError("this tweet is to long ")
        return value

class Tweetserializers(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    parent = TweetsCreateSerializers(read_only=True)

    # content = serializers.SerializerMethodField(read_only=True)
    # is_retweet = serializers.SerializerMethodField(read_only=True) #dont have to do this since it is a object of models
    class Meta:
        model = Tweets
        fields = ['content','id','likes','is_retweet',"parent"]

    def get_likes(self, obj):
        return obj.likes.count()

    # def get_content(self, obj):
    #     content = obj.content
    #     if obj.is_retweet:
    #         content = obj.parent.content
    #     return content
