class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for list in board:
            hs = set()
            for num in list:
                if num != '.' and num in hs:
                    return False
                elif num != '.':
                    hs.add(num)

        for i in range(9):
            hs = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in hs:
                    return False
                elif board[j][i] != '.':
                    hs.add(board[j][i])
        hs1 = set()
        hs2 = set()
        hs3 = set()
        for i in range(9):
            
            if i > 0 and i%3 == 0:
                hs1 = set()
                hs2 = set()
                hs3 = set()
            for j in range(3):
                if board[i][j] != '.' and board[i][j] in hs1:
                    return False
                elif board[i][j] != '.':
                    hs1.add(board[i][j])
            
            for j in range(3,6):
                if board[i][j] != '.' and board[i][j] in hs2:
                    return False
                elif board[i][j] != '.':
                    hs2.add(board[i][j])
                    print(hs2)
            for j in range(6,9):
                if board[i][j] != '.' and board[i][j] in hs3:
                    return False
                elif board[i][j] != '.':
                    hs3.add(board[i][j])
            
        return True

            
