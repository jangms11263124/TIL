# FCM 알림 메시지와 데이터 메시지, 그리고 폴링 보완

- **Category:** #Flutter #Firebase #FCM #Push
- **Time:** (학습 시간 기입)

<br>

## 새롭게 알게 된 것

- FCM 메시지는 크게 두 종류다.
  - **알림 메시지(notification)**: `title`, `body`가 있어서 앱이 백그라운드일 때 시스템이 알림을 알아서 띄운다.
  - **데이터 메시지(data)**: 키-값만 담겨 있고 알림을 띄우지 않는다. 받은 앱이 직접 처리한다. 사용자 눈에 보이지 않게 앱 상태만 바꾸고 싶을 때 쓴다("조용한 푸시").
- 앱이 포그라운드일 때 받은 메시지는 `FirebaseMessaging.onMessage` 스트림으로 들어온다. 화면은 이 스트림을 구독해서 필요한 것만 골라 반응하면 된다.
- 데이터 메시지에도 우선순위(`priority: high`)와 유효 시간(TTL)을 줄 수 있다. 의미가 금방 사라지는 신호라면 TTL을 짧게 둔다.
- **푸시는 도착을 보장하지 않는다.** 늦거나 빠질 수 있다. 화면이 열려 있는 동안 꼭 반영돼야 하는 상태라면, 푸시를 받으면 바로 바꾸되 짧은 주기로 서버 상태도 확인하는 **이중 장치**가 안전하다.

<br>

## 예제 코드

```dart
/// 입장 QR 화면: 게이트에서 검표되면 "이미 입장한 QR" 안내로 바꾼다.
class _EntryQrScreenState extends State<EntryQrScreen> {
  StreamSubscription<RemoteMessage>? _pushSub;
  Timer? _poll;
  bool _entered = false;

  @override
  void initState() {
    super.initState();

    // 1) 조용한 푸시: { type: TICKET_ENTERED, ticketId: "123" }
    _pushSub = FirebaseMessaging.onMessage.listen((message) {
      final data = message.data;
      if (data['type'] == 'TICKET_ENTERED' &&
          data['ticketId'] == widget.ticketId.toString()) {
        _markEntered();
      }
    });

    // 2) 보완: 푸시가 늦거나 빠질 때를 대비해 2초마다 상태 확인
    _poll = Timer.periodic(const Duration(seconds: 2), (_) async {
      final ticket = await widget.api.myTicket(widget.ticketId);
      if (ticket.status == TicketStatus.used) _markEntered();
    });
  }

  void _markEntered() {
    if (!mounted || _entered) return;
    _poll?.cancel();
    setState(() => _entered = true);
  }

  @override
  void dispose() {
    _pushSub?.cancel();
    _poll?.cancel(); // 안 끄면 테스트에서 pending timer 오류
    super.dispose();
  }
  // ...
}
```

<br>

## 겪었던 문제 / 트러블슈팅

- **문제 상황**: 게이트에서 QR을 찍어도 관객 폰의 QR 화면은 그대로라서, 입장이 됐는지 바로 알 수 없었다.
- **해결 방안**: 백엔드와 맞춰서 검표가 통과되면 서버가 데이터 메시지(`TICKET_ENTERED`, 알림함 저장 없음, TTL 5분)를 보내게 했다. 앱은 자기 티켓이면 기존 "이미 입장한 QR입니다." 안내를 그대로 재사용했다. 새 화면은 만들지 않았다.
- **헷갈렸던 점**: 처음엔 QR 발급 API가 `409`를 주면 입장한 걸로 보려고 했다. 그런데 양도 등록 중인 티켓도 `409`가 나와서 구분이 안 됐다. 폴링은 내 티켓 조회 API의 상태가 `USED`인지로 판단하게 했다.
- **확인 방법**: 푸시 경로와 폴링 경로를 각각 위젯 테스트로 확인했다(테스트 9개). 한쪽 조건을 일부러 빼 보고 테스트가 실패하는지도 봤다.

<br>

## 참고 문헌 및 자료

- [About FCM messages (Firebase 공식 문서)](https://firebase.google.com/docs/cloud-messaging/concept-options)
- [firebase_messaging (FlutterFire)](https://firebase.flutter.dev/docs/messaging/usage)
