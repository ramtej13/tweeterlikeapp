from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Tweets

from rest_framework.test import APIClient


User = get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='zca',password='somepassword')
        self.user2 = User.objects.create_user(username='zca-2',password='somepassword2')

        Tweets.objects.create(content="my one  test", user=self.user)
        Tweets.objects.create(content="my two test", user=self.user)
        Tweets.objects.create(content="my threr test", user=self.user2)

        self.currentCount = Tweets.objects.all().count()
        # User.objects.Create_user(username='zxc',password='somepassword')

    def test_tweet_created(self):
        tweet = Tweets.objects.create(content="my secon test", user=self.user)
        self.assertEqual(tweet.id,4)
        self.assertEqual(tweet.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/api/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.json()),3)

    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/",{"id":1,"action":"like"})
        self.assertEqual(response.status_code,200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 1)
        # print(response.json(),"likes: ", like_count)
        # self.assertEqual(len(response.json()),3)

    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/",{"id":2,"action":"like"})
        self.assertEqual(response.status_code,200)
        response = client.post("/api/tweets/action/",{"id":2,"action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0)

    def test_action_reTweet(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/",{"id":2,"action":"retweet"})
        self.assertEqual(response.status_code,201)
        data=response.json()
        new_tweet_id = data.get("id")
        self.assertNotEqual(2,new_tweet_id)
        self.assertEqual(self.currentCount+1,new_tweet_id)

    def test_tweet_create_api_view(self):
        data = {"content":"hello woarld",}
        client = self.get_client()
        response = client.post("/api/create/",data)
        self.assertEqual(response.status_code,201)
        response_data = response.json()
        new_tweet_id = response_data.get("id")
        self.assertEqual(self.currentCount+1,new_tweet_id)

    def test_tweet_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/1/")
        self.assertEqual(response.status_code,200)
        _id = response.json().get("id")
        self.assertEqual(_id,1)

    def test_tweet_delete_api_view(self):
        client = self.get_client()
        response = client.delete("/api/1/delete/")
        self.assertEqual(response.status_code,200)
        client = self.get_client()
        response = client.delete("/api/1/delete/")
        print(response)
        self.assertEqual(response.status_code,400)
        response_response_incorrect_owner = client.delete("/api/3/delete/")
        self.assertEqual(response_response_incorrect_owner.status_code,401)





    #     like_count = response.json().get("likes")
    #     self.assertEqual(like_count, 1)
    #     print(response.json(),"likes: ", like_count)











    # def test_user_created(self):
    #     user = User.objects.get(username="zca")
    #     self.assertEqual(user.username,"zca")