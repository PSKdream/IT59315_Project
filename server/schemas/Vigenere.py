from pydantic import BaseModel, Field


class Vigenere(BaseModel):
    text: str = Field(..., description="Add text")
    key: str = Field(..., description="Add key")

    class Config:
        schema_extra = {
            "example": {
                "text": "buffalo",
                "key": "view"
            }
        }
