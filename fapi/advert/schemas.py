from typing import Optional

from pydantic import BaseModel


class Advert(BaseModel):
    name: str
    price: int
    contact: str
    description: str

class EditAdvert(BaseModel):
    name: Optional[str]
    price: Optional[int]
    contact: Optional[str]
    description: Optional[str]