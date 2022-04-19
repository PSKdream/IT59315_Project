import sys
from fastapi import APIRouter
from schemas.RailFence import RailFence as schema

sys.path.append("../")
import algorithm

route = APIRouter()
obj = algorithm.RailFence()

@route.post('/api/RailFence/encrypt')
async def encrypt(cts: schema):
    try:
        return obj.encrypt(cts.text, cts.key)
    except Exception as e:
        return str(e)


@route.post('/api/RailFence/decrypt')
async def decrypt(cts: schema):
    try:
        return obj.decrypt(cts.text, cts.key)
    except Exception as e:
        return str(e)
