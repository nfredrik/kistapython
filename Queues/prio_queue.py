class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)


    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]: maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        return item

    def checkRep(self):
    	pass
    	

    q = PriorityQueue()
    q.insert(11)
    q.insert(12)
    q.insert(14)
    q.insert(13)
    while not q.is_empty(): print q.remove()