def shellSort(arr):
	trocas = 0
	n = len(arr) 
	gap = n//2

	while gap > 0: 
		for i in range(gap,n): 
			temp = arr[i] 
			j = i

			while j >= gap and arr[j-gap] >temp: 
				arr[j] = arr[j-gap] 
				trocas += 1
				j -= gap 
			arr[j] = temp

		gap = round(gap/2)
	
	return arr, trocas

if __name__ == "__main__":
	arr = [12, 34, 54, 2, 3]
	print(arr)
	vetor, trocas = shellSort(arr)
	print(vetor, trocas)
