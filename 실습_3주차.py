#1
def selectionSort(array, n) :
    for i in range(0, n-1) :
        minIdx = i
        for k in range(i+1, n) :
            if array[minIdx] > array[k] :
                minIdx = k
        tmp = array[i]
        array[i] = array[minIdx]
        array[minIdx] = tmp
    
    return array

def bubbleSort(array, n) :
    for end in range(n-1, 0, -1) :
        for cur in range(0, end) :
            if array[cur] > array[cur+1] :
                array[cur], array[cur+1] = array[cur+1], array[cur]
    
    return array

def insertionSort(array, n) :
    for i in range(1, n) :
        for j in range(i, 0, -1) :
            if array[j-1] > array[j] :
                array[j-1], array[j] = array[j], array[j-1]

    return array 

#2
n, k = map(int, input().split())
numlist = list(map(int, input().split()))
insertionSort(numlist, n)
print(numlist[-k])

#3


#4

#5