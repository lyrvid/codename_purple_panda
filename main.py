from fastapi import FastAPI, Response
from schemas import Parcel, ParcelResponse, ParcelResponses, ParcelInput
from typing import List

from pricing import calculate_parcel_size, calculate_parcel_cost

app = FastAPI()


def _get_parcel_pricing(
        parcel_input: ParcelInput
):

    parcel_responses: List[ParcelResponse] = []
    total = 0
    for parcel in parcel_input.parcels:
        size = calculate_parcel_size(parcel)
        cost = calculate_parcel_cost(parcel)

        response = ParcelResponse(size=size, cost=cost)
        parcel_responses.append(response)
        total += cost

    return ParcelResponses(parcels=parcel_responses, total=total)


@app.post("/")
async def get_parcel_pricing(
        parcel_input: ParcelInput
):
    return _get_parcel_pricing(parcel_input)


@app.post("/text")
async def get_parcel_pricing(
        parcel_input: ParcelInput
):

    response = _get_parcel_pricing(parcel_input)
    return str(response)
