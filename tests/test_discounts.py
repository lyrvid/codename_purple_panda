from pricing import calculate_parcel_mania_discounts
from schemas import ParcelResponse, ParcelSize


def test_small_discounts():
    parcels = [
        ParcelResponse(size=ParcelSize.SMALL, cost=6),
        ParcelResponse(size=ParcelSize.SMALL, cost=8),
        ParcelResponse(size=ParcelSize.SMALL, cost=11),
        ParcelResponse(size=ParcelSize.SMALL, cost=3),
        ParcelResponse(size=ParcelSize.SMALL, cost=2),
        ParcelResponse(size=ParcelSize.SMALL, cost=2),
        ParcelResponse(size=ParcelSize.SMALL, cost=2),
        ParcelResponse(size=ParcelSize.SMALL, cost=2),
    ]

    assert calculate_parcel_mania_discounts(parcels[0:3]) == 0
    assert calculate_parcel_mania_discounts(parcels[0:4]) == 3
    assert calculate_parcel_mania_discounts(parcels) == 5


def test_medium_discounts():
    parcels = [
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=10),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=10),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=10),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=2),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=2),
    ]

    assert calculate_parcel_mania_discounts(parcels[0:2]) == 0
    assert calculate_parcel_mania_discounts(parcels[0:4]) == 8
    assert calculate_parcel_mania_discounts(parcels) == 18


def test_medium_discounts_all_same():
    parcels = [
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
    ]

    assert calculate_parcel_mania_discounts(parcels) == 16


def test_mixed_discounts():
    parcels = [
        ParcelResponse(size=ParcelSize.LARGE, cost=6),
        ParcelResponse(size=ParcelSize.LARGE, cost=8),
        ParcelResponse(size=ParcelSize.LARGE, cost=11),
        ParcelResponse(size=ParcelSize.LARGE, cost=3),
        ParcelResponse(size=ParcelSize.LARGE, cost=4),
        ParcelResponse(size=ParcelSize.LARGE, cost=4),
    ]

    assert calculate_parcel_mania_discounts(parcels) == 3


def test_multiple_discounts():
    parcels = [
        ParcelResponse(size=ParcelSize.LARGE, cost=6),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=8),
        ParcelResponse(size=ParcelSize.LARGE, cost=11),
        ParcelResponse(size=ParcelSize.LARGE, cost=3),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=103),
        ParcelResponse(size=ParcelSize.MEDIUM, cost=50),
    ]

    assert calculate_parcel_mania_discounts(parcels) == 11
