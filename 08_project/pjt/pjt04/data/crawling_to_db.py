import os
import django
from urllib.request import urlopen
from urllib.parse import quote
import xml.etree.ElementTree as ET
from openai import OpenAI

# 1. Django 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_board.settings')
django.setup()

from boards.models import Post
from django.conf import settings

def generate_toss_style_content(title, link):
    """OpenAI API를 활용해 기사 내용을 요약하거나, API 키가 없을 시 제목과 링크만 깔끔하게 출력합니다."""
    api_key = getattr(settings, 'OPENAI_API_KEY', '')
    
    # API 키가 없으면 (에러 메시지 대신) 제목을 강조해서 보여주고 원문 링크 제공
    if not api_key or api_key.strip() == "":
        return f"""
        <div style="margin-bottom: 30px;">
            <h3 style="margin-top: 0; color: #f2f4f6; font-size: 1.4rem; line-height: 1.5;">{title}</h3>
        </div>
        <div style="margin-top: 40px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 40px; text-align: center;">
            <a href='{link}' target='_blank' style="display: inline-flex; align-items: center; justify-content: center; background: rgba(49,130,246,0.15); color: #3182f6; padding: 14px 30px; border-radius: 12px; font-weight: 600; font-size: 1.1rem; text-decoration: none; transition: transform 0.2s;">
                기사 원문 보러가기 &rarr;
            </a>
        </div>
        """
    
    client = OpenAI(api_key=api_key)
    prompt = f"""
당신은 토스(Toss) 피드 스타일의 금융/경제 콘텐츠 에디터입니다.
다음 기사 제목을 바탕으로 사람들이 읽기 쉽고 직관적인 핵심 요약글을 HTML 형식으로 작성해주세요.

[기사 제목]: {title}
[원문 링크]: {link}

요구사항:
1. 최상단에는 <div class="summary-box"> 태그를 사용하여 2~3줄로 기사의 TL;DR(핵심 요약)을 친절한 말투로 작성해주세요.
2. 그 밑에는 <h3> 태그로 주요 섹션 제목(예: "꼭 알아두어야 할 포인트")을 넣고, <ul>과 <li>를 활용하여 3~4가지 핵심 포인트를 가독성 있게 정리해주세요.
3. 텍스트 강조가 필요한 곳은 <strong>을 사용하세요.
4. 마지막에는 <p> 태그 안에 원문 링크를 보기 좋게 첨부해주세요. (예: <a href="{link}" target="_blank">기사 원문 보러가기 &rarr;</a>)
5. 마크다운 코드 블록(```html, ```)이나 <html>, <body> 태그 없이 내부 순수 HTML 문자열만 바로 반환해주세요.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=600
        )
        result = response.choices[0].message.content.strip()
        # Remove potential markdown block wrappers just in case
        if result.startswith("```html"):
            result = result[7:]
        if result.endswith("```"):
            result = result[:-3]
        return result.strip()
    except Exception as e:
        print(f"OpenAI 요약 에러: {e}")
        return f"<div class='summary-box'>요약을 생성하는 중 오류가 발생했습니다.</div><p><a href='{link}' target='_blank'>기사 원문 보러가기 &rarr;</a></p>"

def crawl_and_upload():
    # 2. 크롤링 대상 키워드와 매칭
    assets = {
        'stock-kospi': '코스피 시황',
        'stock-kosdaq': '코스닥 시황',
        'gold': '금값 전망',
        'us-stock': '미국주식 나스닥',
        'bond-korea': '한국 국채 금리',
        'bitcoin': '비트코인 전망'
    }

    print("크롤링 및 AI 요약 자동 업로드를 시작합니다 (자산별 2건)...")
    
    # 이전에 자동 생성된 게시글(가독성을 위해) 전부 지우고 새로 생성 (원치 않으면 주석처리)
    Post.objects.filter(author="금융 봇").delete()
    
    for asset_id, keyword in assets.items():
        url = f"https://news.google.com/rss/search?q={quote(keyword)}&hl=ko&gl=KR&ceid=KR:ko"
        
        try:
            response = urlopen(url)
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            # 각 자산별 상위 2개의 뉴스만 (API 호출 시간 단축 목적)
            items = root.findall('.//item')[:2]
            for item in items:
                title = item.find('title').text
                link = item.find('link').text
                
                # 중복 방지
                clean_title = f"{title.split(' - ')[0]}" # 끝에 언론사 제거
                if not Post.objects.filter(title=clean_title).exists():
                    print(f"[{keyword}] AI 요약 중: {clean_title}")
                    formatted_content = generate_toss_style_content(clean_title, link)
                    
                    Post.objects.create(
                        asset_id=asset_id,
                        title=clean_title,
                        content=formatted_content,
                        author="금융 봇"
                    )
            print(f"✅ [{keyword}] 게시글 업로드 완료!")
        except Exception as e:
            print(f"❌ {keyword} 크롤링 실패: {e}")

if __name__ == '__main__':
    crawl_and_upload()
    print("모든 작업이 완료되었습니다! 웹 페이지를 새로고침 해보세요.")
