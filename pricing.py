from models import Parcel, ParcelSize


PARCEL_SIZE_LIMITS = [
    (ParcelSize.SMALL, 10),
    (ParcelSize.MEDIUM, 50),
    (ParcelSize.LARGE, 100),
    (ParcelSize.EXTRA_LARGE, -1),
]


def calculate_parcel_size(parcel: Parcel) -> ParcelSize:
    max_dimension = max(parcel.depth, parcel.width, parcel.height)

    # Iterate over sizes and return the smallest the parcel fits in to
    for size, limit in PARCEL_SIZE_LIMITS:
        if max_dimension < limit:
            return size

    # Default to the largest possible size
    return PARCEL_SIZE_LIMITS[-1][0]
