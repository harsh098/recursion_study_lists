from typing import List

class Solution:
    def __init__(self):
        self.DIGITS = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"],}
    
    def genCombinations(self, digits: str, ds: str, res: List[str]):
        if not digits:
            if ds:
                res.append(ds)
            return
        for i in self.DIGITS[digits[0]]:
            self.genCombinations(digits[1:], ds+i, res)

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        self.genCombinations(digits, "", res)
        return res