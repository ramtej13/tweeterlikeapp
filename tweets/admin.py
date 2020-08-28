from django.contrib import admin
from .models import Tweets, TweetLikes

# Register your models here.
class TweetLikesAdmin(admin.TabularInline):
    model = TweetLikes

class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikesAdmin]
    list_display = ['__str__','user']
    search_fields = ['content', 'user__username', 'id']
    class Meta:
        model = Tweets



admin.site.register(Tweets,TweetAdmin)