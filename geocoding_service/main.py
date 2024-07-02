from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from app.setings import LOG_PATH 
import logging
from fastapi import FastAPI
from app.api import router


#Cоздаем FastAPI приложениt
app = FastAPI()

# Включаем маршрутизацию
app.include_router(router)


# Настраиваем логирование
logging.basicConfig(
    filename=LOG_PATH,  # Имя файла для логов
    level=logging.ERROR,  # Уровень логирования
    format='%(asctime)s - geocoding_service - %(levelname)s - %(message)s'  # Формат логов
)

# Инициализация кэша
@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())




