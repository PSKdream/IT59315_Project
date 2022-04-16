from pydantic import BaseModel, Field


class ColumnarTransposition(BaseModel):
    text: str = Field(..., description="Add text")
    key: str = Field(..., description="Add key")

    class Config:
        schema_extra = {
            "example": {
                "text": "buffalo view",
                "key": "2,3,1"
            }
        }

