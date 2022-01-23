# Decorators
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are a significant part of Python. In simple words: they are functions which modify the functionality of other functions.
# You'll use a decorator when you need to change the behavior of a function without modifying the function itself

def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    
    return wrapper

@f1
def f(a, b, c, d):
    print(a, b, c, d)

# x = f1(f)

f("Hi", 2, 3, 4)