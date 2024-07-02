# MIDDLEWARE
from fastapi import Header, HTTPException
from typing_extensions import Annotated
from app.settings import WEATHER_TOKEN 

# Проверка токена WEATHER
async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != WEATHER_TOKEN:
        raise HTTPException(status_code=401, detail=f"{x_token, WEATHER_TOKEN}")
    return x_token