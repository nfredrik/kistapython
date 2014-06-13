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

    def checkRep(self):
        assert True 


