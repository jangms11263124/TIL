# A2A (Agent2Agent Protocol)

- **Category:** #AIAgent #A2A #Protocol

<br>

## 새롭게 알게 된 것

- A2A는 **서로 다른 회사·프레임워크로 만들어진 AI 에이전트들이 서로를 발견하고 협업할 수 있게 하는 개방형 표준 프로토콜**이다. 2025년 4월 Google이 공개했고, 이후 Linux Foundation으로 이관되어 중립적으로 관리된다. 현재 v1.0이 안정 버전.
- **왜 필요한가**: 에이전트마다 API가 제각각이면 에이전트 N개를 연결할 때 N×N개의 커스텀 연동이 필요하다. A2A는 "에이전트끼리 대화하는 공통 언어"를 정해서, 상대가 LangGraph로 만들어졌든 자체 구현이든 상관없이 통신할 수 있게 한다.
- **핵심 개념**
  - **Agent Card**: 에이전트의 "명함". `/.well-known/agent-card.json` 경로에 공개되는 JSON 문서로, 이름·설명·보유 스킬·지원 기능(스트리밍, 푸시 알림)·인증 방식을 담는다. 클라이언트 에이전트는 이걸 읽고 "이 에이전트에게 이 일을 맡겨도 되는지" 판단한다. (디스커버리)
  - **Task**: 상태를 가진 작업 단위. `submitted → working → completed / failed / canceled / rejected` 라이프사이클을 가지며, 중간에 `input-required`(추가 입력 대기), `auth-required`(인증 대기) 상태로 멈출 수도 있다. 즉, **몇 초짜리 요청-응답이 아니라 몇 시간짜리 장기 작업까지 표현**할 수 있다.
  - **Message / Part**: 통신의 한 턴(turn). role은 `user` 또는 `agent`이고, 내용물인 Part는 텍스트, 파일(바이트), URL 참조 등 멀티모달을 지원한다.
  - **Artifact**: Task의 최종 산출물. "대화(Message)"와 "결과물(Artifact)"을 명확히 분리하는 게 설계 포인트다.
- **통신 방식**: 전송 바인딩은 JSON-RPC 2.0, gRPC, HTTP+JSON/REST 세 가지가 표준으로 정의되어 있다. 진행 상황 수신은 ① 폴링(`tasks/get`) ② SSE 스트리밍(`message/stream`) ③ 푸시 알림(웹훅 등록) 세 방법을 지원한다.
- **MCP와의 관계 (중요)**: 경쟁이 아니라 상호보완이다.
  - **MCP** = 에이전트 ↔ 도구/데이터 연결 (수직 통합, "에이전트에게 손발 달아주기")
  - **A2A** = 에이전트 ↔ 에이전트 연결 (수평 통합, "에이전트끼리 협업시키기")
  - 하나의 에이전트가 MCP로 도구를 쓰면서, 자기 전문 분야가 아닌 일은 A2A로 다른 에이전트에게 위임하는 조합이 표준적인 그림이다.
- **불투명성(opaque)**: A2A에서 에이전트들은 서로의 내부(프롬프트, 메모리, 사용 도구)를 공유하지 않는다. 오직 메시지와 결과물로만 협업한다. 그래서 사내 에이전트와 외부 업체 에이전트처럼 신뢰 경계를 넘는 협업이 가능하다.

<br>

## 예제 코드

**1) Agent Card 조회 (디스커버리)**: 상대 에이전트가 뭘 할 수 있는지 먼저 확인

```json
// GET https://translator.example.com/.well-known/agent-card.json
{
  "name": "translator-agent",
  "description": "한국어-영어 전문 번역 에이전트",
  "capabilities": { "streaming": true, "pushNotifications": false },
  "skills": [
    { "id": "ko-en-translate", "name": "한영 번역", "description": "문서 단위 한국어→영어 번역" }
  ],
  "securitySchemes": [{ "type": "oauth2" }]
}
```

**2) 작업 요청 (JSON-RPC 2.0 바인딩의 `message/send`)**

```json
// POST https://translator.example.com/a2a
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "message/send",
  "params": {
    "message": {
      "messageId": "msg-001",
      "role": "user",
      "parts": [{ "kind": "text", "text": "다음 문서를 영어로 번역해줘: 오늘 배운 내용을 정리한다." }]
    }
  }
}
```

**3) 응답: Task로 감싸져서 돌아온다** (상태와 결과물이 분리되어 있음)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "id": "task-42",
    "status": { "state": "completed" },
    "artifacts": [
      {
        "artifactId": "artifact-1",
        "parts": [{ "kind": "text", "text": "I summarize what I learned today." }]
      }
    ]
  }
}
```

작업이 오래 걸리면 `status.state`가 `working`으로 먼저 오고, 이후 `tasks/get`으로 폴링하거나 `message/stream`(SSE)으로 진행 상황을 구독한다.

<br>

## 겪었던 문제 / 트러블슈팅

- **헷갈렸던 점 1**: "MCP가 있는데 A2A가 왜 또 필요하지? 경쟁 표준인가?" → 층이 다르다. MCP는 에이전트가 **도구를 호출**하는 규약이고, A2A는 에이전트가 **다른 에이전트에게 일을 맡기는** 규약이다. 도구는 정해진 입출력의 함수지만, 에이전트는 되묻기도 하고(`input-required`) 거절하기도 하는(`rejected`) 자율적인 상대라서 별도 프로토콜이 필요하다.
- **헷갈렸던 점 2**: 다른 에이전트 호출을 함수 호출처럼 "부르면 바로 리턴"으로 생각했는데, A2A의 기본 단위는 **상태를 가진 Task**다. 제출 후 작업 중, 입력 대기, 완료까지 라이프사이클이 있고, 그래서 폴링/스트리밍/푸시 같은 비동기 수신 방식이 스펙에 포함되어 있다.
- **헷갈렸던 점 3**: Agent Card 경로를 초기 자료에서 본 `agent.json`으로 알고 있었는데, 최신 스펙에서는 **`/.well-known/agent-card.json`**이다. 이 프로토콜은 아직 빠르게 바뀌고 있어서(v0.2 → v0.3 → v1.0에서 gRPC/REST 바인딩 추가 등) 블로그보다 공식 스펙 문서를 기준으로 봐야 한다.

<br>

## 참고 문헌 및 자료

- [A2A 공식 스펙 문서](https://a2a-protocol.org/latest/specification/)
- [GitHub - a2aproject/A2A](https://github.com/a2aproject/A2A)
- [Google 발표 블로그 - Announcing the Agent2Agent Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- 함께 보기: MCP(Model Context Protocol)와 비교. MCP는 에이전트와 도구를, A2A는 에이전트끼리를 잇는다
