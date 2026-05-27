from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'name': 'jihye',
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'GET':
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
    
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # form.save()
            # return redirect('articles:index')
            article = form.save()
            return redirect('articles:detail', article.pk)
            

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    
    elif request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save() # db는 변경됨
            return redirect('articles:detail', article.pk)
            