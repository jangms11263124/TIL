from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index (request):
    articles = Article.objects.all()
    context = {
        'name': 'haley',
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # get, filter
    article = Article.objects.get(pk=pk)
    # get은 객체 1개만 반환
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save() # article이 생성 저장이 되는 순간 pk가 생길 것이고, redirect로 전달 

    # return render(request, 'articles/create.html')
    # return rennder(reuqest, 'articles/create.html', context)

    # redirect는 어디로 보낼지 url, 특정 값도 함께 보낼 수 있음 , 쉼표로 구분
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 1. 삭제하고 싶은 객체 조회
    article = Article.objects.get(pk=pk)
    # 2. 삭제 
    article.delete()

    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 1. 객체 조회
    article = Article.objects.get(pk=pk)
    # 2. request.POST 안에 있는 정보로 업데이트
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 3. 저장
    article.save()

    return redirect('articles:detail', article.pk)