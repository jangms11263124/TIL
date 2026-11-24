# 서버 시각 문자열과 기기 타임존

- **Category:** #Flutter #Dart #DateTime #Timezone

<br>

## 새롭게 알게 된 것

- 서버(Spring)가 `LocalDateTime`을 그대로 내려 주면 `2026-09-14T20:04:22`처럼 **타임존 표시가 없는 문자열**이 된다.
- Dart의 `DateTime.parse`는 타임존 표시(`Z`나 `+09:00`)가 없는 문자열을 **기기의 로컬 시각**으로 해석한다. 서버는 한국 시각으로 줬는데 기기가 다른 타임존이면 그만큼 어긋난다.
- 반대로 `Z`나 오프셋이 붙어 있으면 UTC 기준의 정확한 순간으로 읽고, `isUtc`도 그에 맞게 정해진다.
- 그래서 "서버가 준 마감 시각 − 지금"으로 남은 시간을 세는 방식은 기기 타임존에 따라 틀릴 수 있다. **응답을 받은 순간부터 흐른 시간**을 재서 정해진 시간(예: 좌석 선점 5분)에서 빼면 타임존과 상관없이 맞다.
- 근본적으로는 서버가 오프셋을 붙여(`+09:00`) 주거나 UTC로 주는 게 맞다.

<br>

## 예제 코드

```dart
// 타임존 표시가 없으면 기기 로컬 시각으로 읽힌다
final a = DateTime.parse('2026-09-14T20:04:22');        // isUtc == false
// 오프셋이 있으면 정확한 순간으로 읽힌다 (내부적으로 UTC)
final b = DateTime.parse('2026-09-14T20:04:22+09:00');  // isUtc == true

// 남은 시간은 "받은 뒤 흐른 시간"으로 센다
class SeatHold {
  SeatHold({required this.receivedAt, this.limit = const Duration(minutes: 5)});

  final DateTime receivedAt; // 응답을 받은 순간 (DateTime.now())
  final Duration limit;

  Duration remainingFrom(DateTime now) {
    final left = limit - now.difference(receivedAt);
    return left.isNegative ? Duration.zero : left;
  }
}
```

<br>

## 겪었던 문제 / 트러블슈팅

- **문제 상황**: 결제 화면의 선점 카운트다운이 `5:00`이 아니라 `544:57`로 찍혔다. 5분에 9시간이 더해진 값이었다.
- **원인**: 에뮬레이터(Pixel 8)의 타임존이 GMT였다. 서버가 한국 시각으로 준 마감 시각을 기기가 GMT로 읽어서 9시간이 어긋났다. 절대 시각(epoch)은 PC와 같았고 타임존만 달랐다.
- **해결 방안**: 남은 시간을 "응답 받은 뒤 흐른 시간" 기준으로 바꿨다. 백엔드에도 시각에 오프셋을 붙여 달라고 요청했다. 실제 사용자 폰도 타임존이 다를 수 있어서 에뮬레이터만의 문제가 아니다.
- **참고**: 에뮬레이터 타임존은 루트 권한 없이 아래 명령으로 바꿀 수 있었다. 바꾼 뒤에는 앱을 다시 띄워야 반영된다.

```bash
adb shell settings put global auto_time_zone 0
adb shell cmd alarm set-timezone Asia/Seoul
```

<br>

## 참고 문헌 및 자료

- [DateTime.parse (Dart API)](https://api.dart.dev/stable/dart-core/DateTime/parse.html)
