class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        center = (N - 1) / 2

        top_left_range = [(N + 1) // 2, N // 2]
        
        for i in range(top_left_range[0]):
            for j in range(top_left_range[1]):
                x, y = i - center, j - center
                
                tmp = matrix[i][j]
                
                for _ in range(3):
                    matrix[int(x + center)][int(y + center)] = matrix[int(-y + center)][int(x + center)]
                    x, y = -y, x

                matrix[int(x + center)][int(y + center)] = tmp