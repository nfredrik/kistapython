from node import Node
from invariants import EnforceCheckRep

class Queue:
    __metaclass__ = EnforceCheckRep # the ONLY line you need to add to the class definition
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next: last = last.next
            # append the new node
            last.next = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        return cargo

    def checkRep(self):
        print "checkrRep"
        cntr = 0
        tmp = self.head
        while tmp:
            tmp = tmp.next
            cntr+=1
        assert cntr == self.length 


if __name__ == '__main__':

    queue1 = Queue()

    queue1.insert(5)
    queue1.insert(3)
    queue1.insert(1)

    for i in range(3):
        print queue1.remove()
