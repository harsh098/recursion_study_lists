from typing import List

"""
Codestudio Link
https://www.codingninjas.com/studio/problems/-binary-strings-with-no-consecutive-1s._893001?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
"""

def generate(ds: str, N: int, res: List[str]) -> List[str]:
    if len(ds)==N:
        res.append(ds)
        return
    if (not ds) or ds[-1]=="0":
        generate(ds+"0", N, res)
        generate(ds+"1", N, res)
    else:
        generate(ds+"0", N, res)

def generateString(N: int) -> List[str]:
    # write your code here
    res = []
    generate("", N, res)
    return res