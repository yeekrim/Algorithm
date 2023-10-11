#1
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot, tail = array[0], array[1:]
    
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    
    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2
    left_arr = merge_sort(array[:mid])
    right_arr = merge_sort(array[mid:])
    merged_arr = []
    l=r=0
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            merged_arr.append(left_arr[l])
            l += 1
        else:
            merged_arr.append(right_arr[r])
            r += 1
    merged_arr += left_arr[l:]
    merged_arr += right_arr[r:]
    return merged_arr

#2
array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
res = []

def oneres(array, cmd) :
    i = cmd[0]; j = cmd[1]; k = cmd[2]
    resary = array[i-1:j]
    sortedary = quick_sort(resary)
    return sortedary[k-1]

for i in range(len(commands)) :
    cmd = commands[i]
    res.append(oneres(array, cmd))

print(res)

#3
input_ary = list(input().split())
sorted_ary = []
res = ''

for i in range(len(input_ary)) :
    sorted_ary.append([input_ary[i]*3, input_ary[i]])

sorted_ary = quick_sort(sorted_ary)

for i in range(len(sorted_ary)-1,-1, -1) :
    res += sorted_ary[i][1]

print(res)

#4
n = int(input())
x_ary = list(map(int, input().split()))
sort_ary = quick_sort(x_ary)
res_ary = []

for i in range(len(x_ary)) :
    ary = []
    for j in range(len(sort_ary)) :
        if x_ary[i] > sort_ary[j] and sort_ary[j] not in ary :
            ary.append(sort_ary[j])
        elif x_ary[i] == sort_ary[j] :
            break
    res_ary.append(len(ary))

print(res_ary)

#5
ary = list(map(int, input().split()))
sort_ary = quick_sort(ary)
res = 0

for i in range(len(sort_ary)) :
    high = 0
    low = 0
    for j in range(len(sort_ary)) :
        if sort_ary[i] < ary[j] :
            high += 1
        elif sort_ary[i] > ary[j] :
            low += 1
        else :
            high += 1
            low += 1
    
    if high == low and sort_ary[i] > res :
        res = low

print(res)

#6
n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

arr.sort(key=lambda x: len(x))
res = len(arr)

for i in range(len(arr)):
    isPrefix = False

    for j in range(i+1, len(arr)):
        if arr[i] == arr[j][:len(arr[i])]:
            isPrefix = True
            break
    
    if isPrefix:
        res -= 1

print(res)

#7
n = int(input())
arr = []
res = []
for i in range(n) :
    arr.append(list(map(int, input().split())))

for i in range(0,len(arr),2) :
    x = (sorted(arr[i][:2] + arr[i+1][:2]))
    res.append(x[-2])
    y = (sorted(arr[i][2:] + arr[i+1][2:]))
    res.append(y[-2])

res = sorted(res)
print(res[-2])