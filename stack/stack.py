"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

### 3. The difference between using an array and a linked list when implementing a Stack is that arrays can be manipulated by dropping or adding an element to the list while to change linked lists you have to change the value that the node points to.

"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         return self.storage.append(value)
    
#     def pop(self):
#         if(len(self.storage) > 0):
#             return self.storage.pop()
#         return None

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
    
class Stack:
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

    def push(self, value):
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

    def pop(self):
        # what if the list is empty?
        if not self.head:
            return None
        elif self.head.get_next() is None:
            value = self.head.value
            self.head = None
            return value
        # what if it isn't empty?
        else:
            current = self.head
            prev = None
            while current.get_next() is not None:
                prev = current
                current = current.get_next()
            # we're at the end of the linked list
            prev.set_next(None)
            del_current = current.value
            current = None
            return del_current
