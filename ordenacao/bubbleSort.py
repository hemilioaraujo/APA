from os import name


def bubbleSort(arr): 
	n = len(arr) 

	for i in range(n-1): 
		for j in range(0, n-i-1): 
			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(arr)
    bubbleSort(arr)
    print(arr)
