class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False 

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                
        return True
































        # sudoku=False
        # for row in board:
        #     for i in row:
        #         if i=='.':
        #             continue
        #         elif i in [row[0:i],row[i:]]:
        #             sudoku=True
        #         else:
        #             sudoku=True

        # for col in board:
        #     for i in col:
        #         if i=='.':
        #             continue
        #         elif i in [col[0]]
            