from django.shortcuts import render
from .models import Article

# Create your views here.
def index (request):
    articles = Article.objects.all()
    context = {
        'name': 'haley',
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)