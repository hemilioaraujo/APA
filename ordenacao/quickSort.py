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

def quickSort(arr, low, high):
    if low < high: 
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
    global trocas
    return trocas


if __name__ == "__main__":    
    arr = [10, 80, 30, 90, 40, 50, 70] # 5 trocas
    # arr = [4,7,2,6,4,1,8,3] # 6 trocas
    n = len(arr) 
    print(arr)
    trocas = quickSort(arr,0,n-1)
    print(arr)
    print(f'Número de trocas: {trocas}')
    
