import heapq


def k_smallest(nums, k):
    """Return the k smallest values from nums (ascending)."""
    if k < 0:
        raise ValueError("k must be >= 0")
    return heapq.nsmallest(k, nums)


if __name__ == "__main__":
    print(k_smallest([5, 1, 4, 2, 3], 3))
