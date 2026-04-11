class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1


        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
            
        return False