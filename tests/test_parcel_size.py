from models import Parcel, ParcelSize
from pricing import calculate_parcel_size


def test_small_parcel():
    parcel = Parcel(width=1, height=1, depth=1)
    assert calculate_parcel_size(parcel) == ParcelSize.SMALL

    parcel = Parcel(width=9, height=9, depth=9)
    assert calculate_parcel_size(parcel) == ParcelSize.SMALL

    parcel = Parcel(width=1, height=5, depth=9)
    assert calculate_parcel_size(parcel) == ParcelSize.SMALL

    parcel = Parcel(width=1, height=5, depth=10)
    assert calculate_parcel_size(parcel) != ParcelSize.SMALL
