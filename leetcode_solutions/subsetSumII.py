from typing import List, Set, Tuple

# Approach 1: Using Hashmap
# class Solution:
#     def subsetWith(self, i: int, ds: List[int], arr: List[int], res: Set[Tuple[int]]):
#         if i>=len(arr):
#             res.add(tuple(ds[:]))
#             return
        
#         ds.append(arr[i])
#         self.subsetWith(i+1, ds, arr, res)
#         ds.pop()
#         self.subsetWith(i+1, ds, arr, res)

#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         nums.sort()
#         self.subsetWith(0, [], nums, res)
#         result = [list(x) for x in res]
#         return result

# Approach 2: (Optimised) w/o using Hashmap

class Solution:
    def subsetWith(self, i: int, ds: List[int], arr: List[int], res: List[int]):
        res.append(ds[:])   
        for j in range(i, len(arr)):
            if j>i and arr[j]==arr[j-1]:
                continue
            ds.append(arr[j])
            self.subsetWith(j+1, ds, arr, res)
            ds.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.subsetWith(0, [], nums, res)
        return res