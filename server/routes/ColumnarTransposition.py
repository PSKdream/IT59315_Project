import sys
from fastapi import APIRouter
from schemas.ColumnarTransposition import ColumnarTransposition as schema

sys.path.append("../")
import algorithm

route = APIRouter()


@route.post('/ColumnarTransposition/encrypt')
async def encrypt(cts: schema):
    obj = algorithm.ColumnarTransposition()
    return obj.encrypt(cts.text, cts.key)


@route.post('/ColumnarTransposition/decrypt')
async def encrypt(cts: schema):
    obj = algorithm.ColumnarTransposition()
    return obj.decrypt(cts.text, cts.key)
