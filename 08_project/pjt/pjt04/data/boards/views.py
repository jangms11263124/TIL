import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.conf import settings
from django.contrib import messages
from .models import Post
from .forms import PostForm
from .services import check_inappropriate_content

def load_assets():
    import os
    with open(os.path.join(settings.BASE_DIR, 'assets.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def get_asset_or_404(asset_id):
    assets = load_assets()
    for asset in assets:
        if asset['id'] == asset_id:
            return asset
    raise Http404("해당 자산을 찾을 수 없습니다.")

def asset_list(request):
    assets = load_assets()
    return render(request, 'boards/asset_list.html', {'assets': assets})

def board_list(request, asset_id):
    asset = get_asset_or_404(asset_id)
    posts = Post.objects.filter(asset_id=asset_id).order_by('-created_at')
    return render(request, 'boards/board_list.html', {'asset': asset, 'posts': posts})

def post_create(request, asset_id):
    asset = get_asset_or_404(asset_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if check_inappropriate_content(title, content):
                messages.error(request, '부적절한 표현이 감지되어 게시글 등록이 차단되었습니다.')
            else:
                post = form.save(commit=False)
                post.asset_id = asset_id
                post.save()
                return redirect('boards:board_list', asset_id=asset_id)
    else:
        form = PostForm()
    return render(request, 'boards/post_form.html', {'form': form, 'asset': asset, 'action': '작성'})

def post_detail(request, asset_id, post_id):
    asset = get_asset_or_404(asset_id)
    post = get_object_or_404(Post, pk=post_id, asset_id=asset_id)
    return render(request, 'boards/post_detail.html', {'asset': asset, 'post': post})

def post_update(request, asset_id, post_id):
    asset = get_asset_or_404(asset_id)
    post = get_object_or_404(Post, pk=post_id, asset_id=asset_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if check_inappropriate_content(title, content):
                messages.error(request, '부적절한 표현이 감지되어 게시글 수정이 차단되었습니다.')
            else:
                form.save()
                return redirect('boards:post_detail', asset_id=asset_id, post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'boards/post_form.html', {'form': form, 'asset': asset, 'post': post, 'action': '수정'})

def post_delete(request, asset_id, post_id):
    asset = get_asset_or_404(asset_id)
    post = get_object_or_404(Post, pk=post_id, asset_id=asset_id)
    if request.method == 'POST':
        post.delete()
        return redirect('boards:board_list', asset_id=asset_id)
    return redirect('boards:post_detail', asset_id=asset_id, post_id=post.pk)

def custom_404(request, exception):
    return render(request, '404.html', status=404)
