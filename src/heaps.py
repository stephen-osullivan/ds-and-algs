# heaps.py
import heapq # for testing
class MinHeap:
    def __init__(self, data=None):
        self.data = data or [] # stored as dynamic array
        self.size = len(self.data)
        self._heapify()
    
    def __str__(self):
        return str(self.data)
    
    def _heapify(self):
        # heapify the data in place: Time O(n) Space O(1)
        # start from the last non-leaf node and heapify down
        # last leaf: self.size -1, last parent: (self.size - 2) // 2
        for i in range(self.size // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def _heapify_down(self, idx):
        # heapify down the node at index idx
        left, right = idx*2 + 1, idx*2 + 2

        # access the data
        parent_val = self.data[idx]
        left_val = self.data[left] if left < self.size else None
        right_val = self.data[right] if right < self.size else None

        # base case: no children
        if not left_val:
            return

        # compare with left and right children
        largest=idx    
        if left_val and left_val < self.data[largest]:
            largest = left
        if right_val and right_val < self.data[largest]:
            largest = right

        # swap if necessary
        self.data[idx], self.data[largest] = self.data[largest], self.data[idx]
        
        if largest != idx:
            self._heapify_down(largest)

    def insert(self, val):
        self.data.append(val)
        self.size += 1
        self._heapify_up(self.size - 1)
    
    def _heapify_up(self, idx):
        parent = (idx-1) // 2
        
        if self.data[idx] >= self.data[parent]:
            return
        else:
            self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
            self._heapify_up(parent)

    def pop(self):
        # remove the root of the heap
        if self.size == 0:
            return None
        elif self.size == 1:
            return self.data.pop()
        else:
            root = self.data[0]
            self.data[0] = self.data.pop()
            self.size -= 1
            self._heapify_down(0)
            return root



if __name__ == "__main__":
    # Test the heap class
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 8, 9, -10, 13]
    h = MinHeap(data)
    print("Heapified data:".ljust(30), h.data) # should be a valid heap
    data_copy = h.data.copy()
    heapq.heapify(data_copy)
    print("Check with heapq:".ljust(30), data_copy) # should be a valid heap
    print('Inserting 4')
    h.insert(2)
    print("Heapified data:".ljust(30), h.data) # should be a valid heap
    heapq.heappush(data_copy, 2)
    print("Check with heapq:".ljust(30), data_copy) # should be a valid heap
    print('Popping')
    while h.data:
        print(h.pop(), end=' ')
    print()

