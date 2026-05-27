## ORM with views
* `urls.py` -> `views.py` -> `templates..` 순서 절대 숙지

## CREATE
*  `new/` -> `create/`
  * `new/` 입력 받을 form 이 필요함
  * `create/` 입력 받은 데이터를 저장하는 로직 
    * POST로 저장


## READE
* `<int:pk>/`: pk 값으로 조회


## DELETE
* `<int:pk>/delete/`: pk 값으로 조회 후 삭제 
    * url로 삭제할 수 있기 때문에 GET이 아니라 POST로 처리해야함 (다음 시간에)

## UPDATE
* `edit/` -> `update/`
  * `edit/` 기존 정보를 가져와함 
  * `update/` 새롭게 업데이트된 정보를 저장하는 로직
