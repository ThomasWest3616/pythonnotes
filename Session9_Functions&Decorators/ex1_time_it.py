# timer.py

#Next week we will work with generators, generator expressions and list comprehensions. These topics has a lot to do with program efficiency.

# For this we will be measuring our code in diffenrent ways and especialy we will ‘time it’ and ‘messure memmory usage’.

# Task:

# Your job is, to write a decorator function that can time any piece of code.

import time

def timer(func):                                                                                                                                   
    def wrapper(*args, **kwargs):                                                                                                                  
        start = time.time()                                                                                                                        
        func(*args, **kwargs)                                                                                                                      
        end = (time.time()) - start                                                                                                              
        print(f'Time elapsed: {end}')                                                                                                              

    return wrapper                                                                                                                                 


@timer                                                                                                                                             
def genrate_list(num):                                                                                                                             
    [x for x in range(1, num)]