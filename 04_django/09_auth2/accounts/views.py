from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    # 님의 정보 필요 
    print('accounts의 index 일단 접근 가능! ')
    return render(request, 'accounts/index.html')


# create랑 비슷  
def login(request):
    # POST: 로그인을 수락
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # login
        if form.is_valid():
            # form 저장 x
            # user = form.get_user()
            auth_login(request, form.get_user())
            return redirect('accounts:index')
        
        # signup 
        # if form.is_valid():
            # form 저장 o, user객체로 만들어서 
            # user = form.save() 
            # 로그인 시켜주고 
            # auth_login(request, user)
            # index로 보냄 그러면 로그인된 상태로 페이지가 리다이렉팅

    # GET: 로그인 창을 보여줌
    else: 
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return  render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST': 
        auth_logout(request)
        return redirect('accounts:index')
    

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # .save() 유저 생성 완료!!! 
            ## login 과 로직 비교 start 
            # form 저장 x
            # user = form.get_user()
            # auth_login(request, form.get_user())
            ## login 과 로직 비교 end
            auth_login(request, user) # 로그인된 상태로 index 보여줄려고
            return redirect('accounts:index')

    else:
        # 회원가입 폼
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        auth_logout(request)
        return redirect('accounts:index')