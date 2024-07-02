# Модули
from app.settings import BASEURL_GEOCODING, BASEURL_WEATHER, GEO_TOKEN, API_KEY, WEATHER_TOKEN
from fastapi import HTTPException
import logging 
import requests

# Отправляем запрос на сервис geocoding_cervice
# TODO возможно лучше разедлить запросы к сервисам на разные функции
async def get_weather(city: str): 
    if not city:
        raise HTTPException(status_code=523, detail="Ошибка при получении города")
    
    url = f"{BASEURL_GEOCODING}/coordinates"
    params = {"city": city}
    headers={"x-token": GEO_TOKEN}
    response = requests.get(url, headers=headers, params=params) # отправляем город и токен для проверки

    # Проверка статус кода
    if response.status_code != 200:
        error_message = f"Ошибка при запросе к openweatgermap.org для получения измерений температуры сервис геокодирования. Статус код: {response.status_code}, Ответ: {response.text}"
        logging.error(error_message)  # Логируем ошибку
        raise HTTPException(status_code=523, detail="Ошибка при запросе к сервису геокодирования")
        
    data = response.json() # Получаем ответ JSON

    if not data.get("lat") or not data.get("lon"):
        error_message = f"Ошибка при получении параметров lat, lon"
        logging.error(error_message)
        raise HTTPException(status_code=523, detail="Ошибка при получении параметров lat, lon")
    
    lat, lon = data["lat"], data["lon"] # Распаковываем в lat, lon

        
    # Отправляем координаты для получения погоды
    url = f"{BASEURL_WEATHER}/weather" 
    params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": 'metric'}
    headers = {"x-token": WEATHER_TOKEN}
    response = requests.get(url, headers=headers, params=params) 

    #Проверка статус кода
    if response.status_code != 200:
        error_message = f"Ошибка при запросе к openweatgermap.org для получения измерений температуры. Статус код: {response.status_code}, Ответ: {response.text}"
        logging.error(error_message)  # Логируем ошибку
        raise HTTPException(status_code=523, detail="Ошибка при запросе к openweatgermap.org для получения измерений температуры") 
    
    data = response.json()    
    
    if not data.get("main", {}).get("temp"):
        error_message = f"Ошибка при получении температуры в цельсиях"
        logging.error(error_message)
        raise HTTPException(status_code=523, detail="Ошибка при получении температуры в цельсиях")
    
    temp_celsius = data["main"]["temp"]

    
    temp_fahrenheit = temp_celsius * 9/5 + 32
    temp_kelvin = temp_celsius + 273.15

    temp = {
        "celsius": temp_celsius,         # °C
        "fahrenheit": temp_fahrenheit,   # °F
        "kelvin": temp_kelvin            # K
    }

    return temp