from collections import defaultdict


def max_sum_fixed_k(nums, k):
    """Return max sum of any length-k contiguous subarray."""
    if k <= 0:
        raise ValueError("k must be positive")
    if k > len(nums):
        raise ValueError("k cannot exceed len(nums)")

    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        if window > best:
            best = window
    return best


def min_subarray_len_at_least(target, nums):
    """Return minimal length of a contiguous subarray with sum >= target, or 0 if none.

    Assumes nums are non-negative.
    """
    left = 0
    window = 0
    best = float("inf")
    for right, x in enumerate(nums):
        window += x
        while window >= target and left <= right:
            best = min(best, right - left + 1)
            window -= nums[left]
            left += 1
    return 0 if best == float("inf") else best


def longest_substring_k_distinct(s, k):
    """Return length of the longest substring with at most k distinct characters."""
    if k < 0:
        raise ValueError("k cannot be negative")
    if k == 0:
        return 0

    counts = defaultdict(int)
    left = 0
    distinct = 0
    best = 0

    for right, ch in enumerate(s):
        if counts[ch] == 0:
            distinct += 1
        counts[ch] += 1

        while distinct > k:
            drop = s[left]
            counts[drop] -= 1
            if counts[drop] == 0:
                distinct -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    assert max_sum_fixed_k([1, 2, 3, 4], 2) == 7
    assert max_sum_fixed_k([-1, -2, -3], 1) == -1

    assert min_subarray_len_at_least(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_subarray_len_at_least(15, [1, 2, 3, 4, 5]) == 5
    assert min_subarray_len_at_least(100, [1, 2, 3]) == 0

    assert longest_substring_k_distinct("eceba", 2) == 3  # "ece"
    assert longest_substring_k_distinct("aa", 1) == 2
    assert longest_substring_k_distinct("", 2) == 0
