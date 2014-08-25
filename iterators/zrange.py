class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def next(self):
        print self.i, self.n
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            print 'end'
            raise StopIteration()


z = zrange(3)

print list(z)

