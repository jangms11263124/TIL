# adb 무선 디버깅으로 실기기 연결하기

- **Category:** #Android #Flutter #adb #Debugging

<br>

## 새롭게 알게 된 것

- `adb`는 USB 말고 **Wi-Fi(TCP/IP)** 로도 기기에 붙을 수 있다. PC와 폰이 같은 네트워크에 있으면 된다.
- 방법은 두 가지다.
  1. **USB가 꽂혀 있을 때**: `adb tcpip 5555`로 기기의 adb를 TCP 모드로 바꾸고 `adb connect <폰IP>:5555`로 붙는다. 페어링 코드가 필요 없다. 연결되면 USB를 빼도 된다.
  2. **USB 없이 처음부터 (Android 11 이상)**: 개발자 옵션 → 무선 디버깅 → "페어링 코드로 기기 페어링"에서 나오는 IP·포트·6자리 코드로 `adb pair` 한 뒤, 무선 디버깅 화면에 표시된 **접속 포트**로 `adb connect` 한다. 페어링 포트와 접속 포트가 다르다.
- `tcpip` 모드는 **폰을 재부팅하면 풀린다.** IP가 바뀌어도 끊긴다.
- Flutter는 `flutter devices`에 `<IP>:5555`로 잡히고, `flutter run -d <IP>:5555`로 그대로 올릴 수 있다.

<br>

## 예제 코드

```bash
# Android SDK의 adb가 PATH에 없으면 전체 경로로 부른다 (Windows Git Bash 기준)
ADB="$LOCALAPPDATA/Android/Sdk/platform-tools/adb.exe"

# 1) USB로 연결된 상태에서 폰의 Wi-Fi IP 확인
IP=$("$ADB" shell ip -f inet addr show wlan0 | grep -oE "inet [0-9.]+" | awk '{print $2}')

# 2) TCP 모드로 바꾸고 무선으로 연결
"$ADB" tcpip 5555
"$ADB" connect "$IP:5555"

# 3) USB를 빼고 무선으로 실행
flutter run -d "$IP:5555"

# USB 없이 처음 붙일 때 (무선 디버깅 화면의 값 사용)
"$ADB" pair <페어링IP>:<페어링포트>   # 6자리 코드 입력
"$ADB" connect <IP>:<접속포트>
```

<br>

## 겪었던 문제 / 트러블슈팅

- **문제 상황**: 폰을 USB로 연결해 `flutter run`을 띄워 두면, 앱 화면이 내려갈 때마다 `Lost connection to device`로 세션이 끊겼다. 좌석 선택 화면을 고치던 날 다섯 번 넘게 반복됐다.
- **해결 방안**: USB가 꽂혀 있는 동안 `adb tcpip 5555` → `adb connect`로 무선 연결로 바꾸고 USB를 뺐다. 그 뒤로는 끊기지 않았다.
- **추가로 알게 된 것**: 폰 Wi-Fi가 꺼져 있으면 `wlan0`에 IP가 안 나온다. PC의 모바일 핫스팟에 폰을 붙여도 되는데, 이때 폰에서 로컬 백엔드를 부르려면 `localhost`가 아니라 **핫스팟 쪽 PC IP**를 써야 한다.

<br>

## 참고 문헌 및 자료

- [Android Debug Bridge (adb) - 무선 연결 (Android Developers)](https://developer.android.com/tools/adb)
