# Apache Kafka (분산 이벤트 스트리밍 플랫폼)

- **Category:** #Kafka #DataEngineering #MessageQueue
- **Time:** (학습 시간 기입)

<br>

## 새롭게 알게 된 것

- Kafka는 단순한 메시지 큐가 아니라 **분산 이벤트 스트리밍 플랫폼**이다. 데이터를 보내는 쪽(Producer)과 받는 쪽(Consumer)을 분리(디커플링)해서, 서비스 간 직접 API 호출 없이 이벤트 기반으로 통신할 수 있게 해준다.
- **핵심 구성 요소**
  - **Producer**: 메시지(이벤트)를 발행하는 쪽
  - **Consumer**: 메시지를 구독해서 가져가는 쪽
  - **Broker**: 메시지를 저장·중계하는 Kafka 서버. 여러 대를 묶어 클러스터로 운영한다.
  - **Topic**: 메시지를 분류하는 논리적 채널 (예: `order-events`, `payment-events`)
  - **Partition**: Topic을 물리적으로 쪼갠 단위. 파티션을 늘리면 병렬 처리량이 늘어난다.
  - **Offset**: 파티션 내 메시지의 순번. Consumer는 "어디까지 읽었는지"를 offset으로 관리한다.
- **일반 메시지 큐(RabbitMQ 등)와의 가장 큰 차이**: Kafka는 메시지를 소비해도 즉시 삭제하지 않고, 설정한 보존 기간(retention) 동안 **로그 형태로 디스크에 남겨둔다**. 그래서 여러 Consumer 그룹이 같은 데이터를 각자의 속도로 읽을 수 있고, 장애 시 offset을 되돌려 재처리도 가능하다.
- **Consumer Group**: 같은 그룹에 속한 Consumer들은 파티션을 나눠서 소비한다(큐 방식). 그룹이 다르면 각 그룹이 전체 메시지를 다 받는다(Pub/Sub 방식). 즉, 그룹 개념 하나로 큐와 Pub/Sub을 모두 구현한다.
- **순서 보장은 Topic 전체가 아니라 Partition 단위**로만 된다. 순서가 중요한 데이터(예: 같은 주문의 상태 변화)는 같은 key를 줘서 같은 파티션에 들어가게 해야 한다.
- 높은 처리량의 비결: 디스크에 **순차 쓰기(append-only log)** + OS 페이지 캐시 + zero-copy 전송. 디스크를 쓰는데도 빠른 이유가 랜덤 I/O가 아니라 순차 I/O이기 때문이다.

<br>

## 예제 코드

```python
# pip install kafka-python
from kafka import KafkaProducer, KafkaConsumer
import json

# Producer: 주문 이벤트 발행
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    key_serializer=lambda k: k.encode("utf-8"),
)
# 같은 key(주문 ID)는 같은 파티션으로 들어가서 순서가 보장된다
producer.send("order-events", key="order-1", value={"order_id": 1, "status": "CREATED"})
producer.send("order-events", key="order-1", value={"order_id": 1, "status": "PAID"})
producer.flush()

# Consumer: 같은 group_id끼리는 파티션을 나눠서 소비한다
consumer = KafkaConsumer(
    "order-events",
    bootstrap_servers="localhost:9092",
    group_id="order-service",
    auto_offset_reset="earliest",  # 저장된 offset이 없으면 처음부터 읽기
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)
for msg in consumer:
    print(f"partition={msg.partition} offset={msg.offset} value={msg.value}")
```

<br>

## 겪었던 문제 / 트러블슈팅

- **헷갈렸던 점 1**: "메시지 큐면 RabbitMQ랑 뭐가 다르지?"라고 생각했는데, Kafka는 소비해도 메시지가 사라지지 않는 **로그 저장소**라는 점이 근본적인 차이였다. 그래서 같은 데이터를 실시간 처리용, 배치 적재용 등 여러 소비자가 독립적으로 읽는 파이프라인이 가능하다.
- **헷갈렸던 점 2**: Consumer를 늘리면 무조건 빨라지는 줄 알았는데, **하나의 파티션은 그룹 내에서 하나의 Consumer만 소비**할 수 있다. 파티션이 3개인데 Consumer가 4개면 1개는 논다. 병렬성의 상한은 파티션 수라는 것.
- **헷갈렸던 점 3**: 순서 보장이 Topic 단위인 줄 알았는데 **Partition 단위**였다. key 없이 보내면 라운드로빈으로 파티션에 분산되어 순서가 섞일 수 있다.

<br>

## 참고 문헌 및 자료

- [Apache Kafka 공식 문서 - Introduction](https://kafka.apache.org/documentation/#gettingStarted)
- [Confluent - Kafka 개념 설명](https://developer.confluent.io/what-is-apache-kafka/)
- 함께 보기: [Hadoop TIL](./Hadoop.md) — Kafka로 수집한 스트림을 HDFS에 적재하는 파이프라인 구성이 흔한 패턴
