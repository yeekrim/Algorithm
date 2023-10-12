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


#5

#6

