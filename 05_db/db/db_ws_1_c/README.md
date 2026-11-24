목표
학습 주제
시스템을 위한 데이터베이스 설계와 구축
SQL 쿼리 작성 및 활용
학습 목표
데이터베이스에서 SELECT 문을 사용하여 데이터를 조회하는 방법을 습득한다.
WHERE 절과 ORDER BY를 활용한 조건부 조회와 정렬 방법을 습득한다.
집계 함수를 활용하여 데이터를 요약하고 그룹별로 집계할 수 있다.
학습 개념
SQL (Structure Query Language)
﻿﻿﻿데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
기초 문법
SQL 키워드는 대소문자를 구분하지 않음. (단, 대문자로 작성하는 것을 권장)
SQL Statement의 끝에는 세미콜론 ( ; )을 작성
SELECT column_name FROM table_name;

DQL (Data Query Language)
﻿﻿﻿﻿데이터 검색 유형
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


학습 방향
데이터베이스 스키마와 테이블 구조를 이해한다.
SELECT 문의 사용법을 익힌다.
추가 조건을 위한 적절한 문법의 사용법을 익힌다.

문제
좋아하는 노래들만 모아서 보관 할 수 있는 DB를 만들어 보고자 한다. 데이터를 담을 수 있는 테이블 songs을 생성하고, 소수의 데이터를 테이블에 삽입해 두었다. 삽입한 데이터들이 잘 삽입 되었는지 확인하기 위해 몇가지 조회문을 작성해 보고자 한다. 요구 사항을 만족하는 SQL문을 작성하시오.
요구사항
data.sql 파일을 생성한다.
SQL문은 생성한 data.sql 파일에서 작성하고 실행한다.
실행 방법
각 요구사항에 적절한 SQL문을 작성한다.
실행하고자 하는 SQL문을 우클릭한다.
Run Selected Query 를 선택하여 실행한다.
결과를 확인한다.
데이터 그룹화: 테이블 "songs"에서 음악의 장르(genre)를 기준으로 그룹화하는 SQL 문장을 작성하시오.
집계 함수: 테이블 "songs"에서 각 그룹별로 음악의 수를 계산하여 출력하시오.
