class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix) * len(matrix[0]) - 1
        while L <= R:
            mid = (L + R) // 2
            x = mid // len(matrix[0])
            y = mid % len(matrix[0])
            if target < matrix[x][y]:
                R = mid - 1
            elif target > matrix[x][y]:
                L = mid + 1
            else:
                return True
        return False
