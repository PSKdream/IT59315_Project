import sys
from fastapi import APIRouter
from schemas.RSA import RSA as schema
from schemas.RSA import KeySize
import base64
import json

sys.path.append("../")
import algorithm

route = APIRouter()
obj = algorithm.RSA()


@route.post('/RSA/GenerateKey')
async def generateKey(cts: KeySize):
    try:
        public_key, private_key = obj.generateKey(cts.keySize)
        public_key = base64.b64encode(json.dumps(public_key).encode())
        private_key = base64.b64encode(json.dumps(private_key).encode())
        obj_json = {'public_key': public_key,
                    'private_key': private_key}
        return obj_json
    except Exception as e:
        return str(e)


@route.post('/RSA/encrypt')
async def encrypt(cts: schema):
    try:
        key = json.loads(base64.b64decode(cts.key).decode())
        message = obj.encrypt(cts.text, key)
        message_bytes = str(message).encode()
        text = base64.b64encode(message_bytes)
        return text
    except Exception as e:
        return str(e)

@route.post('/RSA/decrypt')
async def decrypt(cts: schema):
    try:
        key = json.loads(base64.b64decode(cts.key).decode())
        message = base64.b64decode(cts.text).decode()
        return str(obj.decrypt(int(message), key))
    except Exception as e:
        return str(e)