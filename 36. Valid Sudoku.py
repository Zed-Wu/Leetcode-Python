class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == '.':
                    continue
                for l in range(0,len(board)):
                    if l == i:
                        continue
                    if board[l][j] == board[i][j]:
                        return False
                for k in range(0,len(board[i])):
                    if k == j:
                        continue
                    if board[i][k] == board[i][j]:
                        return False
                row = i / 3
                col = j / 3
                for r in range(row * 3,row * 3 + 3):
                    for c in range(col * 3,col * 3 + 3):
                        if r == i and c == j:
                            continue
                        if board[r][c] == board[i][j]:
                            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    re = solution.isValidSudoku()
    print re