from two_way_linked_list import TwoWayLinkedList

def run():
    nodes = TwoWayLinkedList(1)
    nodes.append(2)
    nodes.append(3)
    nodes.append(4)
    nodes.insert(2, 1)
    probe = nodes.head

    while probe != None:
        print(probe.data)
        probe = probe.next

if __name__ == "__main__":
    run()