import os
import requests
from pprint import pprint

# 문제1. 날씨 데이터의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.


def get_result(api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    result = requests.get(url).json()
    return result


lat = 37.56
lon = 126.97

# 여러분의 OpenWeatherMap API 키를 설정하세요
api_key = os.getenv('OPENWEATHER_API_KEY')

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_result(api_key)
    # pprint.pprint(): json 을 보기 좋은 형식으로 출력
    pprint(result)
