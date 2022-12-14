from typing import List
from pydantic import BaseModel


class Contract(BaseModel):
    name: str
    start: int
    duration: int
    price: int


class Solution(BaseModel):
    income: int = 0
    path: List[str]
