from typing import List

# Optimised for Time O(N!)
# Uses branch and bound
# T(N) = N*T(N-1) + O(1)


def place(i: int, n: int, board: List[List[int]], l_diag: List[int], r_diag: List[int], cols: List[int]):
    if i==n:
        print_board(board, n)
        return
    
    for j in range(n):
        if (l_diag[i+j]==0 and r_diag[n-1 + (j-i)]==0 and cols[j]==0):
            board[i][j] = 1
            l_diag[i+j] = 1
            r_diag[n-1+ (j-i)] = 1
            cols[j] = 1
            place(i+1, n, board, l_diag, r_diag, cols)
            board[i][j] = 0
            l_diag[i+j] = 0
            r_diag[n-1+ (j-i)] = 0
            cols[j] = 0

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
    l_diag = [0]*(2*n-1)
    r_diag = [0]*(2*n-1)
    cols = [0]*n
    place(0, n, board, l_diag, r_diag, cols)

nqueen(8)



