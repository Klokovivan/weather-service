from fastapi_cache import FastAPICache  
from fastapi_cache.backends.inmemory import InMemoryBackend 
from app.api import router as api_router

# Модули и объекты
from fastapi_cache import FastAPICache
from app.settings import LOG_PATH 
import logging
from fastapi import FastAPI
from app.api import router

# Cоздаем FastAPI приложениt
app = FastAPI()

#включаем маршрутизацию
app.include_router(router)


# Настраиваем логирование
logging.basicConfig(
    filename=LOG_PATH,  
    level=logging.ERROR,  
    format='%(asctime)s - weather_service - %(levelname)s - %(message)s'  
)

# Инициализация кэша
@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")

app.include_router(api_router)

