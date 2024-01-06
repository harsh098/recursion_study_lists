from typing import List

### Brute Force Approach
# class Solution:
#     def valid(self, ds: str) -> bool:
#         stk = []
#         for i in ds:
#             if stk and stk[-1]=="(" and i==")":
#                 stk.pop()
#             else:
#                 stk.append(i) 
#         if stk:
#             return False
#         return True

#     def generator(self, ds: str, n: int, res: List[int]):
#         if len(ds)==2*n:
#             if self.valid(ds):
#                 res.append(ds)
#             return
#         self.generator(ds+"(", n, res)
#         self.generator(ds+")", n, res)
        
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#         self.generator("(", n, res)
#         return res

class Solution:
    def generator(self, left: int, right: int, ds: str, n: int, res: List[int]):
        if len(ds)==2*n:
            res.append(ds)
            return
        if left < n:
            self.generator(left+1, right,ds+"(", n, res)
        if right < left:
            self.generator(left, right+1, ds+")", n, res)
    
     
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generator(0, 0, "", n, res)
        return res
        