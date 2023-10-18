#1
ary = [1,10,5,8,7,6,4,3,2,9]

def max_heapify(array):
    last = len(array) // 2 - 1
    for current in range(last, -1, -1):
        while current <= last:
            child = current * 2 + 1
            sibling = child + 1
            if sibling < len(array) and array[child] < array[sibling]:
                child = sibling
            if array[current] < array[child]:
                array[current], array[child] = array[child], array[current]
                current = child
            else:
                break

    return array

#2
def heap_sort(array):
    n = len(array)

    for i in range(n):
        while i != 0:
            last = (i-1)//2
            if (array[last] < array[i]):
                array[last], array[i] = array[i], array[last]
            i = last

    for j in range(n-1, -1, -1):
        array[0] , array[j] = array[j], array[0]
        last = 0
        i = 1
        while i<j:
            i = 2*last +1
            if (i<j-1) and (array[i] < array[i+1]):
                i += 1
            if (i<j) and (array[last] < array[i]):
                array[last], array[i] = array[i], array[last]
            last = i
    return array

#3
print('s = ', end='')
s = list(map(int,input().split()))

heap_sort(s)

print("\""f'{s[0]}' ' ' f'{s[-1]}'"\"")

#4
def findrectangle(array) :
    x_list = []
    for j in range(4) :
        x_list.append(array[j][0])
    y_list = []
    for j in range(4) :
        y_list.append(array[j][1])

    if x_list.count(x_list[0]) == x_list.count(x_list[1]) == x_list.count(x_list[2]) == x_list.count(x_list[3]) :
        if y_list.count(y_list[0]) == y_list.count(y_list[1]) == y_list.count(y_list[2]) == y_list.count(y_list[3]) :
            return 1
        else :
            return 0
    else :
        return 0


n = int(input())

dot = []
res = []

for i in range(n) :
    dot.append([])
    for j in range(4) :
        x,y = map(int, input().split())
        dot[i].append([x,y])

for i in range(n) :
    res.append(findrectangle(dot[i]))

for i in range(len(res)) :
    print(res[i])

#5
n = int(input())

numlist1 = [1,2,3,4,5,6]
numlist2 = [10000,20,36,47,40,6,10,7000]
sub_list = []
res = []

sort_numlist = heap_sort(numlist1)

for i in sort_numlist :
    sub_list.append([abs(n-i), i])

sub_sort = heap_sort(sub_list)

for j in range(len(sub_sort)-1) :
    if sub_sort[j][0] == sub_sort[j+1][0] :
        sub_sort[j], sub_sort[j+1] = sub_sort[j+1], sub_sort[j]

for l in sub_sort :
    res.append(l[1])

print(res)

#6
n = int(input())
timelist = []
res = []

for _ in range(n) :
    start, end = map(int,input().split())
    timelist.append([start, end])

for i in range(len(timelist)) :
    for j in range(len(timelist)) :
        if timelist[i][0] > timelist[j][0] and timelist[i][1] > timelist[j][1] :
            continue
        elif timelist[i][0] < timelist[j][0] and timelist[i][1] < timelist[j][1] :
            continue
        elif timelist[i] == timelist[j] :
            continue
        else :
            timelist[j] = [0,0]
            break
    

print(len(timelist))
