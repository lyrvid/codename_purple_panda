from pricing import calculate_parcel_cost
from schemas import Parcel


def test_parcel_cost():
    parcel = Parcel(width=1, height=1, depth=1)
    assert calculate_parcel_cost(parcel) == 3

    parcel = Parcel(width=10, height=10, depth=10)
    assert calculate_parcel_cost(parcel) == 8

    parcel = Parcel(width=50, height=50, depth=50)
    assert calculate_parcel_cost(parcel) == 15

    parcel = Parcel(width=100, height=100, depth=100)
    assert calculate_parcel_cost(parcel) == 25
