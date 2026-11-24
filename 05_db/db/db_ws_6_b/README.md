목표
학습 주제
관계형 데이터베이스에 대한 이해
Django ORM에 대한 이해
M:N 관계에 대한 이해

학습 목표
데이터베이스 개념과 관계형 데이터베이스의 특징에 대해 이해하고 적절히 활용할 수 있다.
Django ORM을 활용하여 Python 코드로 데이터베이스와 상호작용할 수 있다.
M:N 관계를 정의하고 이를 Django 모델에서 구현하는 방법을 이해할 수 있다.
데이터베이스에 적절한 테이블을 구성할 수 있다.

학습 개념
Many to many relationships​
한 테이블의 0개 이상의 레코드가 ​다른 테이블의 0개 이상의 레코드와 관련된 경우​
양쪽 모두에서 N:1 관계를 가짐​

ManyToManyField
m:n 관계 설정 모델 필드​
Django에서는 ‘ManyToManyField’로​ 중개모델을 자동으로 생성
# App/models.py​

class Patient(models.Model):​
    doctors = models.ManyToManyField(Doctor)​
    ...

역참조
N:1 관계에서 1 에서 N 을 참조하거나 조회하는 것
N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만
1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 이름이 필요
Model.realtedName_set.all()

역참조 매니저 충돌
1:N 관계를 맺고 있는 두 모델간의 역참조 매니저명이 별도로 설정되어 있지 않은 상황에서
동일한 두 모델이 1:N 혹은 M:N 관계를 추가로 맺고자 할 때 발생 할 수 있는 상황
각 관계에서 같은 이름의 역참조 매니저명을 사용중인 경우
각 관계별 역참조 매니저명을 별도로 지정해 주어야 함

'related_name’ arguments​
역참조시 사용하는 manager name을 변경​
class Patient(models.Model):​
    doctors = models.ManyToManyField(Doctor, related_name='patients')​
    ...

symmetrical
대칭 관계를 설정
N 모델이 M 모델과 관계 형성시, M 모델도 N 모델과 관계를 형성 할 것 인지 결정
# accounts/models.py​

class User(AbstractUser):​
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')​

학습 방향
Django Model을 활용한 M:N 관계를 정의 하는 방법을 학습한다.
django 공식 문서를 참고한다.
공식 문서 ) https://docs.djangoproject.com/en/4.2/

문제
다른 유저의 할 일 목록들을 보다 공감대가 형성이 된다면 해당 유저를 구독해 할 일 목록을 확인할 수 있는 기능을 만들고자 한다. 이를 위한 모델 관계를 우선 형성하고자 하므로, 주어진 ERD를 참고하여 요구사항을 만족하는 코드를 작성하시오.
요구사항
gitignore를 생성한다.
파이썬 가상 환경에서 프로젝트를 진행한다.
migrate 작업을 진행한다.

M:N 모델관계 설정하기
'accounts/models.py'에서 User Class에 MayToManyField를 사용하여 M:N 관계를 형성한다.
자기 자신과 M:N 관계를 형성할 수 있도록 참조할 모델 명을 작성한다.
구독 기능은 내가 상대방을 구독하여도, 상대방은 나를 자동으로 구독하지 않는다.
따라서 비대칭 관계가 형성되도록 설정한다.
컬럼명은 subscription (내가 구독 중인 상대)로 작성하고, 역참조 명은 subscriber (나를 구독 중인 상대)로 작성한다.

구독 버튼 작성하기
'templates/accounts/profile.html'을 수정한다.
현재 로그인한 user와 프로필 페이지 user의 M:N 관계 여부에 따라 버튼이 다르게 렌더링 되어야 한다.
user와 프로필 페이지 user가 아직 M:N 관계를 맺기 전이라면,
'구독' 버튼을 사용자에게 제공한다.
user와 프로필 페이지 user가 이미 M:N 관계를 맺고 있다면,
'구독 취소' 버튼을 사용자에게 제공한다.
단, 자신의 프로필 페이지에서는 구독버튼이 제공되지 않아야 한다.

관리자 페이지 등록
'accounts/admin.py'를 수정하여 관리자 페이지에서 User 정보를 관리할 수 있게 설정한다.
회원가입 기능을 활용하여 관리자 계정 외의 계정을 하나 이상 생성한다.
생성한 데이터와 관리자 계정을 M:N 관계가 될 수 있게 설정한다.

각 기능들이 정상 작동하는지 확인한다.
