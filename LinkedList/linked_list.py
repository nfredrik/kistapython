from invariants import EnforceCheckRep

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next != None:
            tail = self.next
            tail.print_backward()
        print self.cargo,



class LinkedList:
    __metaclass__ = EnforceCheckRep # the ONLY line you need to add to the class definition
    def __init__(self):
        self.length = 0
        self.head   = None

    def print_backward(self):
        print "[",
        if self.head != None:
            self.head.print_backward()
        print "]",

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

    def removeSecond(self):
        if self.head == None: return
        first = self.head
        second = self.head.next
        # make the first node refer to the third
        first.next = second.next
         # separate the second node from the rest of the list
        second.next = None
        self.length-=1
        return second

    def checkRep(self):
        #print 'checkRep()'
        cntr=0
        self.tmp = self.head
        while self.tmp != None:
            cntr+=1
            self.tmp = self.tmp.next

        assert self.length == cntr, "%d %d" % (self.length, cntr)





if __name__ == '__main__':

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next= node2
    node2.next= node3

    node1.print_backward()


    list = LinkedList()

    list.addFirst(1)
    list.addFirst(3)
    list.addFirst(5)

    list.print_backward()

    list.removeSecond()
    list.print_backward()