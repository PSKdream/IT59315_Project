from fastapi import FastAPI
from routes.ColumnarTransposition import route as ct
from routes.Vigenere import route as vg
from routes.RSA import route as rsa
from routes.RailFence import route as rf


app = FastAPI()
app.include_router(ct)
app.include_router(vg)
app.include_router(rsa)
app.include_router(rf)

@app.get("/")
async def root():
    return {"message": "Hello World"}
