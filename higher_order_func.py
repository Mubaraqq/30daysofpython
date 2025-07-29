"""
    # function as a parameter
def greet(name):
    return f'Hello, {name}!'
def shout(text):
    return text.upper()
def process(func, value):
    return func(value)
print(process(greet, 'Musa'))
print(process(shout, 'letsgoo!!'))


def sum_numbers(nums): # normal function
    return sum(nums) # sum() built-in function
def higher_order_func(f, lst):
    #summation = f(lst)
    #return summation
    return f(lst)
result = higher_order_func(sum_numbers, [1, 2, 3, 4, 5])
print(result)

    # function as a return value
def square(x):
    return x**2
def cube(x):
    return x**3
def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
def higher_order_function(func_type):
    if func_type == 'square':
        return square
    elif func_type == 'cube':
        return cube
    elif func_type == 'absolute':
        return absolute
print(higher_order_function('square')(3))
print(higher_order_function('cube')(3))
print(higher_order_function('absolute')(-3))

    # python closure
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(10))
print(add_ten()(5))

def outer(msg):
    def inner():
        print(f'Message: {msg}')
    return inner
# creating a closure
#my_func = outer('Hello, world!')
#my_func()
outer('Hello, World!')()

    # decorators 
# to create a decorator function, we need and outer function with an inner wrapper function
# normal function
def greeting():
    return 'welcome to python'
def uppercase_decorators(x):
    def wrapper():
        #func = x()
        #make_uppercase = func.upper()
        #return make_uppercase
        x()
        make_uppercase = x().upper()
        return make_uppercase
    return wrapper
print(uppercase_decorators(greeting)())

# implemmenting the above with a decorator
def uppercase_decorator(function):
    def wrapper():
        make_uppercase = function().upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'welcome to python'
print(greeting())

# applying mutiple decorators to a single function
# first decorator
def uppercase_dec(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
# second decorator
def split_string_dec(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_dec  # order with decorators is important in this case
@uppercase_dec
def greeting():
    return 'welcome to python'
print(greeting())

# accepting parameters in decorators function
def decorators_with_parameters(function):
    def wrapper_accepting_parameters(p1, p2, p3):
        function(p1, p2, p3)
        print(f'i live in {p3}')
    return wrapper_accepting_parameters
@decorators_with_parameters
def print_full_name(fname, lname, country):
    print(f'i am {fname} {lname}. i love to learn')
print_full_name('Musa', 'Adam', 'Egypt')


# buit-in higher oder functions - map(), filter(), reduce() - works best with lambda functions
# map() - takes a function and iterable as paramters - map(function, iterable)
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x**2
#numbers_squared = map(square, numbers)
#print(list(numbers_squared))


# lets apply it with a lambda function
numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))

names = ['Asa', 'Idi', 'Ema', 'Abu']
def change_to_upper(name):
    return name.upper()
#names_upper = map(change_to_upper, names)
#print(list(names_upper))

# using lambda func
names_upper = map(lambda names: names.upper(), names)
print(list(names_upper))

# filter() - filters the items that satisfy the filtering criteria  
# returns boolean for each items of the iterable - filter(func, iterable)
numbers = [1, 2, 3, 4, 5]
def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

def is_odd(num):
    if num % 2 != 0:
        return True
    return False
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

# filter long name
names = ['Mubarak', 'Abida', 'Abraham', 'Lidiya', 'Ermias']
def is_name_long(name):
    if len(name) > 6:
        return True
    return False
long_names = filter(is_name_long, names)
print(list(long_names))
"""
# reduce() - defined in the function module - take a function and an iterable and returns a single value
from functools import reduce
number_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, number_str)
print(total)
