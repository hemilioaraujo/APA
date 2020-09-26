trocas = 0


def partition(arr,low,high): 
    global trocas
    trocas = low
    i = ( low-1 )
    pivot = arr[high]

    for j in range(low , high):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            trocas += 1

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    trocas += 1
    return ( i+1 )


def _quickSort(arr, low, high):
    if low < high: 
        pi = partition(arr,low,high)
        _quickSort(arr, low, pi-1) 
        _quickSort(arr, pi+1, high)
    


def quickSort(arr):
    n = len(arr)
    low = 0
    high = n - 1
    _quickSort(arr, low, high)
    global trocas
    return arr, trocas


if __name__ == "__main__":    
    arr = [10, 80, 30, 90, 40, 50, 70]
    print(arr)
    vetor, trocas = quickSort(arr)
    print(vetor, trocas)    
