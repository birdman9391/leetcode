class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        isVisited = [[False for _ in range(n)] for __ in range(m)]

        answer = []
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        cx, cy = 0, 0
        direction = 0
        
        for i in range(m * n):
            answer.append(matrix[cy][cx])
            isVisited[cy][cx] = True
            nx, ny = cx + dx[direction], cy + dy[direction]
            if nx not in range(n) or ny not in range(m) or isVisited[ny][nx]:
                direction = (direction + 1) % 4
                nx, ny = cx + dx[direction], cy + dy[direction]
            cx, cy = nx, ny

                
        return answer