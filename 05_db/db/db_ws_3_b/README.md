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

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ...


Migrations
model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법

save(commit=False)​
DB에 저장하지 않고 인스턴스만 반환​
# app/views.py​

def comments_create(request, pk):​
    ...
    if comment_form.is_valid():​
        comment = comment_form.save(commit=False)
        comment.article = article​
        comment.save()​
        return redirect('articles:detail', article.pk)​
    ...

학습 방향
Django Model을 활용한 1:N 관계를 정의 하는 방법을 학습한다.
django 공식 문서를 참고한다.
공식 문서 ) https://docs.djangoproject.com/en/4.2/

문제
diaries 페이지의 각 diary마다 1:N 관계를 형성하고 있는 comment 등을 생성하는 기능을 구현하고자 한다.제시된 코드와 모델 관계 ERD를 참고하여 요구 사항을 만족하는 코드를 작성하시오.
요구사항
gitignore를 생성한다.
파이썬 가상 환경에서 프로젝트를 진행한다.
migrate 작업을 진행한다.

댓글 생성 Form 작성
'diaries/forms.py'에 클래서 CommentForm을 작성한다.
ModelForm으로 구성한다.
content 필드만 포함하여 구성한다. (혹은, diary 필드를 제외할 수도 있다.)

댓글 생성 기능 구현
'diaries/{diary_pk}/comments/' 경로로 POST 요청이 들어왔을 때, 처리할 수 있는 코드를 작성한다.
'diaries/views.py'에 comments_create view 함수를 작성한다.
CommentForm을 사용하여 댓글 생성 코드를 작성한다.
이때, 참조 대상인 Diary 객체의 정보는 경로를 통해 넘겨받은 diary_pk를 활용하여 조회 후 지정한다.
댓글 생성 요청에 대해 항상 'diaries:index' 경로로 redirect 되어야 한다.
유효성 검사를 통과한 경우, 통과하지 못한 경우, GET 요청인 경우 등.

댓글 생성 form 수정
'diaries/views.py'의 index view 함수를 수정한다.
CommentForm을 'templates/diaries/index.html' 에서 렌더링 할 수 있도록 코드를 작성한다.
'templates/diaries/index.html'에서 기존에 작성된 form태그를 수정한다.
요청 경로가 'diaries:comments_create'가 될 수 있도록 action을 수정한다.
이 때, 적절한 diary의 pk를 인자로 가질 수 있도록 작성한다.
요청 방식이 POST 가 될 수 있도록 method를 수정한다.

댓글 생성 요청을 보낸 후, DB를 확인하여 정상적으로 댓글이 생성되었는지 확인한다.
