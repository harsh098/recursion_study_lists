from typing import List
res = []
def p(ds: List[int]):
    if len(ds)>0:
        res.append(ds)
        ds.pop()
        p(ds)

ds = [1,2,3]
p(ds)
print(res)