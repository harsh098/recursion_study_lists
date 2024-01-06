from typing import List

def merge(arr: List[int], l, m, r):
    L = arr[l:m+1]
    R = arr[m+1:r+1]
    n1,n2 = len(L), len(R)
    i,j,k = 0,0,l

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1

def mergeSort(arr, l, r):
    if(l<r):
        m = l + (r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

arr = [9,0,-3,1,2]
mergeSort(arr, 0, len(arr)-1)
print(arr)