from typing import List
def pivot(arr: List[int], l, r) -> int:
    pivot = arr[l]
    i,j = l,r
    while i<j:
        while arr[i]<=pivot and i<=r-1:
            i+=1
        while arr[i]>pivot and j>l:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[j], arr[l] = arr[l], arr[j]
    return j

    

    # TODO: Median pivot strategy
    # TODO: Random pivot startegy


def quickSort(arr, l, r):
    if(l<r):
        p = pivot(arr, l, r)
        quickSort(arr, l, p-1)
        quickSort(arr, p+1,r)


arr = [9,0,-3,1,2]
quickSort(arr, 0, len(arr)-1)
print(arr)