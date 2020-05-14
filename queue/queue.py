"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
### 3. The difference between using an array versus a linked list when implemennting a Queue is that you have to change the index that you want to pop on the array and for the queue, you have to change the head node first before deleting the first element.

# 1. Using Arrays
'''
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        return self.storage.append(value)

    def dequeue(self):
        if(len(self.storage) > 0):
            return self.storage.pop(0)
        return None
'''

class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
    
class Queue:
    def __init__(self):
        self.size = 0
        # first node in the list
        self.head = None

    def __len__(self):
        current = self.head
        counter = 1
        # what if the list is empty? 
        if not current:
            return 0
        # what if the list isn't empty?
        elif current.get_next() is None:
            return counter
        else:
            while current.get_next() is not None:
                counter += 1
                current = current.get_next()
            # we're at the end of the linked list 
            return counter

    def enqueue(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)
        # what if the list is empty? 
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to? 
            # the last node in the list 
            # we can get to the last node in the list by traversing it 
            current = self.head 
            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list 
            current.set_next(new_node)

    def dequeue(self):
       # what if the list is empty?
        if not self.head:
            return None
        elif self.head.get_next() is None:
            value = self.head.value
            self.head = None
            return value
        else:
            cur_node = self.head.value
            self.head = self.head.get_next()
            return cur_node