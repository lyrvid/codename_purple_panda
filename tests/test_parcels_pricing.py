from main import _get_parcel_pricing
from schemas import Parcel, ParcelInput


def test_get_parcel_pricing_total():
    parcels = [
        Parcel(width=1, height=1, depth=1),
    ]

    result = _get_parcel_pricing(ParcelInput(parcels=parcels))
    assert result.total == 3

    parcels = [
        Parcel(width=1, height=1, depth=1),
        Parcel(width=10, height=10, depth=10),
    ]

    result = _get_parcel_pricing(ParcelInput(parcels=parcels))
    assert result.total == 11
