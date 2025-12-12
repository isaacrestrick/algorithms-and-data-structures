def build_prefix_sum(nums):
    """Return prefix sums array ps where ps[i] = sum(nums[:i])."""
    ps = [0]
    running = 0
    for x in nums:
        running += x
        ps.append(running)
    return ps


def range_sum(ps, left, right):
    """Sum over the half-open range nums[left:right] using prefix sums ps."""
    if left < 0 or right < 0 or left > right or right >= len(ps):
        raise ValueError("invalid range")
    return ps[right] - ps[left]


def build_prefix_sum_2d(grid):
    """Return 2D prefix sums p where p[r+1][c+1] = sum(grid[:r+1][:c+1])."""
    if not grid or not grid[0]:
        return [[0]]

    rows, cols = len(grid), len(grid[0])
    p = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            p[r + 1][c + 1] = grid[r][c] + p[r][c + 1] + p[r + 1][c] - p[r][c]
    return p


def range_sum_2d(p, r1, c1, r2, c2):
    """Sum of sub-rectangle grid[r1:r2][c1:c2] (half-open) using 2D prefix sums p."""
    if r1 < 0 or c1 < 0 or r2 < 0 or c2 < 0 or r1 > r2 or c1 > c2:
        raise ValueError("invalid range")

    rows = len(p) - 1
    cols = len(p[0]) - 1
    if r2 > rows or c2 > cols:
        raise ValueError("range out of bounds")

    return p[r2][c2] - p[r1][c2] - p[r2][c1] + p[r1][c1]


if __name__ == "__main__":
    nums = [3, -2, 5, 1]
    ps = build_prefix_sum(nums)
    assert ps == [0, 3, 1, 6, 7]
    assert range_sum(ps, 0, 4) == 7
    assert range_sum(ps, 1, 3) == 3
    assert range_sum(ps, 2, 2) == 0

    grid = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    p = build_prefix_sum_2d(grid)
    assert range_sum_2d(p, 0, 0, 2, 3) == 21
    assert range_sum_2d(p, 0, 0, 1, 1) == 1
    assert range_sum_2d(p, 0, 1, 2, 3) == 2 + 3 + 5 + 6
    assert range_sum_2d(p, 1, 0, 2, 2) == 4 + 5
