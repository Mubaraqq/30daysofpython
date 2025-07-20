############################################ FUNCTIONS ################################################

    # function without parameters 
def generate_full_name(): # defining function
    firstname = 'Musa'
    lastname = 'Abba'
    space = ' '
    fullname = firstname + space + lastname
    print(fullname)
generate_full_name() # function call

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

    # function returning a value
def generate_full_name():
    firstname = 'Ishaq'
    lastname = 'Bashir'
    space = ' '
    fullname = firstname + space + lastname
    return fullname
print(generate_full_name())

def add_two_nums():
    num1 = 5
    num2 = 78
    total = num1 + num2
    return total
print(add_two_nums())

    # function with parameters 
def greetings(name):
    message = name + ', welcome here!'
    return message
print(greetings('Mubarak'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(190))

def square_number(x):
    return x * x
print(square_number(3))

def area_of_circle(r):
    pi = 3.142
    area = pi * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print(sum_of_numbers(10))


    # function with 2 paramaters
def generate_full_name(firstname, lastname):
    space = ' '
    fullname = firstname + space + lastname
    return fullname
print(generate_full_name('Mubarak', 'Yakubu'))

def sum_two_nums(num1, num2):
    sum = num1 + num2
    return sum
print(sum_two_nums(99, 1))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2025, 1996))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + 'N' # has to be change to str to add the unit 
    return weight
print('weight of an object in Newtons = ', weight_of_object(100, 9.81))

    # passing an args with key and value
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num1 = 45, num2 = 89))

    # returning a bool
def is_even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False
#print(is_even(10))
print(is_even(7))

    # returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(20))

    # functions with parameters
def greetings(name = 'Moses'):
    message = 'welcome here, ' + name
    return message
print(greetings())
print(greetings('Musa'))

    # arbitrary number of arguments *
def sum_of_nums(*nums):
    total = 0
    for num in nums:
        total = total + num
    return total
print(sum_of_nums(2, 3, 5))

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1', 'luukman', 'samuel', 'bashir', 'idi'))

    # function as a parameter of another function
def square_number(n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))


################################################# EXERCISES #####################################################
