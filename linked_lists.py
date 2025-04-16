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

    def insert(self, val, index = None):
        # start at head and traverse through list until we reach the end
        current_node = self.head
        current_index = 0
        # keep looping until either we run out of nodes or we hit the node before our index
        while current_node.next and current_index < index:
            current_node = current_node.next
            current_index +=1
        if current_index < index:
            # if we didn't reach our index then it is invalid
            raise IndexError(f'Index {index} is out of bounds. Max index is {current_index}.')
        else:
            next_node = current_node.next
            
            # initialise node
            new_node = Node(val, None)
            current_node.next = new_node

    def get_len(self):
        len = 0
        current_node = self.head
        while current_node.next:
            current_node=current_node.next
            len += 1
        return len
    
    def pop(self, index):



if __name__ == '__main__':
    def divide(a, b):
        return a/b
    tests = [
        {'input':{'a':1, 'b':2}, 'output':0.5},
        {'input':{'a':1, 'b':2}, 'output':0.2},
        {'input':{'a':1, 'b':0}, 'output':0.5}
    ]
    run_tests(divide, tests)
