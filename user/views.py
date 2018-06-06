from django.shortcuts import render ,redirect,reverse
from django.http import HttpResponse


from .forms import UserForm
from .models import User
# Create your views here.
def register(request):
    error_msg = ''
    if request.method == 'POST':
        userForm = UserForm(request.POST, request.FILES)
        if userForm.is_valid():
            userForm.save()
            succee_register = "yes"
            return render(request,'user/register_done.html',{"succee_register":succee_register})

        else:
            error_msg = '信息验证有误'


    if request.method == 'GET':
        userForm = UserForm()
    return render(request, 'user/register.html', {'userForm':userForm,"error_msg":error_msg})


def personInfo(request):
    # user = User.objects.get(username = request.user.username)

    # userInfoForm = UserForm(user)
    userInfoForm = UserForm()
    # print(type(request.user.username))
    return render(request, 'user/personInfo.html',{"userInfoForm":userInfoForm})

