from typing import List

class Solution:

    def __valid(self, s) -> bool:
        return s==s[::-1]
    
    def __solve(self, s: str,i: int, ds: int, res: List[List[str]]):
        if i==len(s):
            res.append(ds[:])
            return

        for j in range(i, len(s)):
            if self.__valid(s[i:j+1]):
                ds.append(s[i:j+1])
                self.__solve(s, j+1, ds, res)
                ds.pop()

    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.__solve(s, 0, [], res)
        return res