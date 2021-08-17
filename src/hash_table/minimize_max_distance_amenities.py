from collections import defaultdict
from typing import List

import numpy as np


def resolve_minimize_max_distance_to_amenities(
        amenities: List[str],
        block_to_amenities: List[List[str]],
        requirements: List[str]
) -> int:
    """
    Assuming you're looking to move and have a set of amenities that you want to have
    easy access to from your new home. You have found a neighborhood you like,
    each block of which has zero or more amenities. How would you pick the block to live in such
    that the farthest distance to any amenity in your list is minimized?

    Example:
        input:
        amenities = [[restaurant, grocery], [movie theater], [school], [], [school]]
        required = [school, grocery]

        output:
        block_idx = 2

    """

    pointer_right = pointer_left = 0
    # Count amenities in the current window
    counter = defaultdict(int)

    reached_amenities = []
    while pointer_right < len(block_to_amenities):
        current_amenities = block_to_amenities[pointer_right]
        for amenity in current_amenities:
            counter[amenity] += 1

        reached_amenities.append(block_to_amenities[pointer_right])

        if set(reached_amenities) == set(requirements):
            counter[pointer_left] = pointer_right

