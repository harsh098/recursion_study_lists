from typing import List, Set


# Approach 1 Generate All Pairs
# class Solution:
#     def __perm(self, i: int, ds: List[int], src: List[int], chosen: Set[int], res: List[int]):
#         if i==len(src):
#             res.append(ds[:])
#             return
        
#         for j in range(len(src)):
#             if j in chosen:
#                 continue
#             chosen.add(j)
#             ds.append(src[j])
#             self.__perm(i+1, ds, src, chosen, res)
#             ds.pop()
#             chosen.remove(j)
    
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res =[]
#         chosen = set()
#         self.__perm(0, [], nums, chosen, res)
#         return res

# Approach 2 (Optimisation 1:- Remove HashSet) Generate All Pairs
# class Solution:
#     def __perm(self, i: int, ds: List[int], src: List[int], chosen: List[bool], res: List[int]):
#         if i==len(src):
#             res.append(ds[:])
#             return
        
#         for j in range(len(src)):
#             if chosen[j]:
#                 continue
#             chosen[j]=True
#             ds.append(src[j])
#             self.__perm(i+1, ds, src, chosen, res)
#             ds.pop()
#             chosen[j]=False
    
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res =[]
#         chosen = [False]*len(nums)
#         self.__perm(0, [], nums, chosen, res)
#         return res

# Approach 3 (Optimal: Optimised Space) Use juggling and placement
class Solution:
    def __perm(self, i: int,  src: List[int], res: List[int]):
        if i==len(src):
            res.append(src[:])
            return
        
        for j in range(i, len(src)):
            src[i], src[j] = src[j], src[i]
            self.__perm(i+1, src, res)
            src[i], src[j] = src[j], src[i]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        self.__perm(0, nums, res)
        return res