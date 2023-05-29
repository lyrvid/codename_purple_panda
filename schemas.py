from pydantic import BaseModel
from enum import Enum, auto
from typing import List


class ParcelSize(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    EXTRA_LARGE = auto()


class Parcel(BaseModel):
    width: int
    height: int
    depth: int


class ParcelResponse(BaseModel):
    size: ParcelSize
    cost: int

    def __str__(self):
        return f'{self.size.name} parcel: ${self.cost}.'


class ParcelResponses(BaseModel):
    parcels: List[ParcelResponse]
    total: int

    def __str__(self):
        return f'{" ".join((str(p) for p in self.parcels))} Total Cost: ${self.total}.'


class ParcelInput(BaseModel):
    parcels: List[Parcel]