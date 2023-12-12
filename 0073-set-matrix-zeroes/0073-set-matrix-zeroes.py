class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    # Set the whole row to '.'
                    i = 0
                    while i < ROWS:
                        if matrix[i][col] != 0:
                            matrix[i][col] = '.'
                        i += 1
                    # Set the whole col to '.'
                    i = 0
                    while i < COLS:
                        if matrix[row][i] != 0:
                            matrix[row][i] = '.'
                        i += 1
    
        
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == '.':
                    matrix[row][col] = 0
