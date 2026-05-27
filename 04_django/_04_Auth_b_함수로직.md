## Auth 관련 함수 로직
* .
<br><br><br>

### login 
* request의 method에 따라서 login form 생성과 login 정보 확인으로 나눌 수 있음
  * views: GET: login form 보여줌
  * templates: form 보여줌 
  * views: POST: login 정보 확인 

1. `urls.py`
  * `path` 등록
  * `path('login/', views.login, name='login')`
2. `views.py`
  * `login` 함수 생성 후 `request.method` GET/POST 분기
  ```
  def login(request):
    if request.method == 'POST':
      ...
    else:
      ...
  ```
#### 1) views: login GET: 로그인 폼 생성 
* 일반적인 `forms.[앱이름]Form`을 사용하지 않고 장고에서 제공해주는 유저 폼을 사용함 
* `AuthenticationForm` 클래스가 있음
  * `from django.contrib.auth.forms import AuthenticationForm` 

1. 로그인 인증 폼 생성
  * 일반적으로 form을 생성하는 것과 동일하게 작성할 수 있음 
  * `form = AuthenticationForm()`
2. `context`에 담아서 template에 전달
  * `accounts/login.html` or `accounts/form.html` 에다 전달.
  * `context = {'form', form, }`
```
# accounts/views.py
def login(request):
  if request.method == 'POST':
    ...
  else:
    form = AuthenticationForm()
  context = {
    'form', form, 
  }
  return render(request, 'accounts/login.html', context)
```
<br><br><br>

#### 2) templates: form 보여줌 
* templates 폴더 만들고 html만드는 과정은 필기 하지 않았음

* form 태그 생성 
  * action은 accounts의 login으로 
  * method는 POST로 
  * csrf
  * 내부에 form 보여주고
  * 전송 버튼 생성 

```
... 
<form action="{% url 'accounts:login' %}method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="login">
</form>
```

#### 3) login POST: 로그인 정보 확인
1. `request.POST` 로 전송된 정보를 form에 저장
  * `AuthenticationForm` 첫번째 인자는 request, 두번째 인자는 `request.POST`인데 명시적으로 `data=request.POST`로 넣어줘도 ok.
  * `form = AuthenticationForm(request, data=request.POST)`
2. `form` 유효성 검사
  * `저장`하는 것이 아니라 `확인` 하는 것임
3. login 정보 확인 준비
  * 장고에서 제공해준 `AuthenticationForm`을 쓴 것 처럼 로그인도 장고가 제공해주는 `login` 함수를 사용 
  * 하지만 views에 우리가 만든 login 함수랑 겹치니까 `auth_login` 으로 치환
  * `from django.contrib.auth import login as auth_login`
4. `auth_login`의 첫번째 인자로 `request`를 전달하고 두번째 인자로 로그인된 정보(form)을 넣어줘야함
  * 로그인 정보는 `AuthenticationForm`을 사용해서 만든 form 객체에 `get_user()`함수로 호출. 함수 임을 기억하기
  * `auth_login(request, form.get_user())`
  * or 1. `user = form.get_user()` 하고 2. `auth_login(request, user)` 해도 됨 
    * `form.get_user()`를 하나의 변수`user`로 만들어서 `auth_login`의 두번째 인자로 전달
  
5. 일반적으로 template에 전달할때 조회를 해서 보내줬지만 `auth_login`을 하면서 `request`에 확인 유저의 정보가 session에 들어가 있음 
  * context에 담아서 user정보를 넣어줄 필요가 없음 
  * 이후에 가고 싶은 경로로 넣어주면됨 

```
  # accounts/views.py
  ...
  from django.contrib.auth import login as auth_login
  ...
  def login(request):
    if request.method == 'POST':
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        return redirect('articles:index')
    else:
      ...
    ...

```
<br><br><br>

### logout
* session을 삭제해주면 됨 
* 서버의 세션 데이터를 비우고, 클라이언트의 세션 쿠키를 삭제
* logout 버튼이 어딘가에는 있어야겠죠?

1. `urls.py`
  * `path` 등록
  * `path('logout/', views.logout, name='logout')`
  * 전달 받을 user의 이름이나 pk 없음
    * 왜일까? : request정보에 user가 등록되어 있으니
2. `views.py`
  * `login` 함수 생성 
  ```
  def login(request):
    ...
  ```
<br><br><br>

#### 1) views: logout 
* logout 정보 확인 준비
  * 로그아웃도 장고가 제공해주는 `logout` 함수를 사용 
  * 하지만 views에 우리가 만든 logout 함수랑 겹치니까 `auth_logout` 으로 치환
  * `from django.contrib.auth import logout as auth_logout`
