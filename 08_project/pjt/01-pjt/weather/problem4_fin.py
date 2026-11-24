import os
import requests
from pprint import pprint

# 문제4. 3번의 데이터를 활용하여, 섭씨 온도 데이터를 추가합니다.


def get_result(api_key):

    lat = 37.56
    lon = 126.97

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url).json()

    m = response.get('main', {})
    # 기존 키값에 섭씨 온도 데이터를 추가로 구성합니다.
    main_data = {
        '기압': m.get('pressure'),
        '습도': m.get('humidity'),
        '온도': m.get('temp'),
        '온도(섭씨)': round(m.get('temp') - 273.15, 2),
        '체감온도': m.get('feels_like'),
        '체감온도(섭씨)': round(m.get('feels_like') - 273.15, 2),
        '최고온도': m.get('temp_max'),
        '최고온도(섭씨)': round(m.get('temp_max') - 273.15, 2),
        '최저온도': m.get('temp_min'),
        '최저온도(섭씨)': round(m.get('temp_min') - 273.15, 2)
    }

    w_list = response.get('weather', [])
    weather_data = []

    for w in w_list:
        weather_data.append({
            '요약': w.get('description'),
            '아이콘': w.get('icon'),
            '식별자': w.get('id'),
            '핵심': w.get('main')
        })

    result = {
        '기본': main_data,
        '날씨': weather_data
    }

    return result


# 여러분의 OpenWeatherMap API 키를 설정하세요
api_key = os.getenv('OPENWEATHER_API_KEY')

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_result(api_key)
    # pprint.pprint(): json 을 보기 좋은 형식으로 출력
    pprint(result)
