trocas = 0

def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2
	global trocas

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i]
		trocas += 1
		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)
	global trocas 

	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		trocas += 1
		heapify(arr, i, 0)
	return arr, trocas

if __name__ == "__main__":
	arr = [ 12, 11, 13, 5, 6, 7]
	print(arr)
	vetor, trocas = heapSort(arr)
	print(vetor, trocas)
