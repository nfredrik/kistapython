import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(
           func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}ms".format(
            func.__name__, time.time() - now))
        return return_value
    return wrapper


@log_calls
def test1(a,b,c):
    print("\ttest1 called")

@log_calls
def test2(a,b):
    print("\ttest2 called")

@log_calls
def test3(a,b):
    print("\ttest3 called")
    time.sleep(1)


test1(1,2,3)
test2(4,b=5)
test3(6,7)
