from fastapi import FastAPI
from routes.ColumnarTransposition import ct

app = FastAPI()
app.include_router(ct)
@app.get("/")
async def root():
    return {"message": "Hello World"}