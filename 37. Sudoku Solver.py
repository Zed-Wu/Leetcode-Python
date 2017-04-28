import sys
sys.setrecursionlimit(1000000)

class Solution(object):
    def checkpos(self,i,j,board):
        if board[i][j] == '.':
            return True
        for l in range(0, len(board)):
            if l == i:
                continue
            if board[l][j] == board[i][j]:
                return False
        for k in range(0, len(board[i])):
            if k == j:
                continue
            if board[i][k] == board[i][j]:
                return False
        row = i / 3
        col = j / 3
        for r in range(row * 3, row * 3 + 3):
            for c in range(col * 3, col * 3 + 3):
                if r == i and c == j:
                    continue
                if board[r][c] == board[i][j]:
                    return False
        return True

    def seeksolution(self,board,flag):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == '.':
                    flag = False
        if flag == True:
            return board,flag

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == '.':
                    for value in range(1,10):
                        tmp = list(board[i])
                        tmp[j] = str(value)
                        board[i] = ''.join(tmp)
                        if self.checkpos(i,j,board):
                            board,flag = self.seeksolution(board,True)
                            if flag == True:
                                return board,flag
                    tmp = list(board[i])
                    tmp[j] = '.'
                    board[i] = ''.join(tmp)
                    return board,flag

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board,flag = self.seeksolution(board,True)
        return board

if __name__ == "__main__":
    solution = Solution()
    re = solution.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
    print re