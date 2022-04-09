import sys
from fastapi import APIRouter
from schemas.ColumnarTransposition import ColumnarTransposition as schema
sys.path.append("../")
import algorithm

ct = APIRouter()

@ct.post('/ColumnarTransposition/encrypt')
async def encrypt(cts:schema):
    obj = algorithm.ColumnarTransposition()
    return obj.encrypt(cts.plan_text,cts.key)

@ct.post('/ColumnarTransposition/decrypt')
async def encrypt(cts:schema):
    obj = algorithm.ColumnarTransposition()
    return obj.decrypt(cts.plan_text,cts.key)