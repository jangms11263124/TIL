import os
import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY 에 해당하는 한글 KEY 값들은 다음과 같습니다.
# feels_like : '체감온도',
# humidity : '습도',
# pressure : '기압',
# temp : '온도',
# temp_max : '최고온도',
# temp_min : '최저온도',
# description : '요약',
# icon : '아이콘',
# main : '핵심’
# id : ‘식별자’


def get_result(api_key):

    lat = 37.56
    lon = 126.97

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url).json()

    m = response.get('main', {})
    main_data = {
        '기압': m.get('pressure'),
        '습도': m.get('humidity'),
        '온도': m.get('temp'),
        '체감온도': m.get('feels_like'),
        '최고온도': m.get('temp_max'),
        '최저온도': m.get('temp_min')
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
