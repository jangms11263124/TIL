목표
학습 주제
시스템을 위한 데이터베이스 설계와 구축
SQL 쿼리 작성 및 활용

학습 목표
데이터베이스 스키마를 구성하는 방법과 데이터베이스 테이블을 생성하는 방법을 이해한다.
데이터를 삽입, 수정, 삭제하는 방법을 숙지한다.
데이터베이스에서 SELECT 문을 사용하여 데이터를 조회하는 방법을 습득한다.

학습 개념
SQL (Structure Query Language)데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
기초 문법
SQL 키워드는 대소문자를 구분하지 않음. (단, 대문자로 작성하는 것을 권장)
SQL Statement의 끝에는 세미콜론 ( ; )을 작성
SELECT column_name FROM table_name;

DDL (Data Definition Language)
데이터의 기본 구조 및 형식을 변경
CREATE, DROP, ALTER

CREATE TABLE
테이블 생성 명령어
각 필드에 적용할 데이터 타입 작성
테이블 및 필드에 대한 제약조건 작성
CREATE TABLE table_name (​
  column_1 data_type constraints,​
  column_2 data_type constraints,​
  ...,​
);​

DML (Data Manipulation Language)
데이터의 조작을 수행
INSERT, UPDATE, DELETE

INSERT
테이블 레코드 삽입 명령어
INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록 작성​
VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성​
INSERT INTO table_name (c1, c2, ...)​
VALUES (v1, v2, ...);​

UPDATE
테이블 레코드 수정 명령어
SET 절 다음에 수정 할 필드와 새 값을 지정​
WHERE 절에서 수정 할 레코드를 지정하는 조건 작성
WHERE 절을 작성하지 않으면 모든 레코드를 수정​
UPDATE table_name​
SET column_name = expression,​
[WHERE condition];​

학습 방향
데이터베이스 스키마와 테이블 구조를 이해한다.
SELECT 문의 사용법을 익힌다.
테이블을 생성하고 데이터를 수정하는 방법을 익힌다.

문제
좋아하는 노래들만 모아서 보관 할 수 있는 DB를 만들어 보고자 한다. 테이블 구성은 미리 기획하여 이미지로 만들어 두었다. 이미지를 참고하여 songs 테이블을 생성하고, 데이터를 삽입, 수정 할 수 있는 SQL문을 작성하시오.
요구사항
songs.sqlite3 파일을 생성한다.
data.sql 파일을 생성한다.
SQL문은 생성한 data.sql 파일에서 작성하고 실행한다.
실행 방법
각 요구사항에 적절한 SQL문을 작성한다.
실행하고자 하는 SQL문을 우클릭한다.
Run Selected Query 를 선택하여 실행한다.
결과를 확인한다.

"songs" 테이블을 생성한다.
"songs" 테이블에 추가할 필드들을 아래와 같다.
id: 음악의 고유 식별자 (INTEGER, PRIMARY KEY)
title: 음악의 제목 (TEXT)
artist: 음악의 아티스트 (TEXT)
album: 음악의 앨범 (TEXT)
genre: 음악의 장르 (TEXT)
duration: 음악의 재생 시간 (INTEGER)

데이터 삽입: 테이블 "songs"에 적어도 5개의 음악 데이터를 삽입하는 SQL 문장을 작성하시오.
데이터 업데이트: 테이블 "songs"에서 특정 음악의 제목(title)을 업데이트하는 SQL 문장을 작성하시오.