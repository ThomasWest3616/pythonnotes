import random
import time

# In this exercise you start out by having a list of names, and a list of majors.

# Your job is to create:

# A list of dictionaries of students (ie: students = [{‘id’: 1,’name’: ‘Claus’, ‘major’: ‘Math’}]), cretated in a normal function that returns the resul.

# A Generator that “returns” a generator object. So the student is yield instead of returned.

# Both functions should do the same, but one returns a list and one a generator object.

# students = [{‘id’: 1,’name’: ‘Clasu’, ‘major’: ‘Math’}]
# The id could be generated by a counter or like in a loop.
# The Name should be found by randomly chosing a name from the names list
# The Major should be found by randomly chosing a major from the major list

def timer(func):
    def wrapper(*args):
        start = time.time()
        val = func(*args)
        end = (time.time()) - start
        print(f'Time elepsed: {end}')
        return val
    return wrapper

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

@timer
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    # return result

@timer
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person