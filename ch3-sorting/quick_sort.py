from typing import List
def pivot(arr: List[int], l, r) -> int:
    # Pivot at the end strategy
    # pivot = arr[r]
    # i = l-1
    # for j in range(l, r+1):
    #     if arr[j]<pivot:
    #         i+=1
    #         arr[j],arr[i] = arr[i],arr[j]
    
    # arr[i+1], arr[r] = arr[r], arr[i+1]
    # return i+1

    #Pivot at the start strategy
    pivot = arr[l]
    j = r+1
    for i in range(r, l-1, -1):
        if arr[i] > pivot:
            j-=1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j-1], arr[l] = arr[l], arr[j-1]
    return j-1

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