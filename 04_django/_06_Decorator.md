## Decorator 
* `@`으로 시작되는 것들
* 함수나 클래스 위에 붙여서 함께 사용 
* 함수나 클래스에서 접근, 사용 등을 제한하거나 넓히고 싶을때 사용 

### `@login_required`
* `views.py`에서 보통은 사용함
* `login_required` 는 `from django.contrib.auth.decorators` 안에 있는 함수
* `from django.contrib.auth.decorators import login_required`로 사용 준비 
<br><br><br>

* 보통 어디에 쓰나?
  * 로그인을 해야지만 사용할 수 있는 기능들에 추가해줌
  * ex. 글 생성, 글 삭제, 글 수정.. etc

```
  # [앱이름]/views.py

  @login_required
  def create(reqest):
    ...

  @login_required
  def update(reqest, ...):
    ...

  @login_required
  def delete(reqest, ...):
    ...
```