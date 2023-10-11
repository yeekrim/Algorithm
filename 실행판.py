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

input_ary = list(input().split())
sorted_ary = []
res = ''

for i in range(len(input_ary)) :
    sorted_ary.append([input_ary[i]*3, input_ary[i]])

sorted_ary = quick_sort(sorted_ary)

for i in range(len(sorted_ary)-1,-1, -1) :
    res += sorted_ary[i][1]

print(res)