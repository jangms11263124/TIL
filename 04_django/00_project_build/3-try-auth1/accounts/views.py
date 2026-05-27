from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


def index(request):
    # 님의 정보 필요 
    print('accounts의 index 일단 접근 가능! ')
    return render(request, 'accounts/index.html')


# create랑 비슷  
def login(request):
    # POST: 로그인을 수락
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    # GET: 로그인 창을 보여줌
    else: 
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return  render(request, 'accounts/login.html', context)