* `auth_logout`의 첫번째 인자로 `request`만 전달하면됨. 
  * session에서 정보만 out 시켜주면 되니깐 더이상 할게 없음 
  * return만 가고 싶은 곳을 보냄 
* views는 끝.

```
  # accounts/views.py
  ...
  from django.contrib.auth import logout as auth_logout
  ...
  def logout(request):
    auth_logout(request)
    return redirect('articles:index')
  ...
```
<br><br><br>

#### 2) templates: logout 
* logout.html이 필요한가요? 놉 로그아웃 할 수 있게 버튼만 있으면 되지 않나요?
* GET으로 삭제하면 안되니깐 (url 접근으로도 접근할 수 있으니 방지)
  * POST로 버튼을 생성 
* logout 버튼을 보여줄 template으로 가서 작업 
* form 태그 생성 
  * action은 accounts의 logout으로 
  * method는 POST로 
  * csrf 
  * 버튼 생성 

* 로그아웃 버튼을 만들 템플릿에서 진행 
```
...
<form action="{% url 'accounts:logout' %} method="POST">
  {% csrf_token %}
  <input type="submit" value="logout">
</form>
...
```
<br><br><br>

### signup
* request의 method에 따라서 signup form 생성과 signup 정보 확인으로 나눌 수 있음
  * views: GET: signup form 보여줌
  * templates: form 보여줌 
  * views: POST: signup 정보 확인 

* accounts에서 models(모델)도 `AbstractUser`을 사용한 것 처럼, forms(폼)도 `UserCreateionForm`을 활용 할 수 있음 
  * 이 대체한 커스텀 유저 모델은 기존의 장고 모델이기 때문에 우리가 직접 `다시 만든` `User`를 쓴다는 등록을 해줘야함 
  * 이 과정이 없다면 auth  User가 없다는 에러가 발생함
    * 순서 1. forms.py 파일 없을거니까 새롭게 생성 후 모델 폼 작성 
    * 순서 2. 모델을 meta에 넣어줘야하는데... 문제가 좀 큽니다. 일반적으로 User를 불러올 수 없음
    * 길어질 예정이라 뒤에서 세부적으로 다룸

1. `accounts` 앱 내부에 `forms.py` 생성 
  * `from django.contrib.auth import get_user_model` 필요. 아래에서 더 설명 
  * `from django.contrib.forms import UserCreationForm` 필요. 이것도 아래에서 더 설명
2. `urls.py`
  * `path` 등록
  * `path('signup/', views.signup, name='signup')`
3. `views.py`
  * `signup` 함수 생성 후 `request.method` GET/POST 분기
  ```
  def signup(request):
    if request.method == 'POST':
      ...
    else:
      ...
  ```

#### 1) forms: 
* `UserCreationForm`은 장고에서 제공해주는 회원가입 폼 
  * `from django.contrib.forms`에 있음
* `get_user_model`은 `AbstarctUser`을 상속받은 `User`객체를 `settings.py`에 등록해둔 정보를 활용해서 가져오는 함수 
  * `from django.contrib.auth` 에 있음
* 기존의 `UserCreationForm`을 커스텀 한다는 의미에서 `CustomUserCreationForm`생성 후 `UserCreationForm`은 상속 받아옴
* `Meta` 정보를 넣어줘야하기에 내부에 `class Meta()`를 만들어주고 상속받아온 `UserCreationFomr`에도 `Meta`를 등록해준다는 의미로 `UserCreationForm.Meta`도 상속 받아줘야함
  * `class Meta(UserCreationForm.Meta):`
* 그 이후에 `model` 에 `User` 등록이 아니라 `get_user_model()`을 이건 함수. 함수로 User 모델 등록
```
  # accounts/forms.py
  from django.contrib.auth import get_user_model
  from django.contrib.auth.forms import UserCreationForm

  class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
      model = get_user_model()
  ...
```

#### 2) views: signup GET: 로그인 폼 생성 
* `forms.py`에 만들어둔 회원가입 폼
  * `from .forms import CustomUserCreationForm`


1. 회원가입 폼 생성
  * 일반적으로 form을 생성하는 것과 동일하게 작성할 수 있음 
  * `form = CustomUserCreationForm()`
2. `context`에 담아서 template에 전달
  * `accounts/signup.html` or `accounts/form.html` 에다 전달.
  * `context = {'form', form, }`
```
# accounts/views.py
def signup(request):
  if request.method == 'POST':
    ...
  else:
    form = CustomUserCreationForm()
  context = {
    'form', form, 
  }
  return render(request, 'accounts/signup.html', context)
```
<br><br><br>

