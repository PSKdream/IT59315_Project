from pydantic import BaseModel
class RailFence(BaseModel):
    text: str
    key: int
