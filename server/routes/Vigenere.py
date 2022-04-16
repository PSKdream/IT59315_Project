import sys
from fastapi import APIRouter
from schemas.Vigenere import Vigenere as schema

sys.path.append("../")
import algorithm

route = APIRouter()
obj = algorithm.Vigenere()

@route.post('/Vigenere/encrypt')
async def encrypt(cts: schema):
    return obj.encrypt(cts.text, cts.key)


@route.post('/Vigenere/decrypt')
async def decrypt(cts: schema):
    return obj.decrypt(cts.text, cts.key)
