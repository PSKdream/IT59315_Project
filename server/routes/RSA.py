import sys
from fastapi import APIRouter
from schemas.RSA import RSA as schema
import base64

sys.path.append("../")
import algorithm

route = APIRouter()
obj = algorithm.RSA()

@route.get('/RSA/GenerateKey')
async def encrypt():
    key = obj.generateKey()
    json = {'public_key': key[0],
            'private_key': key[1]}
    return json

@route.post('/RSA/encrypt')
async def encrypt(cts: schema):
    key = [int(i)for i in cts.key[1:-1].split(',')]
    message = obj.encrypt(cts.text, key)
    message_bytes = message.encode()
    text = base64.b64encode(message_bytes)
    return text


@route.post('/RSA/decrypt')
async def encrypt(cts: schema):
    key = [int(i)for i in cts.key[1:-1].split(',')]
    message = base64.b64decode(cts.text).decode()
    return obj.decrypt(message, key)
