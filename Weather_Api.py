import requests
from datetime import datetime
import sqlite3

API_KEY = '505243b0dd8c812e1a716cb5c5c4fed6'
URL = 'http://api.openweathermap.org/data/2.5/weather'

if __name__ == "__main__":
    city = 'Hwaseong'
    r = requests.get(URL, params={'q': 'Hwaseong',
                                  'APPID': API_KEY, 'units': 'metric'})
    data = r.json()
    wind_speed = data["wind"]["speed"]
    country = data["sys"]["country"]
    weather = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    now = datetime.now()
    Date = now.year, now.month, now.day
    Time = now.hour, now.minute, now.second

    db = sqlite3.connect("Weather_data/weather.db")
    cursor = db.cursor()
    insert_query = \
        f"INSERT INTO Weather VALUES('{Date}', '{Time}', '{country}', '{city}','{weather}','{wind_speed}','{temp}')"
    cursor.execute(insert_query)
    db.commit()

    cursor.execute("SELECT * FROM Weather")
    print(cursor.fetchall())  # 모든행 읽기

    db.close()
