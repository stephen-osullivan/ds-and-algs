#search.py

def binary_search(val, array, verbose=False):
    """performs binary search on a sorted array"""
    # time complexity O(log(n))
    # space complexity O(1)

    if verbose:
        print('Searching', array)

    if len(array) == 0:
        return False
    
    mid_idx = len(array)//2 # for length 2n or 2n+1 this gives position 
    mid_val = array[mid_idx]
    if mid_val == val:
        return True
    elif mid_val < val:
        return binary_search(val, array[(mid_idx+1):])
    else:
        return binary_search(val, array[:mid_idx])

if __name__ == "__main__":
    print(binary_search(10, []))
    print(binary_search(10, list(range(15))))
    print(binary_search(10, list(range(5))))
