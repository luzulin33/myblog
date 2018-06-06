from django import template
from blog.models import Post, Category, Tag
register = template.Library()
from django.db.models import Count

@register.simple_tag
def get_recent_post():
    return Post.objects.all().order_by('-modified_time')[:5]


# 歸檔
@register.simple_tag
def post_time():
    return Post.objects.dates('create_time', 'day', order='DESC')[:5]

# 分类
@register.simple_tag
def post_category():
    return Category.objects.all()


@register.simple_tag
def post_tags():
    return Tag.objects.all()


# 给category添加post数量属性
@register.simple_tag
def post_count():
    return Category.objects.annotate(post_counts=Count('post')).filter(post_counts_gt = 0)




