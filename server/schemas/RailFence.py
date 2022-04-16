from pydantic import BaseModel, Field


class RailFence(BaseModel):
    text: str = Field(..., description="Add text")
    key: int = Field(..., description="Add key")

    class Config:
        schema_extra = {
            "example": {
                "text": "fuck you",
                "key": 3
            }
        }
