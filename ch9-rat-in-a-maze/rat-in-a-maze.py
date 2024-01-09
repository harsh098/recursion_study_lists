from typing import List, Tuple, Dict, Set

"""
Codestudio Link:-
https://www.codingninjas.com/studio/problems/rat-in-a-maze-_8842357?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

"""

def get_moves(matrix: List[List[int]], i: int, j: int) -> Dict[str, Tuple[int]]:
    d ={
        "U": (i-1, j) if i-1>=0 else None, 
        "D": (i+1, j) if i+1<len(matrix) else None, 
        "L": (i, j-1) if j-1>=0 else None, 
        "R": (i, j+1) if j+1<len(matrix) else None
    }

    for k,v in d.items():
        if v is not None:
            d[k] = v if matrix[v[0]][v[1]]==1 else None
    return d

def solve(node: Tuple[int], p: str, g: List[List[int]], res: List[str], visited: Set[Tuple[int]]):
    n= len(g)
    if node == (n-1, n-1):
        res.append(p)
        return
    for k,v in get_moves(g, *node).items():
        if v is not None and v not in visited:
            visited.add(v)
            solve(v, p+k, g, res, visited)
            visited.remove(v)


def ratMaze(matrix: List[List[int]]) -> List[str]:
    # Write your code here.
    res=[]
    visited = {(0,0)}
    solve((0,0), "", matrix, res, visited)
    return res