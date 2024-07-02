
#импортируем модули и функции
from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi_cache.decorator import cache 
from fastapi.responses import JSONResponse
from app.middleware import verify_token
from app.utils import get_weather
import logging

#маршрутизация
router = APIRouter()



@router.get("/weather")
@cache(expire=360)  # Кеширование на 60 секунд
async def weather(
    city: str = Query(..., min_length=1, max_length=50, description="Город для получения погоды"), 
    token: str = Depends(verify_token)):
 
    coordinates = await get_weather(city)
    if not coordinates:
       raise HTTPException(status_code=523, detail="Ошибка при получении координат")
    return JSONResponse(coordinates)   
    
    

