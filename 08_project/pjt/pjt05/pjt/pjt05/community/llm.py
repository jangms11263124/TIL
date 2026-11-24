"""
OpenAI/Upstage Chat Completions를 활용한 기능들.
1) 부적절한 텍스트 검사 (기존)
2) 투자 성향 분석 (F511)
"""
from django.conf import settings
from openai import OpenAI

SYSTEM_PROMPT_FILTER = """당신은 한국어 커뮤니티의 '부적절 표현' 판별기입니다.
아래 규칙으로 사용자 입력(한 문장 또는 여러 문장)을 검사하세요.

[판정 원칙]
1) 아래 항목 중 하나라도 해당하면 반드시 부적절(YES)입니다.
2) 맥락상 상대를 직접 공격/비하/모욕하면, 전형적 욕설이 아니어도 YES입니다.
3) 우회 표현(오타, 띄어쓰기 분리, 초성/자모 분해, 비슷한 발음 치환)도 원형으로 간주해 YES 처리합니다.

[YES(부적절)로 판단할 내용]
- 욕설/비속어/모욕/인신공격
- 혐오/차별/비하 발언
- 괴롭힘/협박/위협/폭력 조장
- 성적 대상화/성희롱/음란성 표현

출력 규칙:
- 부적절하면 YES, 적절하면 NO만 출력하세요."""

SYSTEM_PROMPT_ANALYSIS = """당신은 전문 금융 투자 분석가입니다.
사용자가 작성한 게시글들을 분석하여 사용자의 '투자 성향'을 진단해 주세요.

[분석 지침]
1. 사용자가 관심을 가지는 자산 타입(주식, 채권, 가상자산 등)을 파악하세요.
2. 말투와 내용을 통해 위험 선호도(공격적, 중립적, 방어적)를 판단하세요.
3. 분석 결과를 친절하고 전문적인 한국어로 작성해 주세요.
4. 게시글 내용이 부족하면 분석이 어렵다는 점을 정중히 안내해 주세요.

작성 형식:
- 투자 성향 요약 (한 줄)
- 상세 분석 (자산 관심도, 위험 선호도)
- 투자 조언 (짧게)"""

def _build_llm_client():
    mode = (getattr(settings, "MODE", "OPENAI") or "OPENAI").strip().upper()

    if mode == "UPSTAGE":
        api_key = (getattr(settings, "UPSTAGE_API_KEY", None) or "").strip()
        if not api_key:
            return None, None
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.upstage.ai/v1/solar",
        )
        return client, "solar-mini"

    api_key = (getattr(settings, "OPENAI_API_KEY", None) or "").strip()
    if not api_key:
        return None, None
    client = OpenAI(api_key=api_key)
    return client, "gpt-4o-mini"  # Using a standard model name

def is_inappropriate(text: str) -> bool:
    if not text or not text.strip():
        return False

    client, model = _build_llm_client()
    if not client:
        return False

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT_FILTER},
                {"role": "user", "content": text.strip()},
            ],
        )
        answer = (resp.choices[0].message.content or "").strip().upper()
        return "YES" in answer
    except Exception:
        return False

def analyze_investment_style(posts_content: str) -> str:
    """사용자 게시글 목록을 기반으로 투자 성향 분석"""
    if not posts_content or len(posts_content) < 20:
        return "분석할 데이터가 부족합니다. 더 많은 게시글을 작성해 주세요."

    client, model = _build_llm_client()
    if not client:
        return "API 설정을 확인해 주세요. (관리자 문의)"

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT_ANALYSIS},
                {"role": "user", "content": f"다음은 사용자가 작성한 게시글들입니다:\n\n{posts_content}"},
            ],
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"분석 중 오류가 발생했습니다: {str(e)}"
