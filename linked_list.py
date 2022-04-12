from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def set_start(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def append(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            probe = self.head

            while probe.next:
                probe = probe.next

            probe.next = node
        
        self.size += 1

    def insert(self, index, data):
        counter = 0

        if index > self.size:
            print(f'index is out of range.')
        elif index <= 0:
            self.head = Node(data, self.head)
        else:
            probe = self.head

            while counter != index:
                probe = probe.next
                counter += 1
            
            probe.next = Node(data, probe.next)
            self.size += 1

    def replace(self, data, new_data):
        probe = self.head

        while probe != None and probe.data != data:
            probe.next
        
        if probe.data != None:
            probe.data = new_data
        else:
            print(f"The target element {data} is not in the linked list")

    def delete(self, index):
        count = 0

        if index >= self.size - 1:
            print(f"Index is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            probe = self.head

            while probe.next.next != None and count != index:
                count += 1
                probe = probe.next
            removed_item = probe.next.data
            probe.next = probe.next.next

            print(f"{removed_item}")

            self.size -= 1
        
    def pop(self):
        data = self.head.data

        if self.head.next == None:
            self.head = None
        else:
            probe = self.head

            while probe.next.next != None:
                probe = probe.next
            
            data = probe.next.data
            probe.next = None

        self.size -= 1
        print(data)

    def search(self, data):
        probe = self.head

        while probe.data != data and probe != None:
            probe = probe.next
        
        if probe != None:
            print(f'the target element {data} was found.')
            return probe
        else:
            print(f'the element is not in the linked list.')

    def lenght(self):
        return self.size

    def show(self):
        probe = self.head

        while probe != None:
            print(probe.data)
            probe = probe.next

    def clear(self):
        self.head = None
        self.size = 0

    def iter(self):
        current = self.head

        while current:
            value = current.data
            current = current.next
            yield value