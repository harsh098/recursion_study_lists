from typing import List

def f(arr: List[int], l: int, r: int):
    if l<r:
        arr[l],arr[r] = arr[r],arr[l]
        f(arr, l+1, r-1)

arr = [1,2,3,4]
f(arr, 0, len(arr)-1)
print(arr)