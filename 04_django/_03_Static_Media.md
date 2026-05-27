## Static
<br><br><br>

### 프로젝트 활용 
* 프로젝트 루트 경로에서도 `static/` 활용 가능. 
  * 즉, 프로젝트/앱 내부 모두에서 사용은 가능.
    * `templates/` 처럼 프로젝트 루트 경로에서 사용한다면 settings.py 에 가서 경로를 추가해줘야함
  * 우선 프로젝트에서도 `static/` 폴더를 하나 만들어두자.
<br><br><br>


### 경로 추가
* `settings.py`
  * `STATICFILES_DIRS` 변수를 생성해서 `[]` 안에 경로를 추가
  * 기존에 있는 `STATIC_URL = 'static/'`는 유지
  * remind: 프로젝트 루트에 있는 `static/`을 활용하기 위해서 등록해주는 경로

```
  # [프로젝트 이름]/settings.py 
  ...
  STATIC_URL = 'static/'
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  
```
<br><br><br>


### 앱에서 활용
* 앱 안에서 `static/` 폴더를 직접 생성
  * static/ 안에서 css/, js/, imgs/ .. 추가 
* template 에서 활용할려면
  * `/static` 경로를 모든 경로 앞에 추가해야함
    * `static/` 아님... 
    * 장고(Django)가 [앱이름] 까지만 경로를 찾아가니 우리가 `/` 를 넣어줘서 그 이후부터 찾아갈 수 있게 도와줘야함
    * ex. `"/static/stylesheets/style.css"`
  * template extends 다음에 `{% load static %}` 을 넣어줌
  1. 기본 세팅
    ```
    {% extends 'base.html' %}
    {% load static%}
    ... 
    ```
  2. 활용법 
    * 경로를 넣어야하는 곳에서 static 태그를 써서 문자열 안에 경로를 추가 
    * `{% static "파일경로와 파일이름" %}`
      * ex. `<link rel="stylesheet" href="{% static "stylesheets/style.css" %}">`
        * 동일: `<link rel="stylesheet" href="/static/stylesheets/style.css">`
<br><br><br>


## Media
* 이미지나 파일 등을 올리고 싶을때 사용
<br><br><br>

### 경로 추가1 (프로젝트 settings.py)
* `프로젝트/settings.py`
  * `MEDIA_ROOT` 변수를 생성해서 `BASE_DIR / 'media'`경로를 추가
  * `STATIC_URL`과 다름! [] 안에 넣어주는거 아님~~
    * ex. `MEDIA_ROOT = BASE_DIR / 'media'`
  * `MEDIA_URL` 변수를 media 폴더를 찾을 수 있도록 도와줌 
    * ex. `MEDIA_URL = 'media/'`
  생성해서  = `'static/'`는 유지
  * remind: 프로젝트 루트에 있는 `static/`을 활용하기 위해서 등록해주는 경로

```
  # [프로젝트 이름]/settings.py 
  ...
  MEDIA_ROOT = BASE_DIR / 'media'
  MEDIA_URL = 'media/'
```
<br><br><br>

### 경로 추가2 (프로젝트 urls.py에)
* `프로젝트/urls.py`
  * remind: 앱에 하시면 안됩니다.

* 권장: 장고mdn 에서 찾아서 추가해보기 
  * django media라고 하면 잘 안나옴 
  * django static-files mdn 검색하면 아래의 링크가 나올거에요!!!! 
    * 참고문서: https://docs.djangoproject.com/en/6.0/howto/static-files/
  * 대놓고 알려주는 cheating sheets.. 
  ```
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

* 따라해보기: 
  1. `프로젝트/urls.py` 안에서 라이브러리 import
    * `from django.conf import settings` settings 추가해주고
    * `from django.conf.urls.static import static` static을 추가해주기
  2. urlpatterns에 static을 추가 
    * `+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`
  * 완성본:
    ```
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        ....
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ``` 
<br><br><br>

### 모델클래스에 등록
* models.py
* 모델클래스에 필드 추가 
* `models.ImageField()`
  * argument에 `upload_to='images/` 경로 추가
  * argument에 `blank='True`파일이 안들어왔을때도 허하기
```
  image = models.ImageField(upload_to='images/')
```

* 모두 다 했으면 이제 `makemigrations` -> `migrate` 진행
<br><br><br>

### 라이브러리 설치
* `pip install pillow` 
* 새롭게 라이브러리 추가했으니, pip requirements.txt 업데이트 
   * ex. `pip freeze > requirements.txt`
<br><br><br>

### template에서 받아온 file 데이터 처리하기
<br><br><br>

#### templates/
* 데이터를 views로 전송하기
  * form 태그에서 파일을 보내겠다는 속성 추가 
    * `enctype="multipart/form-data"`
    ```
      <form action="..." method="..." enctype="multipart/form-data">
          ...
      </form>

    ```
  * 참고문서: https://docs.djangoproject.com/en/6.0/topics/http/file-uploads/

* 데이터를 templates에 보여주기
  * file이 있는 column을 조회만 해오면 안보임 
  * `.url` 이라는 필드 속성을 추가해줘야함 `model.colum.url` 
    * ex. `article.image.url` 
  * 이미지는 `img` 태그의 `src` 속성에 넣어주면 됨 
    * ex. `<img src="{{ article.image.url }}" alt="{{ article.image }}>`
      * `article.image.url` 과 `article.image`는 다름 
      * `article.image` : 파일 객체 
      * `article.image.url` : 브라우저에서 접근 가능한 경로 (문자열 URL)
<br><br><br>


#### views.py
* form에 등록시, `request.FILES`도 함께 전달 
  * `form = ModelForm(request.POST, request.FILES)`