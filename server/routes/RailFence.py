import sys
from fastapi import APIRouter
from schemas.RailFence import RailFence as schema

sys.path.append("../")
import algorithm

route = APIRouter()
obj = algorithm.RailFence()

@route.post('/RailFence/encrypt')
async def encrypt(cts: schema):
    return obj.encrypt(cts.text, cts.key)


@route.post('/RailFence/decrypt')
async def encrypt(cts: schema):
    return obj.decrypt(cts.text, cts.key)
