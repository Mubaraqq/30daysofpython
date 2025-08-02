# exception handling
try:
    f = open('file.txt')
except FileNotFoundError:
    print('file not found!')
finally:
    print('end of try-except block')


try:
    name = input('enter your name: ')
    year_born = input('enter the year you were born: ')
    age = 2025 - year_born # type error, should be int(year_born)
    print(f'you are {name}. and your age is {age}')

except TypeError:
    print('type error occured')
except ValueError:
    print('value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('i usually run with the try block')
finally:
    print('i always run')

try:
    name = input('enter your name: ')
    year_born = input('enter the year you were born: ')
    age = 2025 - int(year_born)
    print(f'you are {name}. and your age is {age}')
except Exception as err:
    print(err)

# unpacking list
def sum_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_five_nums(lst)) # TypeError

def sum_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_five_nums(*lst)) # * is an unpacking operator for lists and tuples

# unpacking in the range built-in function
numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args) # unpacked args list into individual numbers
print(list(numbers))

# a list or tuple can also be unpacked like this:
countries = ['Nigeria', 'Dubai', 'Korea', 'Palestine', 'China', 'India']
nig, dub, kor, *rest = countries
print(nig, dub, kor, rest)

numbers = (1, 2, 3, 4, 5, 6, 7)
one, *middle, slast, last = numbers
print(one, middle, slast, last)

# unpacking dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}. he is {age} years old'
dct ={
    'name': 'Hassan',
    'country': 'Ethopia',
    'city': 'Addis Abba',
    'age': '29',
}
print(unpacking_person_info(**dct))


# packing - allows a function to take arbitrary number of arguments
def sum_all(*args):
    s = 0
    for i in args:
        s = s + i
    return s 
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7,))

# packing dictionaries 
def packing_person_info(**kwargs):
    #check the type of kwargs and it is a dict type?
    #print(type(kwargs))
    #printing dictionary items
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    #return kwargs
print(packing_person_info(name = 'salis', country = 'somalia', city = 'soma', age = '29'))

# spreading in python
nums = [1, 2, 3]
print(*nums)

numbers = [1, 2, 3]
new_numbers = [0, *numbers, 4, 5]
print(new_numbers)

dict1 = {
    'a': 1,
    'b': 2,
}
dict2 = {
    **dict1, # **dict1 spreads its key-value pairs into the new dictionary
    'c': 3,
}
print(dict2)

def add(a, b, c):
    return a + b + c
values = [10, 20, 30]
print(add(*values))

person = {
    'name': 'Aliyu',
    'age': 27
}
def greet(name, age):
    print(f'hello {name}, you are {age} years old')
greet(**person)

# combine list or dict
a = [1, 2]
b = [3, 4]
combined = [*a, *b]
print(combined)

x = {
    'a': 1
    }
y = {
    'b': 2
    }
merged = {**x, **y}
print(merged)

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)

country_lst1 = ['Egypt', 'Canada', 'Qatar']
country_lst2 = ['Iceland', 'Sweden', 'Norway']
nordic_countries = [*country_lst2]
print(nordic_countries)

# enumerate() built-in function used when you want to loop over an iterable and keep track of the index of the current item.
fruits = ['apple', 'banana', 'watermelon', 'orange']
for index, fruit in enumerate(fruits):
    print(index, fruit)

for i, fruit in enumerate(fruits, start = 1):
    print(f'{i}. {fruit}')

# when to use enumerate()
fruits = ['apple', 'banana', 'watermelon', 'orange']

for i in range(len(fruits)):
    print(i, fruits[i])

for i, fruit in enumerate(fruits):
    print(i, fruit) # cleaner and easeir to read

# we can get the index of each item in a list
for index, item in enumerate([20, 30, 40]):
    print(index, item)

countries = ['Nigeria', 'South Africa', 'Kenya', 'Uganda', 'Ghana']
for index, country in enumerate(countries):
    if country != 'Uganda':
        print(f'hi {country}')
    else:
        print(f'the country {country} has been found at index {index}')


# zip() built-in function - pairs items together from each iterable
names = ['Ali', 'Zarah', 'Musa']
scores = [95, 90, 99]
zipped = zip(names, scores)
print(list(zipped))

# if the iterable are not same length, it stops at the shortest one
x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c', 'd']
print(tuple(zip(x, y)))

# to unzip, we can use the unpacking operator *
zipped = [('Ali', 95), ('Zarah', 90)]
names, scores = zip(*zipped)
print(names)
print(scores)

# when to use zip()? 
    # creating dictionaries from keys and values
keys = ['name', 'age']
values = ['Sam', '12']
print(dict(zip(keys, values)))

fruits = ['apple', 'banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
fruits_and_vegetables = []
for f, v in zip(fruits, vegetables):
    fruits_and_vegetables.append(f'fruits: {f}, veg: {v}')
print(list(fruits_and_vegetables))
#print(list(zip(fruits, vegetables)))
