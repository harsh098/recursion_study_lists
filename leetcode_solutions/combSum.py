from typing import List

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def util(i: int, ds: List[int], t: int):
            nonlocal res, n, candidates
            if i==n:
                if t==0:
                    res.append(ds[:])
                return
            #Pick 
            if candidates[i] <= t:
                ds.append(candidates[i])
                util(i, ds, t-candidates[i])
                ds.pop()
            #Not Pick
            util(i+1, ds, t)
        
        util(i=0, ds=[], t=target)
        return res

sol = Solution()
target = 7
candidates = [2,3,6,7]
ans = sol.combinationSum(candidates=candidates, target=target)
print(ans)