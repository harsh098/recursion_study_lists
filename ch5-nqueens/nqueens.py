from typing import List

#  Vanilla Implementation  O(N! * N)
# T(N) = N*T(N-1) + O(N)


def safe(i: int,j: int, board: List[List[int]], n) -> bool :
    for row in range(0, i):
        if board[row][j]==1:
            return False
    #ldiag
    row, col=i-1, j-1
    while row>=0 and col>=0:
        if board[row][col]==1:
            return False
        row-=1
        col-=1
    #rdiag
    row, col=i-1, j+1
    while col<n and row>=0:
        if board[row][col]==1:
            return False
        row-=1
        col+=1
    return True

def place(i: int, n: int, board: List[List[int]]):
    if i==n:
        print_board(board, n)
        return

    for j in range(n):
        if safe(i,j, board, n):
            board[i][j] = 1
            place(i+1, n, board)
            board[i][j] = 0


def print_board(board: List[List[int]], n):
    print("___"*n)
    for i in range(n):
        print("|", end="")
        for j in range(n):
            print("* |" if board[i][j] else "  |", end="")
        print("\n","---"*n)

    print()

def nqueen(n: int):
    board = list(([0]*n).copy() for _ in range(n))
    place(0, n, board)

nqueen(8)