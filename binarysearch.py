def binary_search(arr, target):
    # pred(i) must be False…False, True…True (monotone)
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] >= target:          # mid is on the True side
            hi = mid           # keep left half (could still be the first True)
        else:                  # mid is on the False side
            lo = mid + 1       # keep right half
    return lo if lo < len(arr) and arr[lo] == target else -1                  # first index where pred is True


def greatest_less_than(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo if lo < len(arr) else -1

def smallest_greater_than(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo if lo < len(arr) else -1


# Test block
if __name__ == "__main__":
    # Test array
    test_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    
    # Test binary_search
    assert binary_search(test_arr, 7) == 3, "binary_search(test_arr, 7) should return 3"
    assert binary_search(test_arr, 10) == -1, "binary_search(test_arr, 10) should return -1"
    
    # Test greatest_less_than
    assert greatest_less_than(test_arr, 7) == 2, "greatest_less_than(test_arr, 7) should return 2"
    assert greatest_less_than(test_arr, 0) == -1, "greatest_less_than(test_arr, 0) should return -1"
    
    # Test smallest_greater_than
    assert smallest_greater_than(test_arr, 7) == 4, "smallest_greater_than(test_arr, 7) should return 4"
    assert smallest_greater_than(test_arr, 15) == -1, "smallest_greater_than(test_arr, 15) should return -1"

    # Pathological edge cases
    empty_arr = []
    assert binary_search(empty_arr, 1) == -1, "binary_search on empty array should return -1"
    assert greatest_less_than(empty_arr, 1) == -1, "greatest_less_than on empty array should return -1"
    assert smallest_greater_than(empty_arr, 1) == -1, "smallest_greater_than on empty array should return -1"

    single_arr = [1]
    assert binary_search(single_arr, 1) == 0, "binary_search on single element array should return 0"
    assert binary_search(single_arr, 2) == -1, "binary_search on single element array with non-existent target should return -1"
    assert greatest_less_than(single_arr, 1) == -1, "greatest_less_than on single element array with target equal to element should return -1"
    assert smallest_greater_than(single_arr, 1) == -1, "smallest_greater_than on single element array with target equal to element should return -1"

    duplicate_arr = [1, 1, 1, 1, 1]
    assert binary_search(duplicate_arr, 1) in [0, 1, 2, 3, 4], "binary_search on array with duplicates should return any valid index"
    assert greatest_less_than(duplicate_arr, 1) == -1, "greatest_less_than on array with duplicates and target equal to elements should return -1"
    assert smallest_greater_than(duplicate_arr, 1) == -1, "smallest_greater_than on array with duplicates and target equal to elements should return -1"

    large_arr = list(range(1000000))
    assert binary_search(large_arr, 500000) == 500000, "binary_search on large array should work correctly"
    assert greatest_less_than(large_arr, 500000) == 499999, "greatest_less_than on large array should work correctly"
    assert smallest_greater_than(large_arr, 500000) == 500001, "smallest_greater_than on large array should work correctly"


