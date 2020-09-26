def selectionSort(A):
    trocas = 0
    for i in range(len(A)): 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]
        if(i > trocas):
            trocas += 1
    return A, trocas


if __name__ == "__main__":
    arr = [7, 5, 1, 8, 3]
    print(arr)
    vetor, trocas = selectionSort(arr)
    print(vetor, trocas)
