from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from community.models import Post, Comment

def signup(request):
    if request.user.is_authenticated:
        return redirect('community:asset_list')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:asset_list')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('community:asset_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('community:asset_list')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('community:asset_list')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'accounts/password_done.html')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    person = get_object_or_404(User, username=username)
    # Interest stocks is a comma separated string
    interest_stocks_list = [s.strip() for s in person.interest_stocks.split(',')] if person.interest_stocks else []
    # Post.author is a CharField storing username as per F506
    posts = Post.objects.filter(author=username)
    comments = Comment.objects.filter(author=username).select_related('post')
    context = {
        'person': person,
        'interest_stocks_list': interest_stocks_list,
        'posts': posts,
        'comments': comments,
    }
    return render(request, 'accounts/profile.html', context)
