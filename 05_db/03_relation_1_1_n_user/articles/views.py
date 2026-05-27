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
            # 객체를 내가 만든 필드에 넣어줌 
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
    # 댓글은 혼자 저장이 안됨, 어느 게시글에 소속
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # 1. article 객체를 내가 만든 필드에 넣어줌  
        comment.article = article
        # 2. user 객체를 내가 만든 필드에 넣어줌 
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
        # return redirect('articles:detail', pk)
    '''
    if request.method == 'POST':
        # 저장
        pass 
    else:
        pass
    '''
    '''
    폼을 보여줬어요
    게시글을 보면서 댓글을 달거라서 ... 
    한눈에 볼 수 있도록 detail에 다가 댓글 작성 폼을 보여주자
    '''
    context =  {
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)


def comment_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == comment.user:
        if request.method == 'POST':
            comment = Comment.objects.get(pk=comment_pk)
            comment.delete()
            return redirect('articles:detail', article.pk)
            # return redirect('articles:detail', article_pk)