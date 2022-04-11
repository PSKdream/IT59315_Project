from pydantic import BaseModel
class RSA(BaseModel):
    text: str
    key: str
