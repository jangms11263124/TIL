## 가상환경 만들기
* `python -m venv venv`: 가상환경 생성
* `source venv/Scripts/activate`: 가상환경 활성화 
* `pip list`: pip 설치 목록 확인
* pip list 설치
 * `pip freeze > requirements.txt`: `requirements.txt` 파일로 pip 패키지 리스트 텍스트로 저장 
 * `pip install -r requirements.txt`: 제공된 pip 패키지 리스트 한번에 설치 (가상환경 키고 진행 추천) 
* venv 관리
 * `.gitignore` 파일에 `venv/` 추가하기
  * 파일의 이름은 없음. 확장자만 gitignore입니다.
 * `gitignore.io` 적극 활용하기 
 * `touch .gitignore`: gitignore 파일 생성
<br><br><br>

## 장고 프로젝트 생성
* `pip install django`: 장고 pip 패키지 설치
* `django-admin startproject [프로젝트 이름]`: 대괄호는 사용하지 않음. 사용자 입력. 
  * [프로젝트 이름] 으로 폴더 생성됨.
 * ex. `django-admin startproject projectname` 
 * `cd [프로젝트 이름]` 으로 폴더 들어가서 장고 작업을 해야함
 * 이후에 `.` 추가하면 현재 있는 폴더 자체가 프로젝트가 됨 
  * ex. `django-admin startproject projectname .` 
  * 새롭게 폴더가 생기지 않아서 바로 장고 작업 가능
<br><br><br>

## 장고 프로젝트 실행
* `python manage.py runserver`: 장고 프로젝트 실행
  * `ls -al`로 현재 폴더 경로에 `manage.py`가 있는지 확인
  * 안보이면 `cd [폴더 이름]`으로 폴더 이동
<br><br><br>

### 앱 생성
* `python manage.py startapp [앱 이름]`: 앱 생성
  * 앱 이름은 복수로 만드는 것을 권장 (ex. articles, accounts, pages)
<br><br><br>

### 앱 등록
* `settings.py` 에서 `INSTALLED_APPS=[]` 안에 `'[앱 이름]',` 추가 
```
# settings.py
INSTALLED_APPS = [
  'articles',
  'accounts',
  'pages', ...
]
```

1. 프로젝트의 `urls.py` 에서 새로 만든 앱의 url 등록
  * `from django.urls import include`
  * `path('[앱 이름]/', include('[앱 이름].urls')), `
    * ex. `path('articles/', include('articles.urls')), `


2. 앱의 `urls.py` 에서 url 등록
  * 주의: url을 생성하면 views에 함수를 등록해야하기때문에 views -> template까지 완성이 되어야지 `makemigrations`가 된다. 
  * 모델 생성 이후에 앱 내의 `urls.py`를 채우는 것을 권장.
  * 없음. 앱의 폴더에서 `urls.py` 생성. 
  ```
  # [앱 이름]/urls.py

  from django.urls import path
  from . import views

  app_name = '[앱 이름]'
  urlpatterns = [
    # 우선 공백으로 나중에 urls 파일 만들면 index 경로추가
    # path('', 'vies.index', name='index'),
  ]
  ```
  * `app_name`: 앱 이름 등록

  * 
  ```
  # [앱 이름]/ views.py

  def index(request):
    context = {
      'name': 'jihye',
    }
    return render
  
  ```
<br><br><br>


## 모델 생성
1. 앱의 `models.py` 에서 Model 등록
  
2. Model 클래스 작성 
* `from django.db import models` 라이브러리를 가져오고
* 반드시 Model 클래스는 `models.Model`을 상속을 받아야함. 절대 잊지 않기~~ 
  ```
  # [앱이름]/models.py

  from django.db import models

  class PascalCase로모델이름만들기(models.Model):
    # 필드 작성란
    ...
  ```

3. field 추가 
  ```
  # [앱이름]/models.py

  from django.db import models

  class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    ....
  ```
<br><br><br>


### 모델 등록
* 스키마 모델 생성 (makemigration**s**): 
  * `python manage.py makemigrations`
  * 테이블 생성확인
  * 1번만 하면 됨
  
