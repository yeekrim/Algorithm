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
n = int(input())
dot_list = []

for i in range(n) :
    x, y = map(int,input().split())
    dot_list.append([y,x])

selectionSort(dot_list, n)
for i in range(n) :
    print(dot_list[i][1], dot_list[i][0])

#4
n = int(input())
nlist = list(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

res = []

selectionSort(nlist, n)

for i in range(m) :
    cnt = 0
    for j in range(n) :
        if mlist[i] == nlist[j] :
            cnt += 1
        else :
            continue
    res.append(cnt)

print(res)

#5
n = int(input())
length = []

for i in range(n) :
    string = str(input())
    if [len(string),string] in length :
        pass
    else :
        length.append([len(string), string])

selectionSort(length, len(length))

for i in range(len(length)) :
    print(length[i][1])