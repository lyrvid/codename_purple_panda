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


def test_medium_parcel():
    parcel = Parcel(width=9, height=9, depth=9)
    assert calculate_parcel_size(parcel) != ParcelSize.MEDIUM

    parcel = Parcel(width=10, height=10, depth=10)
    assert calculate_parcel_size(parcel) == ParcelSize.MEDIUM

    parcel = Parcel(width=49, height=49, depth=49)
    assert calculate_parcel_size(parcel) == ParcelSize.MEDIUM

    parcel = Parcel(width=49, height=5, depth=50)
    assert calculate_parcel_size(parcel) != ParcelSize.MEDIUM


def test_large_parcel():
    parcel = Parcel(width=49, height=49, depth=49)
    assert calculate_parcel_size(parcel) != ParcelSize.LARGE

    parcel = Parcel(width=50, height=50, depth=50)
    assert calculate_parcel_size(parcel) == ParcelSize.LARGE

    parcel = Parcel(width=99, height=99, depth=99)
    assert calculate_parcel_size(parcel) == ParcelSize.LARGE

    parcel = Parcel(width=99, height=5, depth=100)
    assert calculate_parcel_size(parcel) != ParcelSize.LARGE


def test_extra_large_parcel():
    parcel = Parcel(width=99, height=99, depth=99)
    assert calculate_parcel_size(parcel) != ParcelSize.EXTRA_LARGE

    parcel = Parcel(width=100, height=100, depth=100)
    assert calculate_parcel_size(parcel) == ParcelSize.EXTRA_LARGE

    parcel = Parcel(width=9999, height=99999, depth=9999999999)
    assert calculate_parcel_size(parcel) == ParcelSize.EXTRA_LARGE
