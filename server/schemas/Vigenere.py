from pydantic import BaseModel
class Vigenere(BaseModel):
    text: str
    key: str
