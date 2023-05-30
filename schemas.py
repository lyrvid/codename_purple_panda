from pydantic import BaseModel
from enum import Enum, auto
from typing import List


class ParcelSize(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    EXTRA_LARGE = auto()
    HEAVY = auto()


class Parcel(BaseModel):
    width: int
    height: int
    depth: int
    weight: int = 0


class ParcelResponse(BaseModel):
    size: ParcelSize
    cost: int

    def __str__(self):
        return f"{self.size.name} parcel: ${self.cost}."

    def __hash__(self):
        return hash(id(self))


class ParcelResponses(BaseModel):
    parcels: List[ParcelResponse]
    total: int
    speedy_shipping: int = 0
    discount: int = 0

    def __str__(self):
        return (
            f'{" ".join((str(p) for p in self.parcels))} Discount: ${self.discount}. Speedy shipping Cost: '
            f"${self.speedy_shipping}. Total Cost: ${self.total}."
        )


class ParcelInput(BaseModel):
    parcels: List[Parcel]
    speedy_shipping: bool = False
