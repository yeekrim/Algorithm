def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot, tail = array[0], array[1:]
    
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    
    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

