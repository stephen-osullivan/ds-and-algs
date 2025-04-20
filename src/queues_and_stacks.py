# queues and stacks

class Node:
    def __init__(self, val, next= None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        # we need a head and a tail to allow O(1) enqueue and dequeue
        self.head = Node(None, None)
        self.tail = self.head

    def enqueue(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.tail == self.head:
            return None
        else:
            first_node = self.head.next
            val = first_node.val
            if first_node is self.tail:
                self.head.next = None
                self.tail = self.head
            else:
                self.head.next = first_node.next
        return val
    
class Stack:
    def __init__(self):
        self.head = None
    
    def add(self, val):
        self.head = Node(val, self.head)

    def pop(self):
        if self.head is None:
            return None
        else:
            val = self.head.val
            self.head = self.head.next
            return val

if __name__ == "__main__":
    print('Queue:')
    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(3)
    queue.enqueue(-10)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print('Stack:')
    stack = Stack()
    stack.add(0)
    stack.add(3)
    stack.add(-10)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    
    