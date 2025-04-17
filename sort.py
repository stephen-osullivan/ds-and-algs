# sort.py

def quick_sort(array):
    """take an array and quicksort it"""

    if len(array) == 0:
        return list()
    
    mid_idx = len(array)//2
    mid_val = array[mid_idx]
    
    same = [x for x in array if x == mid_val]
    left = [x for x in array if x < mid_val]
    right = [x for x in array if x > mid_val]
    
    return quick_sort(left) + same + quick_sort(right)

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid_idx = len(array)//2
    left = array[:mid_idx]
    right = array[mid_idx:]

    left = merge_sort(left)
    right = merge_sort(right)
    out = list()
    i, j, k = 0, 0, 0
    while left and right:
        if left[0] < right[0]:
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))
    return out + left + right


if __name__ == "__main__":
    l1 = []
    l2 = [3,3,3,3]
    l3 = [1,4,5,-1,10]
    l4 = [1,1,2,-9,1.5,100]
    
    print('quick sort')
    print(quick_sort(l1))
    print(quick_sort(l2))
    print(quick_sort(l3))
    print(quick_sort(l4))

    print('merge sort')
    print(merge_sort(l1))
    print(merge_sort(l2))
    print(merge_sort(l3))
    print(merge_sort(l4))
    