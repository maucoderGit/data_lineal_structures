from node import Node

class CircleLinkedList:
    def __init__(self, data = None):
        self.head = Node(data)
        self.head.next = self.head
        
        if self.head == None:
            self.size = 0
        else:
            self.size = 1
    
    def append_elements(self, data):
        """
        Set a data list to traverse them
        """
        probe = self.head

        while probe.next != None and probe.next != self.head:
            probe = probe.next
        
        for i in data:
            probe.next = Node(i)
            probe = probe.next
            self.size += 1

        probe.next = self.head

    def iter(self):
        """
        Iter in nodes.
        """
        start = self.head
        current = start.next

        yield start.data

        while current != start:
            value = current.data
            current = current.next
            yield value

    def print_data(self):
        nodes = []
        for node in self.iter():
            nodes.append(str(node))
            print(" -> ".join(nodes))
        