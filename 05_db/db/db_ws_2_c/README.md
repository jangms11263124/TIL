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
GROUP BY
집계 함수와 함께 사용하여 레코드를 그룹화하고 요약본을 생성​
aggregation Funtions
값에 대한 계산을 수행하고 단일한 값을 반환하는 함수​
AVG, MAX, MIN, COUNT 등
SELECT ​c1, c2,..., cn, aggregate_function(ci)​
FROM​ table_name​
GROUP BY ​ c1, c2, ..., cn;​
학습 방향
데이터베이스 스키마와 테이블 구조를 이해한다.
SELECT 문의 사용법을 익힌다.
추가 조건을 위한 적절한 문법의 사용법을 익힌다.

문제
제공된 DB는 sqlite에서 SQL문 연습용으로 제공하는 DataBase이다. DB에는 다수의 테이블을 생성할 수 있는데, 이번에는 그 중 송장 정보가 담겨있는 invoices 테이블을 사용하여 SQL 조회문을 연습하고자 한다. 요구 사항을 만족하는 코드를 작성하시오.
요구사항
data.sql 파일을 생성한다.
SQL문은 생성한 data.sql 파일에서 작성하고 실행한다.
실행 방법
각 요구사항에 적절한 SQL문을 작성한다.
실행하고자 하는 SQL문을 우클릭한다.
Run Selected Query 를 선택하여 실행한다.
결과를 확인한다.

sql 파일을 생성하고 각 요구 사항을 만족하는 코드를 작성하고 실행 결과를 확인하시오.
BillingState 에 저장되어 있는 데이터 값은 주 이름의 약자로 저장되어 있음을 주의한다. 
"BillingCountry"를 기준으로 그룹화하고, 각 나라별 총판매액을 계산하여 조회하시오.
"InvoiceDate"를 연도별로 그룹화하고, 각 연도별 총판매액을 계산하여 조회하시오.
 "BillingCountry"이 'USA'이고 "InvoiceDate"가 2010년 01월 01 이후인 레코드를 "BillingState"를 기준으로 그룹화하고, 각 주별로 총 주문 금액을 계산하여 조회하시오. 
"BillingCountry"이 'Germany'이거나 "BillingCountry"이 'France'인 레코드를 "BillingCountry"를 기준으로 그룹화하고, 각 나라별로 최대 주문 금액을 계산하여 조회하시오.