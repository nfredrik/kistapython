
def A():
    print 'A'
    
def B():
    print 'B'

def C():
    print 'C'
    
functions = [A, B, C]


def get_functions():
    try:
        return next(get_functions.s)
    except StopIteration:
        get_functions.s = iter(functions)
        return next(get_functions.s)
        
setattr(get_functions, 's', iter(functions))




for i in range(10):
    get_functions()()


    
print 'the end'
