from pricing import calculate_weight_penalty
from schemas import Parcel


def test_parcel_weight_penalty():
    parcel = Parcel(width=1, height=1, depth=1, weight=2)
    assert calculate_weight_penalty(parcel) == 2

    parcel = Parcel(width=10, height=10, depth=10, weight=5)
    assert calculate_weight_penalty(parcel) == 4

    parcel = Parcel(width=50, height=50, depth=50, weight=8)
    assert calculate_weight_penalty(parcel) == 4

    parcel = Parcel(width=100, height=100, depth=100, weight=12)
    assert calculate_weight_penalty(parcel) == 4

