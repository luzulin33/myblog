from django.shortcuts import render
from .forms import CommentForm
from blog.models import Post

# 路由设计考虑不当。作废
# Create your views here.
# def comment_list(request):
#     p_id = request.GET.get('id')
#     post = Post.objects.get(id = p_id)
#     comment_form = CommentForm()
#     comment_list = post.comment_set
#     if request.method == 'POST':
#         pass
#
#     else:
#         return render(request, 'blog/page.html',
#                       context={'post': post, 'comment_list': comment_list, 'comment_form': comment_form})