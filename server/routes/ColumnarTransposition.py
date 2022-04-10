import sys
from fastapi import APIRouter
from schemas.ColumnarTransposition import ColumnarTransposition as schema

sys.path.append("../")
import algorithm

route = APIRouter()


@route.post('/ColumnarTransposition/encrypt')
async def encrypt(cts: schema):
    obj = algorithm.ColumnarTransposition()
<<<<<<< HEAD
    return obj.encrypt(cts.text,cts.key)
=======
    return obj.encrypt(cts.text, cts.key)

>>>>>>> ea7699b264d38236f55254d352c37230392727b6

@route.post('/ColumnarTransposition/decrypt')
async def encrypt(cts: schema):
    obj = algorithm.ColumnarTransposition()
<<<<<<< HEAD
    return obj.decrypt(cts.text,cts.key)
=======
    return obj.decrypt(cts.text, cts.key)
>>>>>>> ea7699b264d38236f55254d352c37230392727b6
