from django.shortcuts import render, redirect
from .models import Article
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


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all() # queryset 
    context = {
        'article': article,
        'comment_form': comment_form, 
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
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


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')


def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)


def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    me = request.user

    # 좋아요 누르기 할려면 
    # 게시글에 좋아요 누른 사람에 내가 없어야함 
    if me not in article.like_users.all():
        article.like_users.add(me)

    # 좋아요 취소 할려면
    # 게시글에 좋아요 누른 사람에 내가 있어야 함 
    else: 
        article.like_users.remove(me)

    return redirect('articles:detail', article.pk)