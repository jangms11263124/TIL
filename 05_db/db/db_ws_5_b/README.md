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

'related_name’ arguments​
역참조시 사용하는 manager name을 변경​
class Patient(models.Model):​
    doctors = models.ManyToManyField(Doctor, related_name='patients')​
    ...

학습 방향
Django Model을 활용한 M:N 관계를 정의 하는 방법을 학습한다.
django 공식 문서를 참고한다.
공식 문서 ) https://docs.djangoproject.com/en/4.2/

문제
현재 프로젝트는 User와 Diary의 M:N 관계 형성을 위한 모델 설정과 기능이 없는 버튼만 구현되어 있다. 버튼을 클릭하였을 때, 정상적으로 M:N 관계 형성 기능이 구현되도록 코드를 작성하시오. 요구사항을 참고하여 기능을 구현한다.
요구사항
gitignore를 생성한다.
파이썬 가상 환경에서 프로젝트를 진행한다.
migrate 작업을 진행한다.

요청 경로 설정하기
'diaries/urls.py'를 수정한다.
'/diaries/{diary_pk}/likes/' 경로로 요청이 들어올 때, likes view 함수가 실행되도록 코드를 작성한다.

M:N 관계 기능 구현하기
'diaries/views.py'를 수정한다.
likes view 함수는 POST 요청에 대해 아래와 같은 작업을 수행한다.
인자로 전달받은 diary_pk를 기반으로 특정 diary 정보를 조회한다.
조회한 diary와 요청을 보낸 유저 간의 M:N 관계 형성 여부를 확인한다.
user와 diary가 아직 M:N 관계를 맺기 전이라면,
M:N 관계가 형성되도록 코드를 작성한다.
user와 diary가 이미 M:N 관계를 맺고 있다면,
M:N 관계가 해제되도록 코드를 작성한다.
각 상황에 맞는 기능 수행이 완료되면 'diaries:index' 경로로 redirect 되어야 한다.

요청 버튼 수정하기
'templates/diaries/index.html' 파일을 수정한다.
M:N 관계 요청 버튼이 POST 방식으로 요청할 수 있도록 method를 수정한다.
올바른 경로로 요청을 보낼 수 있도록 action을 수정한다.

각 기능들이 정상 작동하는지 확인한다.
