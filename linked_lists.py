from utils.testing import run_tests

# let's define a linked list, we'll need the following functionality
# 1) add a node at an index
# 2) traversal
# 3) linear search
# 4) pop(index)
# 5) remove value

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        # initialise an empty dummy head. This will point to our first node when we add it
        self.head = Node(None, None)
        self.size = 0

    def __str__(self):
        return str(self.to_array())
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, idx):
        assert not self.is_empty(), 'List is empty'
        self.validate_index(idx)
        # 0th element
        current_node = self.head.next
        # increment if idx > 0
        for i in range(idx):
            current_node=current_node.next
        return current_node.val

    def get_size(self):
        return self.size

    def is_empty(self):
        """Checks if the array is initialised"""
        # if the head is pointing to None then we're empty
        return self.head.next is None
    
    def validate_index(self, index: int):
        """Checks whether the idx is in bounds"""
        assert (0 <= index) and (index <= self.size), f'Index {index} is out of bounds. Current list size: {self.size}.' 

    def insert(self, val, index = None):
        """Inserts a value into the list. If index is None then put it at the end."""
        # set index to end if empty
        index = index or self.size
        self.validate_index(index)
        
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        next_node = current_node.next
        
        # add node
        current_node.next = Node(val, next_node)
        self.size +=1

    def pop(self, index = None):
        """removes node at specified index from list and returns value. Return none if empty"""
        if self.is_empty():
            return None
        
        index = index or self.size -1
        self.validate_index(index)
        
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        target_node = current_node.next
    
        # remove_node
        current_node.next = target_node.next
        self.size -=1
        # return value
        return target_node.val
    
    def search(self, val):
        """search for a value. Return the idx if it exists, and None if not"""
        if self.is_empty():
            return None
        
        current_node = self.head
        for i in range(self.size):
            current_node=current_node.next
            if current_node.val == val:
                return i            
        return None
    
    def to_array(self):
        array = []
        current_node = self.head
        for i in range(self.size):
            current_node = current_node.next
            array.append(current_node.val)
        return array

if __name__ == '__main__':
    print('Debug')
    linked_list = LinkedList()
    linked_list.insert(0)
    linked_list.insert(1)
    linked_list.insert(2)
    print(linked_list)
    linked_list.insert(6)    
    print('insert 6 at end', linked_list)
    linked_list.pop(1)    
    print('pop first element', linked_list)
    print('print elments', linked_list[0], linked_list[1], linked_list[2])
    print('search for 6:', linked_list.search(6))
    print('search for -1:', linked_list.search(-1))

    # tests
    print('Running Tests')
    linked_list = LinkedList()
    linked_list.insert(0)
    linked_list.insert(1)
    linked_list.insert(2)
    tests = [
        (linked_list.get_size, {}, 3),
        (linked_list.insert, {'val':5}, None),
        (linked_list.get_size, {}, 4),
        (linked_list.pop, {}, 5),
        (linked_list.pop, {'index': 1}, 1),
    ]
    run_tests(tests)
