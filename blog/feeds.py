#!/usr/local/python3/bin/python3
from django.contrib.syndication.views import Feed


from .models import Post

class PostRssFeed(Feed):
    title = '读书博客'

    link = '/index/'

    description = '读书博客推送'

    def items(self):
        return Post.objects.all()


    def item_title(self, item):
        return "%s"%item.title

    def item_description(self, item):
        return item.content