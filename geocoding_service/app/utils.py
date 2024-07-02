# модули
from fastapi import HTTPException
from app.setings import API_KEY, BASE_URL_GEO
import logging
import requests


# Функция get_coordinates
async def get_coordinates(city: str):  
    
    url = f"{BASE_URL_GEO}"
    params={"q": city, "limit": 1, "appid": API_KEY}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        error_message = f"Ошибка при запросе к openweathermap.org для перевода города в координаты. Статус код: {response.status_code}, Ответ: {response.text}"
        logging.error(error_message)
        raise HTTPException(status_code=523, detail="Ошибка при запросе к openweathermap.org для перевода города в координаты")
    
    data = response.json() 

    if not data:
        error_message = f"Ошибка при получении параметров data при обращении к openweathermap.org GEO"
        logging.error(error_message)
        raise HTTPException(status_code=523, detail="Ошибка при получении параметров data при обращении к openweathermap.org GEO")
    
    if not (data[0].get("lat")) or not (data[0].get("lon")):
        error_message = f"Ошибка при получении параметров lat, lon при обращении к openweathermap.org GEO"
        logging.error(error_message)
        raise HTTPException(status_code=523, detail="Ошибка при получении параметров lat, lon при обращении к openweathermap.org GEO")

    coord = {
            "city": city,         
            "lat": data[0]["lat"],
            "lon": data[0]["lon"]
        }
    
    return coord #Возвращаем ответ
    
    


      

