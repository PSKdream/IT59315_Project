from pydantic import BaseModel, Field
class RSA(BaseModel):
    text: str = Field(..., description="Add text")
    key: str = Field(..., description="Add key")

    class Config:
        schema_extra = {
            "example": {
                "text": "buffalo view",
                "key": "eyJlIjogNTI2MSwgIm4iOiA4NTA3fQ=="
            }
        }

class KeySize(BaseModel):
    keySize: int = Field(..., description="Add key size")

    class Config:
        schema_extra = {
            "example": {
                "keySize": 256,
            }
        }