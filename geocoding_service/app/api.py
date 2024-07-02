# Модули и функции
from fastapi import APIRouter, Depends, HTTPException, FastAPI, Query
from fastapi_cache.decorator import cache

from app.utils import get_coordinates
from app.middleware import verify_token
import logging


# Маршрутизатор
router = APIRouter()
app = FastAPI()


# Маршрут для получения координат
@router.get("/coordinates")
@cache(expire=360)  # Кеширование на 360 секунд
async def coordinates(
    city: str = Query(..., min_length=1, max_length=50, description="Город для получения координат"), 
    token: str = Depends(verify_token)
): 
    
    coord = await get_coordinates(city)

    if not coord:
        raise HTTPException(status_code=523, detail="Ошибка при получении координат")
    return coord 
    