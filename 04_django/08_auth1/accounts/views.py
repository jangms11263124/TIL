from django.shortcuts import render, redirect
# GET으로 auth user form을 보여주기 위함 
from django.contrib.auth.forms import AuthenticationForm

# POST로 전달 받은 정보를 로그인 하기 위해서 가져오는 함수
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model

# Create your views here.
# 재정의 overriding 
def login(request):
    # POST 로그인 시켜주면됨 
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
            # return redirect('articles:detail', user.pk)
    # GET 로그인 창
    else: 
        # 1. form을 만들어서 보내줌
        form =  AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
    
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)