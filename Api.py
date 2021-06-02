'''
https://openweathermap.org/
사이트에서 날씨 API를 받아오는 실습
requests 모듈을 이용하여 Rest API 형식으로 Data를 받아온다.
'''

import requests

API_KEY = "505243b0dd8c812e1a716cb5c5c4fed6"
URL = "http://api.openweathermap.org/data/2.5/weather"

'''
API_KEY와 URL은 보통 API를 제공하는 사이트에서 알려준다.
'''

city = "Hwaseong"
r = requests.get(URL, params={"q": city, "APPID": API_KEY, "units": "metric"})
data = r.json()

'''
보통 정보를 제공하는 API들은 json 형식으로 전달하는 경우가 대다수인 것 같다.
'''

wind_speed = data["wind"]["speed"]
country = data["sys"]["country"]
weather = data["weather"][0]["main"]
temp = data["main"]["temp"]

print(f"도시 이름 : {city}")
print(f"나라 이름 : {country}")
print(f"날씨 : {weather}")
print(f"바람 속도 : {wind_speed}")
print(f"기온 : {temp}")

'''
requests를 요청한 뒤, 원하는 data를 정리하는 과정도 필요하다.
'''