* 변경된 내용 반영 (migrate)
  * `python manage.py migrate` 
  * 모델 구조 변경 될때마다 진행하기

* 스키마 확인 (showmigration**s**)
  * `python manage.py showmigrations`
<br><br><br>

### 필드 유의사항
* `auto_now`: 수시로
  * ex. `updated_at = models.DateTimeField(auto_now=True)`
* `auto_now_add`: 처음 생성시
  * ex. `created_at = models.DateTimeField(auto_now_add=True)`
<br><br><br>

## 관리자
* 
1. 관리자 계정 생성 `python manage.py createsuperuser` 
2. `[앱이름]/admin.py`에 모델 등록 
  * `admin.site.register([모델 이름])`
```
# [앱이름]/admin.py

from django.contrib import admin
from .model import [모델 이름]

admin.site.register([모델 이름])
```
<br><br><br>

## ORM
* Object - Relational - Mapping 
* Django과 DB의 상호 번역기
### 사용 방법
* DB를 생성 후 패키지 설치하고 진행
<br><br><br>

### 설치
* 패키지 설치: `pip install ipython` 
* shell 접근: `python manage.py shell`
  * `python manage.py shell -v 2`: 일반적인 정보보다 더 맣은 진행 상황을 보여달라는 요청
  * 기본값은 1
* shell 끄기: shell terminal에서 `exit()`
<br><br><br>

### Queryset API
#### `ModelClass.Manager.QuerysetAPI`
* `Article.objects.all()`
<br><br><br>

#### 준비사항
* ModelClass로부터 instance 생성
  * `instance = ModelClass()`
    * ex. `article = Article()`
<br><br><br>

#### Create
* instance의 field에 값 할당
  * `instance.field = 'value'`
    * ex. `article.title = '자기소개'`
    * ex. `article.content = '나는 구미 2반이야'`

* 한꺼번에 field의 값을 지정 + instance 생성과 동시
  * `instance = ModelClass(field1='value1' ...)`
    * ex. `article = Article(title='싸피', content='15기')`

* `save()`: 저장하지 않으면 DB에 값을 저장하지 못함
  * `instance.save()`
    * ex. `article.save()`

* `create()`: 저장하지 않아도 바로 데이터 생성
  * `ModelClass.Manager.create(field1='value1' ...)`
    * ex. `Article.objects.create(title='싸피', content='15기')`
<br><br><br>

#### Read
* `all()`: ModelClass에 있는 모든 정보 조회
  * `ModelClass.Manager.all()`
    * ex. `Article.objects.all()`

* `get(field='value')`: ModelClass에서 특정 1개의 조건으로 **객체** 반환
  * `ModelClass.Manager.get(field='value')`
    * ex. `Article.objects.get(pk=1)`
    * ex. `Article.objects.get(title='자기소개')`
  * 객체를 반환할때 해당 조건이 여러개라면 `MultipleObjectReturned`, 없으면 `DoesNotExist` 예외를 발생함
  * 따라서 `pk`와 같이 고유성을 보장하는 정보에서만 조회하는 것을 권장

* `filter(filed='value)`: ModelClass에서 특정 1개의 조건으로 QuerySet 반환
  * `ModelClass.Manager.filter(field='value')`
    * ex. `Article.objects.filter(title='자기소개')`
  * `get()`과 다르게 여러개가 조회가 가능해서 일반적으로 더 많이 쓰임

* instance에서 field 바로 조회 가능
  * `instance.field`
    * ex. `article.title`
    * ex. `article.content`
<br><br><br>

#### Update
1. 수정할 instance 조회
  * `instance = ModelClass.Manager.get(field=value)`
    * ex.`article = Article.objects.get(pk=1)`
2. instance 정보 변경
  * `instance.field='new value'`
    * ex.`article.title='new'`
3. 저장
  * `instance.save()`
    * ex.`article.save()`
<br><br><br>

#### Delete
1. 삭제할 instance 조회
  * `instance = ModelClass.Manager.get(field=value)`
    * ex.`article = Article.objects.get(pk=1)`
2. `delete()` 삭제
  * `instance.delete()`
    * ex.`article.delete()`

<br><br><br>

