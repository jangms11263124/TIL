from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# form . # 지금 내가 있는 경로
# from .파일명 # 해당 파일에서
# from .파일명 import 클래스  # 해당 파일에 있는 클래스를 가져올게
# ArticleForm.sample()

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    # 사용자가 데이터를 입력할 수 있는 빈 form 페이지를 보여주는 역할
    # 비어있는 form
    form = ArticleForm() # modelForm
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    form = ArticleForm()
    # 1. 사용자 입력 데이터를 통째로 Form 클래스의 인자로 넣어서 인스턴스를 생성
    # request.POST에서 받아온 내용을 채운 form
    # 요청이 POST인지, GET인지 체크 

    # GET이면 form을 template에 보여줘
    # method="GET", a태그쓰거나 url로 직접접근 
    if request.method == 'GET':
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)
    
    # POST로 들어오면 request.POST로 받은 값을 article 저장해줘
    else:
        # form을 먼저 저장을 받고
        form = ArticleForm(request.POST)

    
    # 2. 사용자의 입력 데이터가 유효한지(데이터타입, 제약조건) 검사
    if form.is_valid():  # t/f
        # 2.1 유효성 검사가 통과하면 저장
        article = form.save() # instance
        return redirect('articles:detail', article.pk)



def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# 생성과 수정의 차이는 기존 Data 유무의 차이!
def edit(request, pk):
    # 1. 수정할 게시글의 기존 데이터를 pk를 이용해 조회
    article = Article.objects.get(pk=pk)
    # 비어있는 Form이 아닌 조회한 Data를 값으로 설정
    form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article, # 어떤 글을 수정하는지 게시글 pk를 URL로 전달하기 위해 필요
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    if request.method == 'GET':
        form = ArticleForm(instance=article)
        context = {
            'form': form,
        }
        return render(request, 'articles/edit.html', context)
    else:
        # 너 그래서 몇번째 ARTICLE 객체인거야..?
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)


    # 1. 수정할 게시글을 pk를 이용해 조회
    article = Article.objects.get(pk=pk)
    # 2. 기존 Data가 설정된 Form에 사용자의 입력(request.POST)을 채움
    form = ArticleForm(request.POST, instance=article)
    
    # 3. 유효성 검사
    if form.is_valid():
        # 3.1 검사 통과 했을 때
        form.save()
        return redirect('articles:detail', article.pk)
    
    # 3.2 검사 통과 못했을 때
    context = {
        'form': form,
        'article': article, # 어떤 글을 수정하는지 게시글 pk를 URL로 전달하기 위해 필요
    }
    return render(request, 'articles/edit.html', context)


