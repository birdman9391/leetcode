class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        for i, cell in enumerate(obstacleGrid[0]):
            if i == 0:
                obstacleGrid[0][i] = 1 - obstacleGrid[0][i]
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1] * (1 - obstacleGrid[0][i])

        # print(obstacleGrid[0])
        for i, row in enumerate(obstacleGrid):
            if i == 0:
                continue
            for j, cell in enumerate(row):
                if cell:
                    obstacleGrid[i][j] = 0
                elif j == 0:
                    obstacleGrid[i][0] = obstacleGrid[i-1][0]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                    
        # print(obstacleGrid)
        return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]