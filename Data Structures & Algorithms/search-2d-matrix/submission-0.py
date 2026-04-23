class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])  # all rows are of same length
        L = 0
        R = rowLen * len(matrix) - 1
        while L <= R:
            mid = (L + R) // 2
            i = mid // rowLen
            j = mid % rowLen

            if target < matrix[i][j]:
                R = mid - 1
            elif target > matrix[i][j]:
                L = mid + 1
            else:
                return True
        return False
