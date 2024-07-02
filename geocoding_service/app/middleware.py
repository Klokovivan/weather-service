#МMIDLWARE
from fastapi import Header, HTTPException
from typing_extensions import Annotated
from app.setings import GEO_TOKEN 

#Проверка токена GEO
async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != GEO_TOKEN:
        raise HTTPException(status_code=401, detail=f"{x_token, GEO_TOKEN}")
    return x_token
    