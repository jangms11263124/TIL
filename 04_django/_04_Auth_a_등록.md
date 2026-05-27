## Auth 등록 
* 장고의 유저 DB
* 장고에서 제공해주는 유저가 있음 
* 일반적인 앱에서 모델클래스를 만드는것처럼 만들지 않음
  * 대부분의 양식들을 장고에서 제공해줌
  * 이를 상속 받아서 개발자가 원하는 형식으로 수정해서 사용함
  * 거의 대부분 `django.contrib.auth` 안에 있음 
<br><br><br>

* 장고에서는 유저를 추후에 만들거나 기존의 폼을 수정하는 것을 권장하지 않음 
  * 안되는게 아니라, 추천을 하지 않는 것. 복잡해서 저도 비선호
  * 되도록이면 명세서에 유저 DB를 먼저 만들고 처음부터 진행하고 다른 앱들을 빌딩하는 것을 완전추천
<br><br><br>

* 앱 생성 -> ... -> models.py -> settings.py  순서로 진행됨
<br><br><br>

### Auth 사용 방법
* 보통 `accounts` 이름으로 앱 생성 
* 앱 등록, urls.py 까지는 큰 변동사항이 없음
<br><br><br>

### Auth 모델 생성
* ... -> 1. models.py -> 2. settings.py  순서로 진행됨
  * 이 순서를 잊지마세요!
<br><br><br>

#### 1. models.py 
* 일반적인 모델 등록 처럼 [앱이름]을 PascalCase 형태로 ModelClass를 만들지 않음 
  * `accounts`이지만, `Account`로 만들지 않고, 
  1. `User`로 ModelClass를 만듦
  2. `User`에 장고가 제공해주는 유저를 가져와야함 
    * `AbstractUser` 클래스가 있음
      * `from django.contrib.auth.models import AbstractUser` 
    * *cf*. 기존 models에 있는 `from django.db import models`은 지우지 말고 유지
  3. `AbstractUser`를 `User`가 상속을 받아야함
    * `class User(Abstract)`
  ```
    # acccounts/models.py
    from django.db import models 
    from django.contrib.auth.models import AbstractUser

    class User(AbstractUser):
      pass 
      # pass로 두는 이유는 상속받아온 클래스를 쓸건데, 클래스를 빈 칸으로 둘 수 없으니까 추가
  ```
  

#### 2. settings.py 
* 우리가 `models.py`에 `User`클래스도 만들고 `AbstractUser`도 잘 상속 받았지만,
* 프로젝트 내부에서 (1)어떤 앱에서, (2)어떤 클래스에서 장고 내부에서 제공된 클래스를 가져왔는지 장고는 모름 
* 그래서 우리는 알려줘야함
* `settings.py` 에서 `AUTH_USER_MODEL` 변수를 생성해서 `AbstractUser`을 상속받은 모델클래스를 등록해줘야함 
  * 문자열로 넣어줘야하고 규칙은 
    * `AUTH_USER_MODEL =[앱이름].[클래스이름]` - 대소문자 구분 필수 
      * ex. `AUTH_USER_MODEL= 'accounts.User`
```
  # [프로젝트]/settings.py
  ...
  AUTH_USER_MODEL = 'accounts.User`
  ...
```

### Auth 모델 forms
... TBC