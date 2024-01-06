from typing import List

"""
You are given an array arr and a target sum k. Print the number of subsequences that sum up to s.
the sum for empty subsequence [] is considered 0.

--------------------------------------------------------------
Input:-
arr = [3,2,1,0,1,5]
k = 4
--------------------------------------------------------------
Output:-
6
---------------------------------------------------------------
Explanation:-

Possible Subsequences are:
[3, 1, 0]
[3, 1]
[3, 0, 1]
[3, 1]
[2, 1, 0, 1]
[2, 1, 1]
---------------------------------------------------------------


"""

def printCountOfTargetSubsets(i: int, arr: List[int], t: int, s: int)-> int:
    n = len(arr)
    if i>=n:
        if t==s:
            return 1
        return 0
    
    # We have 2 choices so we go for take(l) and not_take(r).
    # The more choices per element we take as many variables
    
    s+=arr[i]
    l = printCountOfTargetSubsets(i+1, arr, t, s)
    s-=arr[i]
    r = printCountOfTargetSubsets(i+1, arr, t, s)

    return l+r

if __name__ == '__main__':
    arr = [3,2,1,0,1,5]
    k = 4
    print(printCountOfTargetSubsets(0, arr, k, 0))