#### 3) templates: form 보여줌 
* templates 폴더 만들고 html만드는 과정은 필기 하지 않았음
* form 태그 생성 
  * action은 accounts의 login으로 
  * method는 POST로 
  * csrf
  * 내부에 form 보여주고
  * 전송 버튼 생성 

```
... 
<form action="{% url 'accounts:signup' %}method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="signup">
</form>
```

#### 4) signup POST: 회원가입 정보 저장
1. `request.POST` 로 전송된 정보를 form에 저장
  * 저장 시 `CustomUserCreationForm` 첫번째 인자는 `request`일 필요가 없음! 
  * 바로 `request.POST`
  * `form = CustomUserCreationForm(request.POST)`
2. `form` 유효성 검사
  * `저장`하면 됨.
3. `form.save()`
  * `article = form.save()` 했던거 기억 나시나요? 왜 그랬죠? article 정보를 보낼 detail이 있었기 때문에 
  * `auth_login`처럼 `request`에 user정보(`form.get_user()`)를 바로 전해주는 것이 아니기 때문에 return 하는 경로에 따라서 코드가 달라질 수 있으니 로직을 세우고 진행하시면 됨 
  * 일단 여기서는 `articles의 index`로 갈 거니깐 객체 만들 필요 없음

```
  # accounts/views.py
  ...
  def signup(request):
    if request.method == 'POST':
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('articles:index')
    else:
      ...
    ...
```
<br><br><br>

### delete 
* User 객체를 Delete 만 하면 끝 
* session을 삭제해주면 됨 

1. `urls.py`
  * `path` 등록
  * `path('delete/', views.delete, name='delete')`
  * 전달 받을 user의 이름이나 pk 없음
    * 왜일까? : request정보에 user가 등록되어 있으니
2. `views.py`
  * `delete` 함수 생성 
  ```
  def delete(request):
    ...
  ```
<br><br><br>

#### 1) views: delete 
* `request`에서 `user`정보를 꺼내고 `delete()` 
* `request`에서 유저의 정보가 만료됐다는 것을 인지시켜주기 위해서 `auth_logout`도 함께 진행 
  * 로그아웃을 먼저 하면 안됨 절대 순서를 지키기 1) 회원 정보 삭제, 2)로그아웃
  * 먼저 로그아웃이 진행되면 해당 요청 객체 정보가 없어지면서, 탈퇴에 필요한 유저 정보도 request에 없어지게됨 

```
  # accounts/views.py
  ...
  def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')
  ...
```
<br><br><br>

#### 2) templates: delete 
* delete.html이 필요한가요? 놉 회원 정보를 삭제되는 버튼만 있으면 됨
* GET으로 삭제하면 안되니깐 (url 접근으로도 접근할 수 있으니 방지)
  * POST로 버튼을 생성 
* delete 버튼을 보여줄 template으로 가서 작업 
* form 태그 생성 
  * action은 accounts의 logout으로 
  * method는 POST로 
  * csrf 
  * 버튼 생성 

* 회원삭제 버튼을 만들 템플릿에서 진행 
```
...
<form action="{% url 'accounts:delete' %} method="POST">
  {% csrf_token %}
  <input type="submit" value="delete">
</form>
...
```
<br><br><br>

### update
* request의 method에 따라서 update form 생성과 update 정보 확인으로 나눌 수 있음
  * views: GET: update form 보여줌
  * templates: form 보여줌 
  * views: POST: update 정보 확인 

* login에서 models(모델)도 `UserCustomForm`을 사용한 것 처럼, 회원정보 수정 forms(폼)도 `UserChangeForm`을 활용 할 수 있음 
  * 이 대체한 커스텀 유저 모델은 기존의 장고 모델이기 때문에 우리가 직접 `다시 만든` `User`를 쓴다는 등록을 해줘야함 
  * 이 과정이 없다면 auth  User가 없다는 에러가 발생함 (`get_user_model`)
    * 순서 1. forms.py 파일 없을거니까 새롭게 생성 후 모델 폼 작성 
    * 순서 2. 모델을 meta에 넣어줘야하는데... 문제가 좀 큽니다. 일반적으로 User를 불러올 수 없음
    * 길어질 예정이라 뒤에서 세부적으로 다룸

1. `accounts/forms.py` login에서 이미 만들어놨으니까 새로 만들 필요 없음  
  * `from django.contrib.auth import get_user_model` 필요. 아래에서 더 설명 
  * `from django.contrib.forms import UserChangeForm` 필요. 이것도 아래에서 더 설명
2. `urls.py`
  * `path` 등록
  * `path('update/', views.update, name='update')`
3. `views.py`
  * `update` 함수 생성 후 `request.method` GET/POST 분기
  ```
  def update(request):
    if request.method == 'POST':
      ...
    else:
      ...
  ```

