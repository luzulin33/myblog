from django.db import models
from django.utils.html import strip_tags
from django.urls import reverse
from user.models import User


import markdown

# Create your models here.
class Post(models.Model):
    # title,content,excerpt,created_time,modified_time,tag,category,author,comment
    title = models.CharField(max_length=40, verbose_name='文章标题')
    excerpt = models.CharField(max_length=200, verbose_name="文章摘要", blank=True, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now= True, verbose_name="修改时间")
    views = models.IntegerField(verbose_name="阅读次数", default=0)
    user = models.ForeignKey(User)

    tag = models.ForeignKey('Tag')
    category = models.ManyToManyField('Category')

    class Meta:
        ordering = ['-create_time']


    def __str__(self):
        return self.title

    def view_times(self):
        self.views += 1
        self.save(update_fields=['views'])


    # 重写save方法
    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions = [
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])

            self.excerpt = strip_tags(md.convert(self.content))[:54]

        super(Post,self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('blog:rss')



class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签')

    def __str__(self):
        return self.name

    pass


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="类别")

    def __str__(self):
        return self.name
    pass


