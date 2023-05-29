from pydantic import BaseModel
from enum import Enum, auto


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
    parcels: None
    total: int
