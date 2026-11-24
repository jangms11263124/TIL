# TIL (Today I Learned)

하루하루 성장하는 개발자가 되기 위해 새롭게 배운 점을 기록하는 저장소입니다.

<br>

## Categories (분류)

현재 학습 중인 과목과 주제별로 분류되어 있습니다. 폴더를 클릭하여 내용을 확인할 수 있습니다.

| 번호 | 폴더명 | 주제 및 내용 |
| :---: | :--- | :--- |
| 00 | [Algorithm](./00_algorithm) | 알고리즘 개념 정리 및 문제 풀이 |
| 01 | [Python](./01_python) | 파이썬 언어 기초 및 심화 문법 |
| 02 | [Web](./02_web) | HTML, CSS 등 웹 프론트엔드 기초 |
| 03 | [AI](./03_ai) | 인공지능 기초 및 활용 |
| 04 | [Django](./04_django) | 웹 프레임워크 (Django) 활용 |
| 05 | [DB](./05_db) | 데이터베이스 개념 및 SQL |
| 06 | [JS](./06_js) | 자바스크립트 문법 및 활용 |
| 07 | [Vue](./07_vue) | Vue.js 기초 및 프론트엔드 프레임워크 |
| 08 | [Project (SSAFY)](./08_project) | SSAFY 과정 중 진행한 실습 및 프로젝트 코드 |
| 09 | [2학기](./09_2학기) | 2학기 학습 기록 — 날짜별 폴더로 정리 (Kafka, Hadoop, A2A 등) |

<br>

## Rules (작성 규칙)

- **파일 이름**: `주제.md` 혹은 `주제_세부내용.md` 형식 (예: `List_Comprehension.md`)
- **작성 원칙**:
  - 나의 언어로 요약해서 적기
  - 가능한 한 예제 코드를 포함하기
  - 트러블슈팅(에러 해결 과정) 기록하기
- [일반 TIL 템플릿 양식 보기](./TIL_TEMPLATE.md)
- [프로젝트 데일리 회고 템플릿 양식 보기](./PROJECT_TEMPLATE.md)

<br>

## Commit Message Convention

나중에 다시 찾아볼 때 한눈에 알아보기 쉽게 통일된 커밋 메시지를 사용합니다.

```markdown
docs: README.md 내용 수정
feat: Python 리스트 컴프리헨션 정리 추가
fix: 알고리즘 BFS 문제 풀이 수정 및 추가
```

<br>

---

## Git Quick Reference (기본 명령어 요약)
상세한 Git 사용법과 동기화 관련 정보는 [git_practice.md](./git_practice.md)를 참고하세요.

### 저장소 초기화 및 설정
```bash
git init
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 변경사항 저장 및 확인
```bash
git status
git add .
git commit -m "commit message"
git log --oneline
```
