import os
from openai import OpenAI
from django.conf import settings

def check_inappropriate_content(title, content):
    mode = getattr(settings, 'MODE', 'OPENAI')
    api_key = getattr(settings, 'OPENAI_API_KEY', '')
    
    if mode == 'OPENAI' and api_key:
        try:
            client = OpenAI(api_key=api_key)
            prompt = f"다음 제목과 내용을 확인하고 욕설, 비방, 혐오 등 부적절한 표현이 포함되어 있다면 'True', 그렇지 않다면 'False' 라고만 대답해줘.\n제목: {title}\n내용: {content}"
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=10,
                temperature=0.0
            )
            result = response.choices[0].message.content.strip().lower()
            if 'true' in result:
                return True
        except Exception as e:
            print("LLM 검사를 실패했거나 우회합니다.:", e)
            return False
    return False
