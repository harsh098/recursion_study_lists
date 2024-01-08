from typing import List

class Solution:
    def __is_safe(self, i: int, j: int, value: int, board: List[List[str]]) -> bool:
        for k in range(9):
            #Check Row
            if board[i][k]==str(value):
                return False 
            #Check Col
            if board[k][j]==str(value):
                return False
            #Check block
            if board[3*(i//3) + k//3][3*(j//3) + k%3]==str(value):
                return False
        
        return True

    def __solve(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    for v in range(1,10):
                        if self.__is_safe(i,j,v,board):
                            board[i][j]=str(v)
                            if(self.__solve(board)):
                                return True
                            board[i][j]="."
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.__solve(board)
        