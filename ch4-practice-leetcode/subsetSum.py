from os import *
from sys import *
from collections import *
from math import *

from typing import List

"""

Codestudio Link:-
______________________________________________________________________
https://takeuforward.org/data-structure/subset-sum-sum-of-all-subsets/

"""

def subset(i: int, s: int, res: List[int], arr: List[int]):
    n = len(arr)
    if i>=n:
        res.append(s)
        return
    
    s+=arr[i]
    subset(i+1,s, res, arr)
    s-=arr[i]
    subset(i+1,s, res, arr)

def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    s=0
    res = []
    subset(0, s, res, num)
    res.sort()
    return res