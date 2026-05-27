from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model # 객체 반환
# from django.conf import settings
# settings.AUTH_USER_MODEL = 'accounts.User'

# User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request, user) 
            return redirect('articles:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else: 
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return  render(request, 'accounts/form.html', context)

def logout(request):
    if request.method == 'POST': 
        auth_logout(request)
        return redirect('articles:index')
    
# urls.py 추가 필요 
# template form.html 도 수정 필요 

@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        auth_logout(request)
        return redirect('accounts:index')
    
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=request.user) 
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user) 

    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = PasswordChangeForm(user=request.user) 
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


def profile(request, username):
    User = get_user_model() # 우리가 models.py에 만든 User 모델 
    person = User.objects.get(username=username)
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user
    if me != you:
        # me 가 you를 팔로잉을 하고 싶어! 
        # 그러면 you의 followers 목록에 me가 없으면 됨
        if me not in you.followers.all():
            you.followers.add(me)

        # me 가 you를 팔로잉 취소하고 싶어! 
        # 그러면 you의 followers 목록에 m가 있으면 됨
        else:
            you.followers.remove(me)

        return redirect('accounts:profile', you.username)
    else:
        return redirect('articles:index')
