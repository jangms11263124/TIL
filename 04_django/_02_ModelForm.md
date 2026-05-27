## Form
* `forms.py`

### import 
* `forms.Form`을 상속받아야 함 
* `ModelClassForm(forms.Form)`
  * ex. `ArticleForm(forms.Form)`
<br><br><br>

### template에서 보여줄 form을 지정
* field 변수가 forms의 input 데이터의 name이 됨
```
title = forms.CharField(max_length=10)
content = forms.CharField(widget=forms.Textarea)
```

## ModelForm
```
from django import forms
from .models import Article 

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # include = ('title', )
        # exclude = ('content', )

```
### views에서의 활용

#### Create 
##### `new/`
1. `views.py`에서 `ArticleForm`을 import 해야함
  * `from .forms import ArticleForm`

2. 함수에서 `form`를 생성해서 `context`에 담아서 template에 전송
```
# 1.
from .forms import ArticleForm

# 2. 
def new(request):
  ...
  form = ArticleForm()
  context = {
    'form': form,
  }

```

##### `create/`
1. template에서 전송 받은 `form` 저장
  * method='POST'로 받았으니까 `request.POST`
  * `form = ModelClassForm(request.POST)`

2. 요청 받은 `form`이 유효한지 **유효성 검사**
  * `is_valid()`
  * true이면 `save()`

```
# 1. 사용자의 입력 채우기 
form = ArticleForm(request.POST)
# 2. 
if form.is_valid():
    # 2.1 
    article = form.save()
    return redirect('articles:detail', article.pk)

# 2.2 유효성을 넘어가지 못하면 생성 페이지로 넘겨버리기 with 에러 메시지
context = {
    'form': form,
}
return render(request, 'articles/new.html', context)
```
<br><br><br>

#### Update
##### `edit/`
1. 기존 데이터가 보여줘야함. pk로 조회
  * `article = Article.objects.get(pk=pk)`
2. 비어 있는 form이 아니라 내용을 채워서 보내줘야함 `instance=instance` 
  * `form = ArticleForm(instance=article)`
3. context에 담아서 template에 전송
```
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
```

##### `update/`
1. 기존 데이터 pk로 조회
  * `article = Article.objects.get(pk=pk)`
2. form에 사용자의 입력을 채우기 `request.POST`
  * `form = ArticleForm(request.POST, instance=article)`
3. 채워 넣은 `form`이 유효한지 **유효성 검사**
  * `is_valid()`
  * true이면 `save()`

```
# 1. 수정할 게시글을 pk를 이용해 조회
article = Article.objects.get(pk=article_id)
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
```


