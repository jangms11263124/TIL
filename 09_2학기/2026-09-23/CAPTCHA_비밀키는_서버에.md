# 앱에 CAPTCHA 붙이기: 비밀키는 서버에 둔다

- **Category:** #Security #Flutter #CAPTCHA #API

<br>

## 새롭게 알게 된 것

- 모바일 앱이나 웹 프론트엔드 코드는 사용자 기기에 그대로 내려간다. APK를 풀거나 번들 JS를 열면 안에 넣은 문자열을 볼 수 있어서, **Client Secret 같은 비밀키를 앱에 넣으면 그대로 샌다.**
- 그래서 비밀키가 필요한 외부 API는 **백엔드가 대신 호출**하고, 앱은 우리 백엔드만 부른다. CAPTCHA도 마찬가지다.
  1. 앱 → 백엔드: 보안문자 요청
  2. 백엔드 → CAPTCHA 서비스: 키 발급, 이미지 받기 (비밀키 사용)
  3. 백엔드 → 앱: 키와 이미지 전달
  4. 앱 → 백엔드: 사용자가 입력한 값 제출 → 백엔드가 검증하고 "통과" 기록을 남김
  5. 이후 보호할 API(예: 좌석 조회)는 백엔드가 통과 기록을 확인하고, 없으면 403
- CAPTCHA 종류마다 방식이 다르다.
  - **Google reCAPTCHA v3**: 문제를 보여 주지 않고 행동 점수만 준다. 글자 입력형이 필요하면 맞지 않는다.
  - **hCaptcha**: 그림 고르기 방식이다.
  - **네이버 클라우드 CAPTCHA(Image)**: 그림 속 글자를 읽어 입력하는 방식이다. 공연 예매 사이트에서 흔히 보는 형태다.
- 통과 기록에는 유효 시간이 있다. 보안문자를 **언제 다시 물을지**를 먼저 정해야 한다. 이번에는 예매를 시작할 때 한 번만 묻고, 구역을 바꾸거나 결제하고 돌아올 때는 다시 묻지 않기로 했다. 그러려면 서버의 유효 시간이 예매 도중에 끝나지 않게 맞춰야 한다.

<br>

## 예제 코드

```dart
/// 앱은 우리 백엔드만 부른다. 비밀키는 앱 어디에도 없다.
class CaptchaApi {
  CaptchaApi(this._dio);
  final Dio _dio;

  Future<CaptchaChallenge> issue(int concertId) async {
    final res = await _dio.post('/captcha', data: {'concertId': concertId});
    return CaptchaChallenge.fromJson(res.data); // { key, imageBase64 }
  }

  Future<bool> verify(int concertId, String key, String value) async {
    try {
      await _dio.post('/captcha/verify',
          data: {'concertId': concertId, 'key': key, 'value': value});
      return true;
    } on DioException catch (e) {
      if (e.response?.statusCode == 400) return false; // 틀린 답
      rethrow;
    }
  }
}
```

<br>

## 겪었던 문제 / 트러블슈팅

- **문제 상황**: 보안문자 정답을 입력해도 자꾸 틀렸다고 나왔다.
- **원인**: 정답에 대문자와 소문자가 섞여 있는데(예: `374vK`), 입력칸이 전부 대문자로 바꿔서 보내고 있었다.
- **해결 방안**: 입력칸의 대문자 강제 변환을 빼고 입력한 그대로 보내게 고쳤다.

- **문제 상황**: 보안문자 그림(200×90)이 화면에서 너무 작아 보였다. 새로고침 아이콘을 그림 안에 넣었더니 글자를 가리고 배경에 묻혔다.
- **해결 방안**: 그림은 화면 폭에 맞춰 비율대로 키우고, 새로고침은 그림 아래 오른쪽에 글자 버튼으로 뺐다.

<br>

## 참고 문헌 및 자료

- [reCAPTCHA v3 (Google)](https://developers.google.com/recaptcha/docs/v3)
- [OWASP Mobile Top 10](https://owasp.org/www-project-mobile-top-10/)
