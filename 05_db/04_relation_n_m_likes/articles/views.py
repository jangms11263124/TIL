from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:            
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form, 
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:            
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/form.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def comment_create(request, pk):
    # pk - article의 pk 값 
    # 댓글의 pk 지금은 안필요 
    article = Article.objects.get(pk=pk)
    user = request.user
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = user # request.user랑 동일
            comment.save()
            return redirect('articles:detail', article.pk)
    context = {
        'comment_form' : comment_form,
    }
    return redirect('articles:detail', article.pk)


def likes(request, pk):
    article = Article.objects.get(pk=pk)
    user = request.user 

    # 좋아요 추가
    # 일단 내가 좋아요를 누른 상태 x
    # article.like_users 안에 user 없어요 
    # add 
    if user not in article.like_users.all():
        article.like_users.add(user)

    # 좋아요 삭제 
    # 일단 내가 좋아요를 누른 상태 o
    # article.like_users 안에 user 있어요
    # remove
    elif user in article.like_users.all():
        article.like_users.remove(user)
    
    return redirect('articles:index')
