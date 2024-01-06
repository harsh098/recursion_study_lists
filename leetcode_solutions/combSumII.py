from typing import List

class Solution:
    def combinations(self,i: int, arr: List[int], ds: List[int], ans: List[int], target: int) -> None:
        if target==0:
            ans.append(ds[:])
            return
        
        for j in range(i, len(arr)):
            if j>i and arr[j-1]==arr[j]:
                continue
            if arr[j]>target:
                break
            ds.append(arr[j])
            self.combinations(j+1, arr, ds, ans, target-arr[j])
            ds.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.combinations(0, candidates, [], res, target)
        return res