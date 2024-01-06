from typing import List

class Solution:
    def combinations(self, i: int, ds: List[int], t: int, k: int, res: List[List[int]]):
        if t==0:
            if len(ds)==k:
                res.append(ds[:])
            return
        
        for j in range(i, t+1 if t<=9 else 10):
            # Pick
            ds.append(j)
            self.combinations(j+1, ds, t-j, k, res)
            #Not Pick
            ds.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        combinations = self.combinations(1, [], n, k, res)
        return res

        