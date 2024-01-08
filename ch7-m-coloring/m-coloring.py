"""
Codestudio Link to the problem:-
https://www.codingninjas.com/studio/problems/m-coloring-problem_981273?leftPanelTabValue=SUBMISSION
"""

from typing import *

def is_safe(i: int, g: List[List[int]], c: int, visited: List[int]) -> bool:
    V=len(g)
    for j in range(V):
        if g[i][j] and visited[j]==c:
            return False
    return True

def solve(i: int, g: List[List[int]], c: int, m: int, visited: List[int]) -> bool:
    if i==len(g):
        return True
    
    if is_safe(i, g, c, visited):
        visited[i]=c
        for color in range(m):
            if(solve(i+1, g, color, m, visited)):
                return True
        visited[i]=-1
    return False


def graphColoring(mat: List[List[int]], m: int) -> str:
    # Write your code here
    return 'YES' if solve(0, mat, 0, m, [-1]*len(mat)) else 'NO'