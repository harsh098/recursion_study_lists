"""
Print all subequences for a given array/string

n=3
[3,1,2]

[]
[3]
[1]
[2]
[3,1]
[3,2]
[1,2]
[3,1,2]

"""

from typing import List

lst=[1,2,3,4,5]

def f(i: int, arr: List[int], n: int):
    global lst
    if i>=n:
        print(arr)
        return
    arr.append(lst[i])
    f(i+1, arr, n)
    del arr[len(arr)-1]
    f(i+1, arr, n)

f(0, [], len(lst))


