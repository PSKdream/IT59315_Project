from fastapi import FastAPI, Request
from routes.ColumnarTransposition import route as ct
from routes.Vigenere import route as vg
from routes.RSA import route as rsa
from routes.RailFence import route as rf

from fastapi.responses import FileResponse

import os

app = FastAPI()
app.include_router(ct)
app.include_router(vg)
app.include_router(rsa)
app.include_router(rf)

folder = '../app/dist/'

@app.get('/')
@app.get('/app/{catchall:path}')
def index(request: Request):
    return FileResponse(folder + "index.html")

@app.get('/js/{catchall:path}', response_class=FileResponse)
def index(request: Request):
    path = request.path_params["catchall"]
    file = folder+'js/' + path
    if os.path.exists(file):
        return FileResponse(file)

@app.get('/css/{catchall:path}', response_class=FileResponse)
def index(request: Request):
    path = request.path_params["catchall"]
    file = folder+'css/' + path
    if os.path.exists(file):
        return FileResponse(file)
