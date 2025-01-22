
def customSort(arr: int, head):
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            if arr[j]>=head and arr[j-1]<head:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            elif arr[j]>head and arr[j-1]>head and arr[j-1]>arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            elif arr[j]<head and arr[j-1]<head and arr[j-1]<arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
        # print(arr)
            
    return arr
                

def process(arr: list, head: int, size):
    if size-1 not in arr:
        arr.append(size-1)
    
    
    arr = customSort(arr, head)
    
    print(arr)

process(list(map(int, input("List: ").split())), int(input("Head: ")), int(input("Size: ")))
    
    