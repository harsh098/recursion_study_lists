from typing import List

# class Solution:
#     # Solve using Vanilla Recursion
#     def __isSafe(self, i: int, j: int, board: List[str],n: int ) -> bool:
#         row, col = i-1, j-1
#         while row>=0 and col>=0:
#             if board[row][col]=='Q':
#                 return False
#             row-=1
#             col-=1
        
#         row, col = i-1, j+1
#         while row>=0 and col<n:
#             if board[row][col]=='Q':
#                 return False
#             row-=1
#             col+=1
        
#         for row in range(0, i):
#             if board[row][j]=='Q':
#                 return False
        
#         return True

#     def __solve(self, i: int, board: List[str], n: int, res: List[List[str]]) -> None:
#         if i==n:
#             res.append(board[:])
#             return
#         for j in range(n):
#             if self.__isSafe(i, j, board, n):
#                 board[i] = board[i][:j] + 'Q' + board[i][j+1:]
#                 self.__solve(i+1, board, n, res)
#                 board[i] = board[i][:j] + '.' + board[i][j+1:]
    
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         board = ["."*n]*n
#         res = []
#         self.__solve(0, board, n, res)
#         return res

class Solution:
    # Solve using Branch and Bound
    def __solve(self, i: int, board: List[str], n: int, res: List[List[str]], l_diag: List[int], r_diag: List[int], cols: List[int]) -> None:
        if i==n:
            res.append(board[:])
            return
        for j in range(n):
            if l_diag[i+j]==0 and r_diag[n-1 + (j-i)]==0 and cols[j]==0 :
                board[i] = board[i][:j] + 'Q' + board[i][j+1:]
                l_diag[i+j]=1
                r_diag[n-1+(j-i)]=1
                cols[j]=1
                self.__solve(i+1, board, n, res, l_diag, r_diag, cols)
                board[i] = board[i][:j] + '.' + board[i][j+1:]
                l_diag[i+j]=0
                r_diag[n-1+(j-i)]=0
                cols[j]=0
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["."*n]*n
        l_diag = [0]*(2*n-1)
        r_diag = [0]*(2*n-1)
        cols = [0]*n
        res = []
        self.__solve(0, board, n, res, l_diag, r_diag, cols)
        return res
        