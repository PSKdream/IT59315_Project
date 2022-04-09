import sys
from fastapi import APIRouter
from schemas.Vigenere import Vigenere as schema

sys.path.append("../")
import algorithm

route = APIRouter()


@route.post('/Vigenere/encrypt')
async def encrypt(cts: schema):
    obj = algorithm.Vigenere()
    return obj.encrypt(cts.text, cts.key)


@route.post('/Vigenere/decrypt')
async def encrypt(cts: schema):
    obj = algorithm.Vigenere()
    return obj.decrypt(cts.text, cts.key)
