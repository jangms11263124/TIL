목표
학습 주제
데이터베이스와 테이블 구조 이해하기
SQL의 역할과 목적 이해하기
SQL 문의 기본 구조 이해하기

학습 목표
SQL의 기본적인 개념과 역할에 대해 이해하고, 데이터베이스와 테이블의 구조를 파악할 수 있다.
SQL을 사용하여 단일 테이블에서 데이터를 조회, 필터링하고 정렬, 제한할 수 있다.

학습 개념
SQL (Structure Query Language)
데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
기초 문법
SQL 키워드는 대소문자를 구분하지 않음. (단, 대문자로 작성하는 것을 권장)
SQL Statement의 끝에는 세미콜론 ( ; )을 작성
SELECT column_name FROM table_name;

DQL (Data Query Language)
데이터 검색 유형
SELECT

ORDER BY
조회 결과의 레코드를 특정 조건에 맞춰 정렬
정렬 기준 column_name에 따라 오름차순 (ASC) 또는 내림차순 (DESC) 정렬
SELECT select_list FROM table_name
ORDER BY 
column_name1 [ASC | DESC],
column_name2 [ASC | DESC],
...;

WHERE
조회 시 특정 검색 조건을 지정
SELECT select_list FROM table_name
WHERE search_condition;

LIKE 
값이 특정 패턴에 일치하는지 확인 (wildcards 와 함께 사용)

Wildcard Characters
% | 0개 이상의 문자열과 일치하는지 확인
_ | 단일 문자와 일치하는지 확인
SELECT select_list FROM table_name
WHERE select_list LIKE '__%a';

LIMIT
조회하는 레코드 수를 제한
SELECT select_list FROM table_name
LIMIT [offset,] row_count;

학습 방향
데이터베이스 스키마와 테이블 구조를 이해한다.
SELECT 문의 사용법을 익힌다.
추가 조건을 위한 적절한 문법의 사용법을 익힌다.

문제
제공된 DB는 sqlite에서 SQL문 연습용으로 제공하는 DataBase이다. DB에는 다수의 테이블을 생성할 수 있는데, 이번에는 그 중 가수의 정보가 담겨있는 artists 테이블을 사용하여 SQL 조회문을 연습하고자 한다. 요구 사항을 만족하는 코드를 작성하시오.
요구사항
data.sql 파일을 생성한다.
SQL문은 생성한 data.sql 파일에서 작성하고 실행한다.
실행 방법
각 요구사항에 적절한 SQL문을 작성한다.
실행하고자 하는 SQL문을 우클릭한다.
Run Selected Query 를 선택하여 실행한다.
결과를 확인한다.


'artists' 테이블에서 모든 아티스트의 정보를 조회하시오.
'artists' 테이블의 모든 데이터의 수를 조회하시오.
'artists' 테이블에서 Name이 'AC/DC' 인 정보를 조회하시오.
'artists' 테이블의 모든 데이터 중, artistid와 Name만 출력하시오.
'artists' 테이블에서 Name이 'Gilberto Gil' 이거나 'Ed Motta' 정보를 조회하시오.
'artists' 테이블에서 모든 정보를 Name 기준으로 내림차순 정렬하여 조회하시오.
'artists' 테이블에서 이름이 'Vinícius' 로 시작하는 정보를 조회하시오. 단, 2개까지만 출력되도록 한다.
'artists' 테이블에서 'ArtistId'가 50번부터 70번까지의 데이터를 조회하여 'ArtistId'만 출력하시오.


실행 결과는 제공 파일 참고
