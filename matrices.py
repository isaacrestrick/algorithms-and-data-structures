from typing import List


def rotate(matrix):
    for layer in range(len(matrix) // 2):
        #print(layer, range(layer, len(matrix) - layer - 1))

        for start in range(layer, len(matrix) - 1 - layer):
            # start starts at layer

            upper_left = matrix[layer][start] #
            #print(layer, upper_left)

            upper_right = matrix[start][len(matrix) - 1 - layer] #
            #print(layer, upper_right)
            
            bottom_right = matrix[len(matrix) - 1 - layer][len(matrix) - 1 - start] #
            #print(layer, bottom_right)

            bottom_left = matrix[len(matrix) - 1 - start][layer] #
            #print(layer, bottom_left)

            #upper_left, upper_right, bottom_right, bottom_left = bottom_left, upper_left, upper_right, bottom_right
            matrix[layer][start] = bottom_left
            matrix[start][len(matrix) - 1 - layer] = upper_left
            matrix[len(matrix) - 1 - layer][len(matrix) - 1 - start] = upper_right
            matrix[len(matrix) - 1 - start][layer] = bottom_right
            
    return matrix

def spiral_order(matrix: List[List[int]]):
    ans = []
    while matrix and matrix[0]:
        # the top row
        if not matrix or not matrix[0]:
            return ans
        top_row = matrix.pop(0)
        ans.extend(top_row)

        # the right column
        if not matrix or not matrix[0]:
            return ans

        right_col = []
        for row_index in range(len(matrix)):
            right_col.append(matrix[row_index].pop(-1))
        
        ans.extend(right_col)

        # the bottom row
        if not matrix or not matrix[0]:
            return ans

        bottom_row = matrix.pop(-1)
        ans.extend(reversed(bottom_row))

        # left column
        if not matrix or not matrix[0]:
            return ans

        left_col = []
        for row_index in reversed(range(len(matrix))):
            left_col.append(matrix[row_index].pop(0))
        
        ans.extend(left_col)

    return ans

def set_zeroes(matrix: List[List[int]]):
    """If an element is 0, set its entire row and column to 0. In-place."""
    m, n = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    for i in range(m):
        for j in range(n):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0


# ==================== TEST CASES ====================

if __name__ == "__main__":
    import copy
    
    def test_rotate():
        print("Testing rotate()...")
        
        # 3x3 matrix
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = rotate(copy.deepcopy(matrix))
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        assert result == expected, f"3x3 failed: got {result}"
        
        # 4x4 matrix
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        result = rotate(copy.deepcopy(matrix))
        expected = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        assert result == expected, f"4x4 failed: got {result}"
        
        # 2x2 matrix
        matrix = [[1, 2], [3, 4]]
        result = rotate(copy.deepcopy(matrix))
        expected = [[3, 1], [4, 2]]
        assert result == expected, f"2x2 failed: got {result}"
        
        # 1x1 matrix
        matrix = [[1]]
        result = rotate(copy.deepcopy(matrix))
        expected = [[1]]
        assert result == expected, f"1x1 failed: got {result}"
        
        print("✓ All rotate tests passed!\n")
    
    def test_spiral_order():
        print("Testing spiral_order()...")
        
        # 3x3 matrix
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = spiral_order(copy.deepcopy(matrix))
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        assert result == expected, f"3x3 failed: got {result}"
        
        # 3x4 matrix (non-square)
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        result = spiral_order(copy.deepcopy(matrix))
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        assert result == expected, f"3x4 failed: got {result}"
        
        # Single row
        matrix = [[1, 2, 3, 4]]
        result = spiral_order(copy.deepcopy(matrix))
        expected = [1, 2, 3, 4]
        assert result == expected, f"Single row failed: got {result}"
        
        # Single column
        matrix = [[1], [2], [3]]
        result = spiral_order(copy.deepcopy(matrix))
        expected = [1, 2, 3]
        assert result == expected, f"Single column failed: got {result}"
        
        print("✓ All spiral_order tests passed!\n")
    
    def test_set_zeroes():
        print("Testing set_zeroes()...")
        
        # Basic case
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        set_zeroes(matrix)
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        assert matrix == expected, f"Basic failed: got {matrix}"
        
        # Multiple zeroes
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        set_zeroes(matrix)
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        assert matrix == expected, f"Multiple zeroes failed: got {matrix}"
        
        # No zeroes
        matrix = [[1, 2], [3, 4]]
        set_zeroes(matrix)
        expected = [[1, 2], [3, 4]]
        assert matrix == expected, f"No zeroes failed: got {matrix}"
        
        # All zeroes
        matrix = [[0, 0], [0, 0]]
        set_zeroes(matrix)
        expected = [[0, 0], [0, 0]]
        assert matrix == expected, f"All zeroes failed: got {matrix}"
        
        print("✓ All set_zeroes tests passed!\n")
    
    # Run all tests
    test_rotate()
    test_spiral_order()
    test_set_zeroes()
    print("🎉 All tests passed!")
