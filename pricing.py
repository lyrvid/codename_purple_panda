from schemas import Parcel, ParcelSize


PARCEL_SIZE_LIMITS = [
    (ParcelSize.SMALL, 10),
    (ParcelSize.MEDIUM, 50),
    (ParcelSize.LARGE, 100),
    (ParcelSize.EXTRA_LARGE, -1),
]

PARCEL_SIZE_WEIGHT_LIMITS = {
    ParcelSize.SMALL: 1,
    ParcelSize.MEDIUM: 3,
    ParcelSize.LARGE: 6,
    ParcelSize.EXTRA_LARGE: 10,
    ParcelSize.HEAVY: 50,
}

PARCEL_SIZE_WEIGHT_PENALTY = {
    ParcelSize.SMALL: 2,
    ParcelSize.MEDIUM: 2,
    ParcelSize.LARGE: 2,
    ParcelSize.EXTRA_LARGE: 2,
    ParcelSize.HEAVY: 1,
}

PARCEL_SIZE_TO_BASE_COST = {
    ParcelSize.SMALL: 3,
    ParcelSize.MEDIUM: 8,
    ParcelSize.LARGE: 15,
    ParcelSize.EXTRA_LARGE: 25,
    ParcelSize.HEAVY: 50,
}


def calculate_parcel_size(parcel: Parcel) -> ParcelSize:
    max_dimension = max(parcel.depth, parcel.width, parcel.height)

    # Iterate over sizes and return the smallest the parcel fits in to
    for size, limit in PARCEL_SIZE_LIMITS:
        if max_dimension < limit:
            return size

    # Default to the largest possible size
    return PARCEL_SIZE_LIMITS[-1][0]


def calculate_parcel_cost(parcel: Parcel, size: ParcelSize = None) -> int:
    size = size or calculate_parcel_size(parcel)
    weight_penalty = calculate_weight_penalty(parcel, size)
    cost = PARCEL_SIZE_TO_BASE_COST[size] + weight_penalty
    return cost


def calculate_weight_penalty(parcel: Parcel, size: ParcelSize = None) -> int:
    size = size or calculate_parcel_size(parcel)
    limit = PARCEL_SIZE_WEIGHT_LIMITS[size]
    penalty = PARCEL_SIZE_WEIGHT_PENALTY[size]

    if parcel.weight > limit:
        return (parcel.weight - limit) * penalty
    return 0
