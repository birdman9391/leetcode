class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[False for _ in range(n)] for __ in range(n)]

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        cx, cy = 0, 0
        direction = 0
        
        for i in range(1, n ** 2+1):
            answer[cy][cx] = i
            nx, ny = cx + dx[direction], cy + dy[direction]
            try:
                if answer[ny][nx]:
                    direction = (direction + 1) % 4
                    cx += dx[direction]
                    cy += dy[direction]
                else:
                    cx, cy = nx, ny
            except:
                direction = (direction + 1) % 4
                cx += dx[direction]
                cy += dy[direction]
                
        return answer