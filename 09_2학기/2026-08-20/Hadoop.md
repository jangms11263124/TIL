# Apache Hadoop (분산 저장 및 배치 처리 프레임워크)

- **Category:** #Hadoop #DataEngineering #BigData

<br>

## 새롭게 알게 된 것

- Hadoop은 하나의 프로그램이 아니라 **세 가지 핵심 모듈의 묶음**이다.
  - **HDFS** (분산 파일 시스템): 큰 파일을 블록(기본 128MB)으로 쪼개 여러 서버에 나눠 저장. 각 블록을 기본 3개로 **복제**해서 서버 몇 대가 죽어도 데이터가 유실되지 않는다.
  - **MapReduce** (분산 처리 모델): 데이터를 "데이터가 있는 곳으로 코드를 보내서" 병렬 처리하는 프로그래밍 모델. Map(변환) → Shuffle(같은 key끼리 모으기) → Reduce(집계) 순서로 동작한다.
  - **YARN** (리소스 관리자): 클러스터의 CPU/메모리를 여러 작업에 분배하는 스케줄러. MapReduce뿐 아니라 Spark 같은 다른 엔진도 YARN 위에서 돈다.
- **HDFS 구조**: 메타데이터(파일이 어떤 블록으로 어디에 저장됐는지)를 관리하는 **NameNode** 1대와, 실제 블록을 저장하는 다수의 **DataNode**로 구성된 마스터-슬레이브 구조다.
- 핵심 철학은 **스케일 아웃(scale-out)**: 비싼 서버 한 대를 키우는 게 아니라, 저렴한 서버(commodity hardware)를 여러 대 붙여서 용량과 처리량을 늘린다. 장애는 "예외"가 아니라 "일상"으로 간주하고 복제로 견딘다.
- HDFS는 **한 번 쓰고 여러 번 읽는(write-once, read-many)** 워크로드에 최적화되어 있다. 파일 중간 수정이 안 되고 append만 가능하다. 실시간 조회용 DB가 아니라 대용량 배치 분석용 저장소다.
- **Spark와의 관계**: Spark는 Hadoop 전체를 대체하는 게 아니라 **MapReduce(처리 엔진) 부분을 대체**한다. 디스크 기반인 MapReduce와 달리 메모리 기반이라 반복 연산에서 훨씬 빠르고, 저장소로는 여전히 HDFS를, 리소스 관리로는 YARN을 그대로 쓰는 조합이 흔하다.

<br>

## 예제 코드

Hadoop Streaming을 쓰면 Java 없이 Python으로도 MapReduce를 돌릴 수 있다. (WordCount 예제)

```python
# mapper.py — 한 줄씩 읽어서 (단어, 1) 쌍을 출력
import sys

for line in sys.stdin:
    for word in line.strip().split():
        print(f"{word}\t1")
```

```python
# reducer.py — shuffle 단계에서 key로 정렬되어 들어오므로, 같은 단어끼리 누적
import sys

current_word, count = None, 0
for line in sys.stdin:
    word, num = line.strip().split("\t")
    if word == current_word:
        count += int(num)
    else:
        if current_word is not None:
            print(f"{current_word}\t{count}")
        current_word, count = word, int(num)

if current_word is not None:
    print(f"{current_word}\t{count}")
```

```bash
# HDFS에 입력 파일 업로드 후 스트리밍 잡 실행
hdfs dfs -put data.txt /input/
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /input/data.txt \
  -output /output/wordcount \
  -mapper mapper.py -reducer reducer.py \
  -file mapper.py -file reducer.py

# 결과 확인
hdfs dfs -cat /output/wordcount/part-00000
```

로컬에서는 파이프라인으로 동작 원리를 흉내낼 수 있다. (shuffle의 정렬 역할을 `sort`가 대신함)

```bash
cat data.txt | python mapper.py | sort | python reducer.py
```

<br>

## 겪었던 문제 / 트러블슈팅

- **헷갈렸던 점 1**: "요즘은 다 Spark 쓰는데 Hadoop은 죽은 기술 아닌가?"라고 생각했는데, Spark가 대체한 건 MapReduce 엔진이고 **HDFS와 YARN은 여전히 빅데이터 인프라의 기반**으로 쓰인다. (클라우드에선 HDFS 역할을 S3 같은 오브젝트 스토리지가 대신하는 추세)
- **헷갈렸던 점 2**: HDFS에 작은 파일을 잔뜩 넣으면 안 되는 이유 — 블록·파일 하나당 메타데이터가 **NameNode의 메모리**에 올라가기 때문에, 1GB짜리 파일 1개보다 1MB짜리 파일 1024개가 NameNode에 훨씬 부담이다. 작은 파일은 합쳐서 저장하는 게 정석.
- **헷갈렸던 점 3**: reducer가 단순히 딕셔너리로 세면 되는 줄 알았는데, MapReduce에서는 **shuffle 단계가 key 정렬을 보장**해주기 때문에 위 예제처럼 "이전 key와 비교하는" 스트리밍 방식으로 메모리를 거의 안 쓰고 집계할 수 있다. 데이터가 메모리보다 클 수 있다는 전제가 설계에 깔려 있다.

<br>

## 참고 문헌 및 자료

- [Apache Hadoop 공식 문서](https://hadoop.apache.org/docs/stable/)
- [HDFS Architecture](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
- 함께 보기: [Kafka TIL](./Kafka.md) — 실시간 수집(Kafka) → 대용량 저장·배치 분석(HDFS)으로 이어지는 데이터 파이프라인 패턴
