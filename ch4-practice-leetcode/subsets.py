from typing import List

class Solution:
    def subset(self, i: int, ds: List[int], arr: List[int], res: List[int]):
        if i==len(arr):
            res.append(ds[:])
            return
        ds.append(arr[i])
        self.subset(i+1, ds, arr, res)
        ds.remove(arr[i])
        self.subset(i+1, ds, arr, res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.subset(0, [], nums, res)
        return res
        