# 글자 명도 대비 기준 (WCAG)

- **Category:** #UI #접근성 #WCAG #Design
- **Time:** (학습 시간 기입)

<br>

## 새롭게 알게 된 것

- WCAG는 글자와 배경의 **명도 대비(contrast ratio)** 에 최소 기준을 둔다. 대비는 1:1(같은 색)부터 21:1(흰색과 검정)까지다.
  - **AA 기준**: 일반 글자는 **4.5:1 이상**, 큰 글자(18pt 이상, 굵으면 14pt 이상)는 **3:1 이상**
  - **AAA 기준**: 일반 글자 7:1, 큰 글자 4.5:1
  - 아이콘이나 입력칸 테두리 같은 UI 요소는 3:1 이상
- 대비는 두 색의 **상대 휘도**(relative luminance)로 계산한다. `(L1 + 0.05) / (L2 + 0.05)`이고 L1이 밝은 쪽이다.
- 브랜드 색이 진한 초록이라도, 그 위에 흰 글자를 작게 올리면 기준에 못 미칠 수 있다. 색을 정할 때 "예쁜가"와 별개로 숫자를 확인해야 한다.
- 읽음/안 읽음처럼 상태를 **색만으로** 구분하면 색약 사용자는 알아보기 어렵다. 굵기나 점 같은 다른 단서를 같이 쓰는 게 좋다.

<br>

## 예제 코드

```dart
import 'dart:math';
import 'package:flutter/material.dart';

/// WCAG 명도 대비 계산. Flutter Color.computeLuminance()가 상대 휘도를 준다.
double contrastRatio(Color a, Color b) {
  final la = a.computeLuminance();
  final lb = b.computeLuminance();
  final lighter = max(la, lb);
  final darker = min(la, lb);
  return (lighter + 0.05) / (darker + 0.05);
}

void main() {
  final ratio = contrastRatio(Colors.white, const Color(0xFF2E9E6B));
  print(ratio.toStringAsFixed(2));          // 4.5 미만이면 작은 본문 글자로는 부족
  print(ratio >= 4.5 ? 'AA 통과' : 'AA 미달');
}
```

<br>

## 겪었던 문제 / 트러블슈팅

- **문제 상황**: 알림함 화면을 시안 없이 만들면서 "모두 읽음" 버튼을 브랜드 초록 바탕에 흰 글자로 두려고 했다. 계산해 보니 그 크기에서는 대비가 **3.43:1**로 일반 글자 기준(4.5:1)에 못 미쳤다.
- **해결 방안**: 흰 바탕에 어두운 글자, 초록은 아이콘에만 쓰는 쪽으로 바꿨다. 읽음 여부도 "읽음" 같은 글자 대신 글자 굵기와 브랜드색 점으로 구분하고, 점이 사라져도 자리는 남겨서 글줄이 밀리지 않게 했다.

<br>

## 참고 문헌 및 자료

- [Understanding SC 1.4.3: Contrast (Minimum) (W3C)](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
