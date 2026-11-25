# TIL (Today I Learned)

SSAFY 15기에서 배운 것을 정리한 저장소입니다. 1학기는 과목별로, 2학기부터는 날짜별로 씁니다.

<br>

## 폴더

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
| 09 | [2학기](./09_2학기) | 2학기 기록, 날짜별 폴더 (Kafka, LoRA·vLLM, Flutter 테스트, FCM 등) |

<br>

## 작성 규칙

- **파일 이름**: `주제.md` 혹은 `주제_세부내용.md` 형식 (예: `List_Comprehension.md`)
- **작성 원칙**:
  - 강의 내용을 옮기지 않고 내 말로 요약하기
  - 예제 코드 넣기
  - 막혔던 것과 푼 방법 적기
- [TIL 템플릿](./TIL_TEMPLATE.md)
- [프로젝트 회고 템플릿](./PROJECT_TEMPLATE.md)

<br>

## 커밋 메시지

나중에 찾아보기 쉽게 앞에 종류를 붙입니다.

```markdown
docs: README.md 내용 수정
feat: Python 리스트 컴프리헨션 정리 추가
fix: 알고리즘 BFS 문제 풀이 수정 및 추가
```

<br>

---

## 자주 쓰는 Git 명령어

더 자세한 내용은 [git_practice.md](./git_practice.md)에 정리했습니다.

### 저장소 만들고 설정하기
```bash
git init
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 바뀐 것 저장하고 확인하기
```bash
git status
git add .
git commit -m "commit message"
git log --oneline
```