#### 1) forms: 
* `UserChangeForm`은 장고에서 제공해주는 회원 수정 폼 
  * `from django.contrib.forms`에 있음
* `get_user_model`은 `AbstarctUser`을 상속받은 `User`객체를 `settings.py`에 등록해둔 정보를 활용해서 가져오는 함수 
  * `from django.contrib.auth` 에 있음
* 기존의 `UserChangeForm`을 커스텀 한다는 의미에서 `CustomUserChangeForm`생성 후 `UserChangeForm`은 상속 받아옴
* `Meta` 정보를 넣어줘야하기에 내부에 `class Meta()`를 만들어주고 상속받아온 `UserChangeForm`에도 `Meta`를 등록해준다는 의미로 `UserChangeForm.Meta`도 상속 받아줘야함
  * `class Meta(UserChangeForm.Meta):`
* 그 이후에 `model` 에 `User` 등록이 아니라 `get_user_model()`을 이건 함수. 함수로 User 모델 등록
```
  # accounts/forms.py
  from django.contrib.auth import get_user_model
  from django.contrib.auth.forms import UserChangeForm

  class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
      model = get_user_model()
  ...
```

#### 2) views: update GET: 로그인 폼 생성 
* `forms.py`에 만들어둔 회원정보 폼
  * 이미 우리는 `CustomUserCreateionForm`이 있으니깐 추가만 해주면 되겠지
  * `from .forms import CustomUserCreateionForm, CustomUserChangeForm`


1. 회원 정보 수정 폼 생성
  * 일반적으로 form을 생성하는 것과 동일하게 작성할 수 있음 
  * `form = CustomUserChangeForm(...)`
  * `instance` 속성에 `request.user`를 전달 
    * 수정하는 곳에 기존의 정보가 보여야함
  * `form = CustomUserChangeForm(instance=request.user)`
2. `context`에 담아서 template에 전달
  * `accounts/update.html` or `accounts/form.html` 에다 전달.
  * `context = {'form', form, }`
```
# accounts/views.py
def update(request):
  if request.method == 'POST':
    ...
  else:
    form = CustomUserChangeForm(instance=request.user)
  context = {
    'form', form, 
  }
  return render(request, 'accounts/update.html', context)
```

3. `CustomUserChangeForm()` 수정 
  * 일반적으로 전부다 보여주기 때문에 사용자가 입력하지 않아도 되는 정보도 모두 전달됨
  * fields를 수정해야함 
    * tuple로 
      ```
        fields = ('first_name', 'last_name', 'email', )
      ```


4. 회원 정보 수정 폼으로 갈 수 있는 경로 1개 생성 
  `<a href="{% url 'accounts:update' %}">update</a>`
  * 인자 필요 없음. 왜? request 안에 user 정보가 있어서 
  
<br><br><br>

#### 3) templates: form 보여줌 
* templates 폴더 만들고 html만드는 과정은 필기 하지 않았음
* form 태그 생성 
  * action은 accounts의 login으로 
  * method는 POST로 
  * csrf
  * 내부에 form 보여주고
  * 전송 버튼 생성 

```
... 
<form action="{% url 'accounts:update' %}method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="update">
</form>
```

#### 4) signup POST: 수정된 회원 정보 저장
1. `request.POST` 로 전송된 정보를 form에 저장
  * 저장 시 `CustomUserChangeForm` 첫번째 인자 (data) 는 `request.POST`, 두번째 인자 (instance)는 `request.user`
  * `form = CustomUserChangeForm(data=request.POST, instance=request.user)`
2. `form` 유효성 검사
  * `저장`하면 됨.
3. `form.save()`
  * `article = form.save()` 했던거 기억 나시나요? 왜 그랬죠? article 정보를 보낼 detail이 있었기 때문에 
  * `auth_login`처럼 `request`에 user정보(`form.get_user()`)를 바로 전해주는 것이 아니기 때문에 return 하는 경로에 따라서 코드가 달라질 수 있으니 로직을 세우고 진행하시면 됨  (signup과 동일함)
  * 일단 여기서는 `articles의 index`로 갈 거니깐 객체 만들 필요 없음

```
  # accounts/views.py
  ...
  def update(request):
    if request.method == 'POST':
      form = CustomUserChangeForm(data=request.POST, instance=request.user)
      if form.is_valid():
        form.save()
        return redirect('articles:index')
    else:
      ...
    ...
```
<br><br><br>


### password

1. `urls.py` 등록

2. `views.py` 생성. `forms.py`에 추가 x
* PasswordChangeForm 

```
def password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
      user = form.save()
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form': form,
  }
  return render(request, 'accounts/password.html', context)
```



