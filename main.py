from fastapi import FastAPI
from schemas import ParcelResponse, ParcelResponses, ParcelInput, ParcelSize
from typing import List

from pricing import (
    calculate_parcel_size,
    calculate_parcel_cost,
    calculate_parcel_mania_discounts,
)

app = FastAPI()


def _get_parcel_pricing(parcel_input: ParcelInput):
    parcel_responses: List[ParcelResponse] = []
    total = 0
    for parcel in parcel_input.parcels:
        size = calculate_parcel_size(parcel)
        cost = calculate_parcel_cost(parcel)

        heavy_cost = calculate_parcel_cost(parcel, ParcelSize.HEAVY)

        if heavy_cost < cost:
            cost = heavy_cost
            size = ParcelSize.HEAVY

        response = ParcelResponse(size=size, cost=cost)
        parcel_responses.append(response)
        total += cost

    parcel_mania_discount = calculate_parcel_mania_discounts(parcel_responses)

    if parcel_mania_discount > 0:
        total = total - parcel_mania_discount

    speedy_shipping = 0
    if parcel_input.speedy_shipping:
        speedy_shipping = total
        total = total * 2
        parcel_mania_discount = parcel_mania_discount * 2

    return ParcelResponses(
        parcels=parcel_responses,
        total=total,
        speedy_shipping=speedy_shipping,
        discount=parcel_mania_discount * -1,
    )


@app.post("/")
async def get_parcel_pricing(parcel_input: ParcelInput):
    return _get_parcel_pricing(parcel_input)


@app.post("/text")
async def get_parcel_pricing(parcel_input: ParcelInput):
    response = _get_parcel_pricing(parcel_input)
    return str(response)
