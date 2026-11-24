목표
학습 주제
관계형 데이터베이스에 대한 이해
Django ORM에 대한 이해
1:N 관계에 대한 이해

학습 목표
데이터베이스 개념과 관계형 데이터베이스의 특징에 대해 이해하고 적절히 활용할 수 있다.
Django ORM을 활용하여 Python 코드로 데이터베이스와 상호작용할 수 있다.
1:N 관계를 정의하고 이를 Django 모델에서 구현하는 방법을 이해할 수 있다.
데이터베이스에 적절한 테이블을 구성할 수 있다.

학습 개념
Many to one relationships
한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계를 맺은 형태

ForeignKey
N:1 관계 설정 모델 필드
ForeignKey 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장
# app/models.py

from django.conf import settings​

class Article(models.Model):​
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)​
    ...

역참조​
N:1 관계에서 1 에서 N 을 참조하거나 조회하는 것​
N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만​
1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 이름이 필요​
Model.realtedName_set.all()​


학습 방향
Django Model을 활용한 1:N 관계를 정의 하는 방법을 학습한다.
django 공식 문서를 참고한다.
공식 문서 ) https://docs.djangoproject.com/en/4.2/

문제
할 일 목록 생성 시 작성자가 누구인지 표기하도록 변경하였지만, 여전히 내 할 일 목록만 모아서 보기에는 불편함이 많다. todo 앱에 새로운 페이지를 추가하여, 내가 작성한 todo 목록만 확인할 수 있는 my_page를 생성하도록 하자. 요구 사항을 만족하는 코드를 작성하시오.
요구사항
gitignore를 생성한다.
파이썬 가상 환경에서 프로젝트를 진행한다.
migrate 작업을 진행한다.

my_page 만들기
'todos/mypage/' 경로로 요청이 들어왔을 때, 처리할 수 있는 코드를 작성한다.
'todos/views.py'에서 my_page view 함수를 작성한다.
GET 요청이 들어온 경우, 현재 요청을 보낸 user가 작성한 todo 정보만 조회한다.
user와 Todo의 1:N 관계를 확인하고, user의 역참조 대상 todo 목록을 조회할 수 있어야 한다.
'templates/todos/my_page.html'을 생성한다.
my_page view 함수로 넘겨받은 모든 todo 목록을 화면에 렌더링 한다.

my_page 이동 링크 만들기
'base.html'을 수정하여, 'todos:my_page' 경로로 이동할 수 있는 링크를 작성한다.
로그인되어 있는 경우에만 링크가 렌더링 되어야 한다.
