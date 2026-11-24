# vLLM으로 LLM 추론 빠르게 하기

- **Category:** #AI #LLM #Serving #vLLM
- **Time:** (학습 시간 기입)

<br>

## 새롭게 알게 된 것

- LLM 추론이 느린 큰 이유 중 하나는 **KV 캐시** 관리다. 토큰을 하나 만들 때마다 앞 토큰들의 Key/Value를 GPU 메모리에 쌓아 두는데, 요청마다 최대 길이만큼 미리 잡아 두면 안 쓰는 공간이 많이 생긴다.
- vLLM의 **PagedAttention** 은 KV 캐시를 OS의 가상 메모리처럼 작은 블록(page) 단위로 나눠서 필요할 때만 할당한다. 버려지는 메모리가 줄어서 한 번에 더 많은 요청을 GPU에 올릴 수 있다.
- **Continuous batching**: 배치 안의 요청이 다 끝날 때까지 기다리지 않고, 끝난 요청 자리에 새 요청을 바로 끼워 넣는다. 처리량(throughput)이 크게 오른다.
- LoRA 어댑터를 베이스 모델에 병합하지 않고 **실행 중에 붙여서(runtime load)** 쓸 수 있다. 어댑터 여러 개를 하나의 서버에서 바꿔 가며 쓸 수 있다.
- vLLM은 Windows를 직접 지원하지 않아서 **WSL2(Ubuntu 22.04)** 에서 돌렸다.

### 직접 잰 결과 (SmolLM2-360M + LoRA 병합 모델, RTX 4050 Laptop 6GB)

| 항목 | Transformers | vLLM | 차이 |
| --- | --- | --- | --- |
| 처리량 | 15.16 tok/s | 149.70 tok/s | 약 9.9배 |
| 총 추론 시간 | 7.72초 | 0.60초 | 약 12.8배 |
| 첫 토큰 지연 | 180.8ms | 169.4ms | 6.3% 개선 |

- 처리량은 10배 가까이 올랐지만 **첫 토큰 지연은 거의 그대로**였다. vLLM이 빨라지는 지점은 "많은 요청을 한꺼번에 처리할 때"라서, 요청 하나의 첫 응답 속도와는 다른 문제라는 걸 숫자로 확인했다.

<br>

## 예제 코드

```python
from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest

llm = LLM(
    model="HuggingFaceTB/SmolLM2-360M-Instruct",
    enable_lora=True,
    gpu_memory_utilization=0.55,  # 6GB GPU라 기본값(0.9)보다 낮췄다
    max_model_len=2048,
)
params = SamplingParams(temperature=0.0, max_tokens=256)

prompts = ["-- 학생 테이블에서 나이가 20 이상인 학생 수를 구하는 SQL\n"]

# 베이스 모델 그대로
outputs = llm.generate(prompts, params)

# 학습한 LoRA 어댑터를 실행 중에 붙여서 생성
outputs = llm.generate(
    prompts,
    params,
    lora_request=LoRARequest("text2sql", 1, "./outputs/checkpoint-100"),
)
print(outputs[0].outputs[0].text)
```

<br>

## 겪었던 문제 / 트러블슈팅

- **문제 상황**: 노트북에서 비교 실험을 하려고 엔진을 한 번 내렸다가 다시 띄우면 메모리 부족으로 실패했다.
- **원인**: `gpu_memory_utilization`은 GPU 메모리 중 vLLM이 미리 잡아 둘 비율이다. 6GB GPU에서 0.75로 잡으면 이전 엔진이 메모리를 완전히 놓기 전에 새 엔진이 같은 양을 다시 잡으려고 해서 경합이 생겼다.
- **해결 방안**: 비율을 0.75 → 0.55로 낮추고, 이전 엔진 객체를 `del`로 지운 뒤 잠시 기다렸다가 새 엔진을 띄우게 했다. 작은 GPU에서는 기본값을 그대로 쓰지 말고 모델 크기에 맞춰 낮춰야 한다.

<br>

## 참고 문헌 및 자료

- [vLLM 공식 문서](https://docs.vllm.ai/)
- [PagedAttention 논문 (arXiv 2309.06180)](https://arxiv.org/abs/2309.06180)
- [Install WSL (Microsoft Learn)](https://learn.microsoft.com/windows/wsl/install)
