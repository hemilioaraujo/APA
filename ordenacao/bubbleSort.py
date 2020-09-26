def bubbleSort(arr): 
    trocas = 0
    n = len(arr)
	
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1

    return arr, trocas

if __name__ == "__main__":
    arr = [2, 4, 1, 6, 5, 3]
    print(arr)
    vetor, trocas = bubbleSort(arr)
    print(vetor, trocas)
