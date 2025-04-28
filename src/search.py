#search.py

def binary_search(self, target, nums) -> int:
    """performs binary search on a sorted array"""
    # time complexity O(log(n))
    # space complexity O(1)
    def recursive_binary_search(left = 0, right = len(nums)-1):
        mid = (left + right)//2
        if left > right:
            return -1
        elif nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(mid+1, right)
        else:
            return binary_search(left, mid-1)
    return binary_search()
    
if __name__ == "__main__":
    print(binary_search(10, []))
    print(binary_search(10, list(range(15))))
    print(binary_search(10, list(range(5))))
