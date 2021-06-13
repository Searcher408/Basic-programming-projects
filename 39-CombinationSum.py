class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            for digit in range(9):
                if raw[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    board[i][j] = str(digit + 1)
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    dfs(pos + 1)
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return
        
        raw = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _c in range(3)] for _r in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3] = True
        
        dfs(0)