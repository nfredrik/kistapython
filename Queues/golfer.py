from prio_queue import PriorityQueue

class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score= score

    def __str__(self):
        return "%-16s: %d" % (self.name, self.score)

    def __cmp__(self, other):
        if self.score < other.score: return  1   # less is more
        if self.score > other.score: return -1
        return 0


if __name__ == '__main__':

     tiger = Golfer("Tiger Woods",    61)
     phil  = Golfer("Phil Mickelson", 72)
     hal   = Golfer("Hal Sutton",     69)

     pq = PriorityQueue()
     pq.insert(tiger)
     pq.insert(phil)
     pq.insert(hal)
     while not pq.is_empty(): print pq.remove()
