## `request` 필드 

### `is_authenticated` 
* `request`에서 바로 사용못하고 `request` 안에 있는 `user`까지 들어와서 사용할 수 있음 
* 함수 아니고 필드 뒤에 `()` 없어도됨 
* 사용자가 인증되어있는지 여부를 할 수 있는 User Model의 읽기 전용 속성
* 인증 사용자는 True, 비인증 사용자는 False 반환
* 사용자 인증 정도에 따라서 다른 화면을 보여주고 싶을때
<br><br><br>

* 사용법:
  * `django-html`의 `if` 태그 사용
  * `{% if request....... %}`
  * if 말고 else도 있음 
    * is_authenticated의 반환은 True 나 False 둘 중에 하나니깐 
    * if/else만으로 충분
    * else는 없어도됨 선택사항
  * endif 까지 함께 와야지 완벽함
<br><br><br>

* template에서 사용할때 
```
  <!--..../...html -->
  {% if request.user.is_authenticated %}
    ... True 일때 
  {% else %}
    ... False 일때
  {% endif %}
``` 
<br><br><br>

* views.py에서 사용할 때 
```
  # ..../....py
  def login(request):
    if request.user.is_authenticated:
      return redirect('articles:index')
  ...
```
<br><br><br>

#### `request.user.is_authenticated` 사용처 예시
* 로그인과 비로그인 시에 보여줄 nav 메뉴를 구분하고 싶을 때 사용 
  * 로그인한 상태에서만 게시글 생성 버튼을 보여주고 싶을 때, 댓글 달기를 허하고 싶을 때
  * 로그인이 됐을때만 로그아웃 버튼이 보이게 만들고 싶을때 
  * 로그인이 안됐을때는 로그인 혹은 회원가입 버튼을 보여주고 싶을때
  

