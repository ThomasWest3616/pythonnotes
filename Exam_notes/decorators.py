# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

# Decorators are a significant part of Python. In simple words: they are functions which modify the functionality of other functions.

# You'll use a decorator when you need to change the behavior of a function without modifying the function itself
import time
import datetime

def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    
    return wrapper

@f1
def f(a):
    print(a)

# x = f1(f)

f("Hi")


@f1
def add(x, y):
    return x + y

print(add(4,5))


# Eksempel 1

def before_after(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")
    
    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print("run")

t = Test()
t.decorated_method()

# Eksempel 2

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function took:", time.time() - before, "seconds")
    
    return wrapper

@timer
def run():
    time.sleep(2)

run()

# Eksempel 3

def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "/n")
        val = func(*args, **kwargs)
        return val

    return wrapper

@log
def run(a, b, c=9):
    print(a+b+c)

run(1,3,c=9)




