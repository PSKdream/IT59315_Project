import sys
from fastapi import APIRouter
from schemas.ColumnarTransposition import ColumnarTransposition as schema

sys.path.append("../")
import algorithm

route = APIRouter()
obj = algorithm.ColumnarTransposition()


@route.post('/ColumnarTransposition/encrypt')
async def encrypt(cts: schema):
    return obj.encrypt(cts.text, cts.key)


@route.post('/ColumnarTransposition/decrypt')
async def decrypt(cts: schema):
    return obj.decrypt(cts.text, cts.key)
