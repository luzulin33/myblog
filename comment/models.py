from django.db import models
from blog.models import Post

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=30, verbose_name="姓名")
    email = models.EmailField(max_length=255, verbose_name="邮箱")
    url = models.URLField(max_length=100, verbose_name="网址")
    text = models.TextField(verbose_name="评论")

    create_time = models.DateTimeField(auto_now=True, verbose_name="发表时间")
    post = models.ForeignKey(Post, verbose_name="评论文章")

    def __str__(self):
        self.name


