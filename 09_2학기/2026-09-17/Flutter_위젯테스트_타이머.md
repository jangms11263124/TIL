# 타이머가 있는 화면의 Flutter 위젯 테스트

- **Category:** #Flutter #Test #WidgetTest
- **Time:** (학습 시간 기입)

<br>

## 새롭게 알게 된 것

- `tester.pump()`는 프레임을 한 번만 그린다. `pump(Duration)`은 그만큼 가짜 시간을 흘린 뒤 그린다.
- `tester.pumpAndSettle()`은 **예약된 프레임이 없을 때까지** 계속 그린다. 그래서 매초 `setState`를 거는 카운트다운처럼 주기 타이머가 있는 화면에서는 끝나지 않고 시간 초과로 실패한다.
- Material 3의 기본 화면 전환(`FadeForwardsPageTransitionsBuilder`)은 300ms가 아니라 **800ms**다. 전환이 끝난 뒤 밀려난 화면이 트리에서 빠지는 데 프레임이 하나 더 든다.
- `Navigator.pushReplacementNamed(result: ...)`는 밀려나는 화면의 `Future`를 **전환이 시작될 때 바로** 완료시킨다. 새 화면이 닫힐 때가 아니다.
- 주기 타이머는 화면이 `dispose`될 때 꼭 꺼야 한다. 안 끄면 테스트 끝에 "A Timer is still pending" 오류가 난다.

<br>

## 예제 코드

```dart
/// 타이머가 있는 화면에서 화면 전환을 끝까지 흘려 보내는 헬퍼.
/// pumpAndSettle 대신 쓴다.
Future<void> pumpRouteTransition(WidgetTester tester) async {
  await tester.pump();                          // 전환 시작
  await tester.pump(const Duration(seconds: 1)); // M3 전환(800ms)보다 길게
  await tester.pump();                          // 밀려난 화면이 트리에서 빠지는 프레임
}

testWidgets('결제가 끝나면 결제 화면이 사라진다', (tester) async {
  await tester.pumpWidget(const TestApp(initialRoute: '/payment'));

  await tester.tap(find.text('결제하기'));
  await pumpRouteTransition(tester);

  expect(find.byType(PaymentScreen), findsNothing);
  expect(find.byType(PaymentDoneScreen), findsOneWidget);
});

testWidgets('카운트다운은 1초마다 줄어든다', (tester) async {
  await tester.pumpWidget(const TestApp(initialRoute: '/payment'));

  expect(find.text('5:00'), findsOneWidget);
  await tester.pump(const Duration(seconds: 1)); // Timer.periodic 한 틱
  expect(find.text('4:59'), findsOneWidget);
});
```

<br>

## 겪었던 문제 / 트러블슈팅

- **문제 상황**: 결제 화면 테스트에서 `pump(Duration(milliseconds: 400))` 뒤에도 `PaymentScreen`이 트리에 남아 있어서 테스트 3개가 깨졌다. `pumpAndSettle()`로 바꾸면 카운트다운 때문에 끝나지 않았다.
- **원인**: M3 기본 전환이 800ms라서 400ms로는 부족했고, 전환이 끝난 다음 프레임에야 이전 화면이 빠졌다.
- **해결 방안**: `pump()` → `pump(1초)` → `pump()` 세 번을 묶은 헬퍼를 만들어 썼다. 주기 타이머가 없는 화면끼리는 그냥 `pumpAndSettle()`이 가장 간단하다. `pump(1초)`는 타이머 한 틱도 같이 돌리니 카운트다운 값이 바뀐다는 점도 감안해야 한다.

<br>

## 참고 문헌 및 자료

- [An introduction to widget testing (Flutter 공식 문서)](https://docs.flutter.dev/cookbook/testing/widget/introduction)
- [WidgetTester.pumpAndSettle (Flutter API)](https://api.flutter.dev/flutter/flutter_test/WidgetTester/pumpAndSettle.html)
