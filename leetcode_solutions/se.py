"""
Brute Force Solution to 
https://leetcode.com/problems/distinct-subsequences/description/
"""

result = 0

def numDistinct(s: str, t: str) -> int:
    n = len(s)
    def numDistinctUtil(i: int, x: str):
        global result
        if i>=n:
            result+= (1 if t==x else 0)
            return
        x+=s[i]
        numDistinctUtil(i+1, x)
        x = x[:len(x)-1]
        numDistinctUtil(i+1, x)
    numDistinctUtil(0,"")
    return result

print(numDistinct("babgbag", "bag"))