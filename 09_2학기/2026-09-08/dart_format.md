# dart format은 고친 파일에만 돌리기

- **Category:** #Flutter #Dart #Git #협업

<br>

## 새롭게 알게 된 것

- `dart format`은 Dart SDK 버전에 따라 결과가 달라진다. Dart 3.7부터 포맷터 스타일이 바뀌어서(이른바 "tall style"), 인자 목록을 세로로 펼치는 방식이 달라졌다.
- 그래서 팀원마다 SDK 버전이 다르면, 같은 파일이라도 누가 포맷을 돌렸느냐에 따라 줄바꿈이 바뀐다. 폴더 전체에 포맷을 돌리면 **내가 손대지 않은 파일까지 변경 목록에 올라온다.**
- 기능 MR에 포맷 변경이 섞이면 리뷰어가 진짜 바뀐 줄을 찾기 어렵다. 포맷을 통일하고 싶으면 팀이 합의한 뒤 **포맷만 바꾸는 커밋을 따로** 만드는 게 맞다.

<br>

## 예제 코드

```bash
# 하지 말 것: 폴더 전체 포맷
dart format lib test

# 할 것: 이번에 고친 파일만 지정
dart format lib/features/auth/screens/login_screen.dart test/features/auth/login_screen_test.dart

# 지금 브랜치에서 바뀐 dart 파일만 골라서 포맷 (목록이 비었는지 먼저 확인)
files=$(git diff --name-only --diff-filter=AM origin/develop -- '*.dart')
[ -n "$files" ] && echo "$files" | xargs -n 60 dart format

# 돌린 뒤 내가 의도한 파일만 바뀌었는지 확인
git status --short
```

<br>

## 겪었던 문제 / 트러블슈팅

- **문제 상황**: 로그인 화면 작업 중에 무심코 `dart format lib test`를 돌렸더니, 변경 목록에 36개 파일이 올라왔다. 그중 28개는 내가 건드리지도 않은 예매·홈·결제 화면과 테스트였다. 그대로 커밋했으면 MR에 상관없는 포맷 변경이 290줄 섞일 뻔했다.
- **해결 방안**: `git checkout -- <경로>`로 내가 안 고친 파일을 되돌리고, 그 뒤로는 고친 파일 경로만 지정해서 포맷했다.

- **문제 상황**: 파일 목록을 변수로 넘기는 스크립트에서 목록이 비어 있으면 `dart format`이 **현재 폴더 전체**를 포맷했다. 반대로 파일이 270개쯤 넘어가면 Windows에서 "입력 줄이 너무 깁니다" 오류가 났다.
- **해결 방안**: 목록이 비었는지 먼저 확인하고, 파일이 많을 때는 `xargs -n 60`으로 나눠서 넘겼다.

<br>

## 참고 문헌 및 자료

- [dart format (Dart 공식 문서)](https://dart.dev/tools/dart-format)
