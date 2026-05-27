from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

def index(request):
    articles = Article.objects.all()
    print(articles)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    # POST - 저장 (새롭게 생성)
    if request.method == 'POST':
        # print('create POST 들어옴')
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # 저장을 하고 index로 보내줄지?
            # form.save()
            # return redirect('articles:index')
            # 아니면 detail로 보내줄지?
            article = form.save()
            return redirect('articles:detail', article.pk)

    # GET - form 보여줄 
    else:
        form = ArticleForm() 
        # ArticleForm은 form 태그가 아님
    context = {
        'form' : form,
    }
    return render(request, 'articles/form.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'person': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')
    

def update(request, pk):
    article = Article.objects.get(pk=pk)
    # POST - 저장 (기존 정보 수정)
    if request.method == 'POST':
        # print('update POST 들어옴')
        form = ArticleForm(request.POST, request.FILES, instance=article) # 새롭게 생성
        if form.is_valid():
            # 저장을 하고 index로 보내줄지?
            # form.save()
            # return redirect('articles:index')
            # 아니면 detail로 보내줄지?
            article = form.save()
            return redirect('articles:detail', article.pk)

    # GET - form 보여줄 
    else:
        form = ArticleForm(instance=article) 
        # ArticleForm은 form 태그가 아님
    context = {
        'form' : form,
        'article': article,
    }
    return render(request, 'articles/form.html', context)