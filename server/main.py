from fastapi import FastAPI
from routes.ColumnarTransposition import route as ct
from routes.Vigenere import route as vg

app = FastAPI()
app.include_router(ct)
app.include_router(vg)


@app.get("/")
async def root():
    return {"message": "Hello World"}
