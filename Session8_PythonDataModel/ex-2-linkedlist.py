class Node:
     def __init__(self, data):
             self.data = data
             self.next = None


class LinkedList:
        def __init__(self):
             self.head = None

llist = LinkedList()
llist.head = Node('Data of first Node')        # head is a pointer to a Node with data off 'Data of First Node'
llist.head.next = Node('Data of second Node') # next belongs to 'Data of First Node' Node and points to 'Data of second Node' Node.

help(list)