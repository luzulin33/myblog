from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator
from math import  ceil
from django.db.models import Q
from django.urls import reverse


import markdown
# 导入锚点模块
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


from comment.forms import CommentForm
from comment.models import Comment


from .models import Tag

# Create your views here.
def index(request):
    PAGE_NUM = 1
    post_list = Post.objects.all().order_by('-modified_time')

    # 处理标签过来的跳转
    p_tag= request.GET.get('p_tag')
    if p_tag:
        post_list = Post.objects.filter(tag__name=p_tag).order_by("-create_time")

    # 处理分类过来的跳转
    p_category = request.GET.get('p_category')
    if p_category:
        post_list = Post.objects.filter(category__name = p_category).order_by("-create_time")

    page_count = ceil(len(post_list) / PAGE_NUM)
    page = request.GET.get('page', 1)
    # pages = ceil(Post.objects.count())
    paginator = Paginator(post_list, PAGE_NUM)
    post_list = paginator.page(page)

    # 添加搜索的分页逻辑
    search = None

    return render(request, 'blog/index.html', context={'post_list':post_list, "paginator":paginator,"page_num":range(page_count)})


# 使用view视图改写
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = "post_list"

    def get_queryset(self):
        return super(IndexView, self).get_queryset().order_by('-create_time')



def detail(request):
    post_id = request.GET.get('post', 1)
    post = Post.objects.get(id = post_id)
    comment_form = CommentForm()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify)
    ])
    post.content = md.convert(post.content)
    post.toc = md.toc
    post.save()
    post.view_times()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            comment_list = Comment.objects.filter(post=post)
            return render(request, 'blog/page.html',
                          context={'post': post, 'comment_list': comment_list, 'comment_form': comment_form})
    else:
        comment_list = Comment.objects.filter(post=post)
        return render(request, 'blog/page.html', context = {'post': post,'comment_list':comment_list,'comment_form':comment_form})



def p_time(request,year,month,day):
    # year = request.GET.get('year')
    # month = request.GET.get('month')

    # post_list =  Post.objects.filter(create_time__year=year,
    #                                  create_time__month=month)
    post_list = Post.objects.filter(modified_time__year=year,
                                    modified_time__month=month,
                                    modified_time__day=day
                                    ).order_by("-create_time")
    # post_list = Post.objects.all()
    return render(request, 'blog/index.html',locals())

def p_category(request):
    p_category = request.GET.get('p_category')

    # post_list = Post.objects.filter(category__name=p_category).order_by('-modified_time')
    # return render(request, 'blog/index.html', {'post_list': post_list})
    return redirect('/blog/index?p_category=%s' % (p_category))


# def p_tags(request):
#     p_tag = request.GET.get('tag')
#     post_list = Post.objects.filter(tag__name=p_tag).order_by('-create_time')
#     return render(request, 'blog/index.html', {'post_list': post_list})


# 使用跳转到首页视图的方式添加分页功能
def p_tags(request):
    p_tag = request.GET.get('tag',None)
    # post_list = Post.objects.filter(tag__name=p_tag).order_by('-create_time')
    return redirect('/blog/index?p_tag=%s' % (p_tag))


# 未知如何获取request，废弃
# # 使用ListView改写
# class TagList(ListView):
#     context_object_name = "post_list"
#     model = Post
#     template_name = 'blog/index.html'
#
#     def get_queryset(self):
#         p_tag = self.kwargs.get('tag')
#         print("====================")
#         print(p_tag)
#         return super(TagList,self).get_queryset().filter(tag__name = p_tag).order_by('-create_time')



def search(request):
    s_word = request.POST.get('search')

    error_msg = ''

    if not s_word:
        error_msg = '请输入关键字'
        return render(request, 'blog/index.html',{'error_msg':error_msg})
    post_list = Post.objects.filter(Q(title__icontains=s_word) | Q(content__icontains=s_word))

    PAGE_NUM = 1
    page_count = ceil(len(post_list) / PAGE_NUM)
    page = request.GET.get('page', 1)
    # pages = ceil(Post.objects.count())
    search_paginator = Paginator(post_list, PAGE_NUM)
    post_list = search_paginator.page(page)
    return render(request, 'blog/index.html',
                  {"post_list": post_list, "page_num": range(page_count), "search_paginator": search_paginator})


# 联系板块
def relation(request):
    ralation_msg = "yes"
    return render(request, 'blog/relation.html',{"ralation_msg":ralation_msg})


