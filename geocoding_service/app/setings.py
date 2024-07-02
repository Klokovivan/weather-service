import os

#Подтягиваем значения из параметров окружения
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

GEO_TOKEN = os.getenv("GEOCODING_SERVICE_TOKEN")

BASE_URL_GEO = os.getenv("BASE_URL_GEO")

LOG_PATH = os.getenv("LOG_PATH")