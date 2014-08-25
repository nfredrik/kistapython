class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

class reverse_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def next(self):
        #print '...', self.n
        if self.i < len(self.n):
            i = self.i
            self.i += 1
            return self.n[-1 -i]
        else:
            print 'the end'
            raise StopIteration()


y = reverse_iter([1,2,3,4])
print y.next()
print y.next()
print y.next()
print y.next()
print y.next()
