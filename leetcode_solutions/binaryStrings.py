from typing import List

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