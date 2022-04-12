from msilib.schema import Error
from double_linked_list import TwoWayNode
from node import Node

class TwoWayLinkedList:
    def __init__(self, data, previous: Node = None, next: Node = None):
        self.head = TwoWayNode(data, previous, next)
        self.tail = self.head
        self.size = 1

    def append(self, data):
        probe = self.head

        if self.tail == self.head:
            probe.next = TwoWayNode(data, self.head)
            self.tail = probe.next
        else:
            probe = self.tail
            probe.next = TwoWayNode(data, probe)

            self.tail = probe.next
        
        self.size += 1

    def insert(self, data, index):
        counter = 0
        probe = self.head

        if index > self.size - 1:
            raise Error("Index is out of range")
        elif index == 0:
            self.head = TwoWayNode(data, None, probe)
        else:
            # First iter on TwoWayLinkedList
            while index != counter:
                probe = probe.next
                counter += 1
            
            # Entonces desplazamos el valor anterior. Sin asignar el valor previo
            probe.next = TwoWayNode(probe.data , None, probe.next)
            # Creamos el nuevo nodo en la posición que dejamos vacia.
            probe = TwoWayNode(data, probe.previous, probe.next)

            # Ahora asignamos el valor previo con el nodo creado
            probe.next.previous = probe
        
        self.size += 1
        