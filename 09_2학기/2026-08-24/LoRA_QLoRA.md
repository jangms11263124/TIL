# LoRA와 QLoRA로 작은 LLM 파인튜닝하기

- **Category:** #AI #LLM #PEFT #LoRA
- **Time:** (학습 시간 기입)

<br>

## 새롭게 알게 된 것

- **LoRA(Low-Rank Adaptation)** 는 모델 가중치 전체를 학습하지 않고, 원래 가중치는 얼려 둔 채 옆에 작은 행렬 두 개(A, B)를 붙여 그것만 학습한다. 가중치 변화량 ΔW를 `B × A`(rank r)로 근사하는 방식이라 학습할 파라미터 수가 크게 줄어든다.
  - `r`: 붙이는 행렬의 rank. 클수록 표현력은 늘지만 파라미터도 늘어난다.
  - `lora_alpha`: 학습된 변화량에 곱하는 배율. 보통 `alpha = 2r` 정도로 둔다.
  - `target_modules`: 어느 층에 붙일지. 어텐션의 `q_proj`, `v_proj` 등에 주로 붙인다.
- 학습 결과는 몇 MB짜리 **어댑터**(`adapter_model.safetensors`)로 따로 저장된다. 베이스 모델은 그대로 두고 어댑터만 갈아 끼울 수 있고, 필요하면 베이스에 병합(merge)해서 하나의 모델로 만들 수도 있다.
- **QLoRA** 는 베이스 모델을 4-bit(NF4)로 양자화해서 올린 뒤 그 위에서 LoRA를 학습한다. 메모리가 작은 GPU에서도 더 큰 모델을 학습할 수 있게 해 주는 대신, 양자화·역양자화 때문에 학습 속도는 느려진다.
- Text-to-SQL처럼 정답을 실행해 볼 수 있는 과제는 문자열이 같은지가 아니라 **실행 결과가 같은지(execution accuracy)** 로 평가한다. 쿼리 모양이 달라도 결과가 같으면 맞힌 것으로 본다.

### 직접 돌려 본 결과 (RTX 4050 Laptop 6GB, Spider 검증 60개)

| 실험 | 모델 | 설정 | 학습 시간 | execution accuracy |
| --- | --- | --- | --- | --- |
| LoRA | SmolLM2-360M-Instruct | r=32, alpha=64, 100 step | 143초 | 0.567 → **0.717** |
| QLoRA | SmolLM2-1.7B-Instruct (NF4) | r=16, alpha=32, 100 step | 418초 | 0.550 → 0.550 |

- 360M 모델은 LoRA 100 step만으로 15%p 올랐다. 난이도별로는 medium 문제가 0.250 → 0.562로 가장 크게 올랐다.
- 1.7B 모델은 4-bit 덕분에 6GB에서 학습이 되긴 했지만, 같은 100 step으로는 점수가 오르지 않았다. 학습 속도도 0.70 → 0.24 step/s로 3배 가까이 느렸다. "큰 모델 + QLoRA"가 항상 낫지는 않고, 데이터와 step 수가 받쳐 줘야 한다는 걸 확인했다.

<br>

## 예제 코드

```python
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch

# LoRA: 원래 가중치는 얼리고 q/v projection 옆에 작은 행렬만 붙인다
lora_config = LoraConfig(
    r=32,
    lora_alpha=64,
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj"],
    task_type="CAUSAL_LM",
)
model = AutoModelForCausalLM.from_pretrained("HuggingFaceTB/SmolLM2-360M-Instruct")
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()  # 학습 대상 파라미터가 전체의 일부인 걸 확인

# QLoRA: 베이스를 4-bit(NF4)로 올린 뒤 같은 방식으로 LoRA를 붙인다
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)
base = AutoModelForCausalLM.from_pretrained(
    "HuggingFaceTB/SmolLM2-1.7B-Instruct",
    quantization_config=bnb_config,
    device_map="auto",
)
```

<br>

## 겪었던 문제 / 트러블슈팅

- **문제 상황**: 노트북 안의 `!` 셸 명령과 `subprocess(shell=True)`가 전부 실패했다. 평가 스크립트도 돌지 않았다.
- **원인**: 이 PC의 시스템 환경 변수 `ComSpec`이 `cmd.exe`가 아니라 다른 프로그램 경로로 덮어써져 있었다. 파이썬은 `shell=True`일 때 `ComSpec`이 가리키는 프로그램으로 명령을 실행하기 때문에, 셸을 거치는 호출이 모두 깨졌다.
- **해결 방안**: 실행 세션에서 `$env:COMSPEC = "$env:SystemRoot\System32\cmd.exe"`로 바로잡은 뒤 노트북을 실행했다. 영구적으로 고치려면 관리자 권한으로 시스템 환경 변수를 되돌려야 한다.

- **문제 상황**: 평가 셀에서 띄운 PowerShell이 가상 환경이 아니라 conda의 python을 잡았다.
- **해결 방안**: PowerShell 프로필이 conda를 먼저 활성화하고 있었다. `powershell -NoProfile`로 띄워 프로필을 건너뛰게 했다.

<br>

## 참고 문헌 및 자료

- [LoRA 논문 (arXiv 2106.09685)](https://arxiv.org/abs/2106.09685)
- [QLoRA 논문 (arXiv 2305.14314)](https://arxiv.org/abs/2305.14314)
- [Hugging Face PEFT 문서](https://huggingface.co/docs/peft)
- [Spider 데이터셋](https://yale-lily.github.io/spider)
