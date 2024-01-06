from typing import List

"""
You are given an array arr and a target sum s. Print any one of subsequences that sum up to s.
the sum for empty subsequence [] is considered 0.

--------------------------------------------------------------
Input:-
arr = [3,2,1,0,1,5]
s = 4
--------------------------------------------------------------
Output:-
[3, 1, 0]
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

def printAllSubsequences(i: int, arr: List[int], s: int, t: int,  l: List[int]) -> bool:
    n = len(arr)
    if i>=n:
        if s==t:
            print(l)
            return True
        return False
    
    s+=arr[i]
    l.append(arr[i])
    if (printAllSubsequences(i+1, arr, s, t, l)==True):
       return True
    l.pop()
    s-=arr[i]
    if(printAllSubsequences(i+1, arr, s, t, l)==True):
        return True
    
    return False

if __name__ == '__main__':
    arr = [3,2,1,0,1,5]
    printAllSubsequences(0, arr, 0, 4, [])