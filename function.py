import time

l = [3,4,2]
l.sort()
print(l)

l = [{'a':1, 'b':5}, {'a':3, 'b':4}, {'a':2, 'b':3}]
l.sort(key=lambda i: i['b'])
print(l)

l2=sorted(l, key=lambda i: i['b'])
print(l2)



def call_func(f, *args):
    return f(*args)
x = call_func(lambda x, y: x + y, 4, 5)
print(x)

import operator
x = call_func(operator.le, 4, 5)
print(x)



def outer():
    def inner(a):
        return a
    return inner
f = outer()
x = f(10)
print(x)


def outer2(a):
    def inner(b):
        return a + b
    return inner
f = outer2(10)
x = f(3)
print(x)

l = [1,2,5,6]
get=operator.itemgetter(1)
x = get(l)
print(x)


zepp = [('Guitar', 'Jimmy'), ('Vocals', 'Robert'), ('Bass', 'John Paul'), ('Drums', 'John')]
s=sorted(zepp)
print(s)
s=sorted(zepp, key=operator.itemgetter(1))
print(s)



def add_power(p):
    def iterate(series):
        x = 0
        for i in series:
            x += i**p
        return x
    return iterate

series1 = (0, 1, 2, 3, 4, 5)
series2 = (2, 4, 8, 16, 32)
power_2 = add_power(2)
print(power_2(series1))
print(power_2(series2))
power_3 = add_power(3)
print(power_3(series1))
print(power_3(series2))



# decorators
def sum(a, b):    
    return a + b

def logit(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called with args = {args} ")
        start_time = time.perf_counter()  # Get starting time
        result = func(*args, **kwargs)
        end_time = time.perf_counter()  # Get ending time
        execution_time_ms = (end_time - start_time) * 1000  # Calculate time in milliseconds
        print(f"Function {func.__name__} returned {result} - exec time: {round(execution_time_ms,3)} ms")
        return result
    return wrapper

sum = logit(sum)
sum(1,2)

@logit
def sum2(a, b):    
    return a + b

sum2(3,4)