from node import Node
import gc

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        """Add an element in top of a stack"""
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def length(self):
        return self.size

    def iter(self):
        """create loops with an stack"""
        probe = self.top

        while probe:
            value = probe.data
            probe = probe.next
            yield value

    def find(self, data):
        """search an element on stack"""
        probe = self.top

        while probe:
            if probe.data == data:
                return True
            else:
                probe = probe.next
        
        return False

    def pop(self):
        """Remove top element in a stack"""
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            
            return data

        else:
            return "There no value on the stack"
            
    def peek(self):
        """Show top element in a stack"""
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    def clear(self):
        """Remove all elemnts in a stack"""
        self.size = 0
        self.top = None
        gc.collect()

