class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # taking transpose
        for row in range(len(matrix)):
            # running only in upper matrix
            # to avoid double replacement
            for col in range(row,len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # exchanging columns
        for row in range(len(matrix)):
            l, r = 0, len(matrix[row])-1
            
            while l < r:
                matrix[row][l],matrix[row][r] = matrix[row][r],matrix[row][l]
                l += 1
                r -= 1
        