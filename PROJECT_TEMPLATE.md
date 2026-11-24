# [프로젝트명] 데일리 회고 (예: 2024-03-21)

- **Category:** #Project #Troubleshooting #Feedback
- **Time:** (학습 및 개발에 소요된 시간)

<br>

## 오늘 진행한 작업 (What I Did)

- 소셜 로그인(Kakao) API 연동 테스트
- 메인 페이지 UI 레이아웃 초안 작성

<br>

## 컨설턴트/멘토 피드백 (Feedback)

*(미팅이나 멘토링을 통해 들은 조언, 방향성, 수정해야 할 사항들을 기록합니다.)*

- UI 구성 시 모바일 환경을 먼저 고려할 것 (Mobile First)
- API Key와 같은 민감한 정보는 절대 Github에 올리지 말고 `.env` 파일로 분리할 것!

<br>

## 새롭게 배운 점 & 트러블슈팅 (Learnings & Troubleshooting)

*(프로젝트를 진행하며 부딪힌 에러나 새롭게 알게 된 기술적 지식을 기록합니다. 기존 TIL과 가장 유사한 부분입니다.)*

### 1. `.env` 환경 변수 설정
- **문제 상황**: Django에서 `settings.py`에 API Key를 하드코딩하면 보안에 취약함.
- **해결 방안**: `django-environ` 라이브러리를 사용해 `.env` 파일로 분리함. `.gitignore`에 `.env` 추가 필수.

### 2. (기타 알게된 팁이나 기술)
- (내용)

<br>

## 내일 할 일 (To-Do)

- [ ] 카카오 로그인 유저 DB 저장 로직 구현
- [ ] 메인 페이지 컴포넌트 CSS 스타일링
