class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check = set()
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                elif cell not in check:
                    check.add(cell)
                else:
                    return False
            check = set()
            for j in range(9):
                cell = board[j][i]
                if cell == ".":
                    continue
                elif cell not in check:
                    check.add(cell)
                else:
                    return False
            check = set()
            for j in range(9):
                cell = board[(i//3)*3 + j // 3][(i%3)*3 + j % 3]
                if cell == ".":
                    continue
                elif cell not in check:
                    check.add(cell)
                else:
                    return False
        return True