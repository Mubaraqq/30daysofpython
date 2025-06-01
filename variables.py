#Day 2: 30 Days of python programming

""""
first_name = 'Salma'
last_name = 'Abdullahi'
full_name = 'Salma Abdullahi'
country = 'Nigeria'
city = 'Kano'
age = 22
year = 2016
is_married = False
is_true = True
is_light_on = True

phone_no, email, EVM_address = +2347065777783, 'mubbyr@gmail.com', '0x2fe...ab2a'
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(phone_no))
print(type(email))
print(type(EVM_address))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
reminder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(reminder)
print(exp)
print(floor_division) 

pi = 3.142
r = 30

area_of_circle = (3.142 * (30**2))
print(area_of_circle) 

import math

r = 30

area_of_circle = math.pi * r**2

print("The area of circle = ", area_of_circle)

import math
r = 30
circum_of_circle = 2 * math.pi * r

print("The Circumference of circle = ", circum_of_circle)

import math
r = int(input('Enter radius of the circle = '))
area_of_circle = math.pi * r**2
print('The area of circle = ', area_of_circle)

from datetime import datetime  #get the current year using the datetime module

first_name = str(input('Enter your firsr name '))
last_name = str(input('Enter your last name '))
country = str(input('Country '))
age = int(input('age '))

year = datetime.now().year
year_1 = year - age

print('My name is',first_name, last_name)
print('I am from', country, 'born in', year_1) 

print('== Addition, Substraction, Multiplication, Division, Modulus ==')

num_one = 3
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
reminder = num_two % num_one

print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('reminder: ', reminder)

#calculating area of circle

radius = 10
area_of_circle = 3.14 * radius**2

print('Area of circle: ', area_of_circle)

#calculating area of rectangle 

length = 10
width = 20
area_of_rectangle = length * width

print('Area of rectangle: ', area_of_rectangle) 

#calculating a weight of an object 

mass = 75
gravity = 9.81
weight = mass * gravity 

print(weight,'N') #N is unit 

#calculating the density of a liquid 

mass = 75 #in kg
volume = 0.075 #in cubic meter
density = mass / volume

print('Density: ', density, 'kg/m**3') 

base = float(input('Enter base: '))
height = float(input('Enter height: '))

area = 0.5 * base * height

print('Area of the triangle: ', area) 

print('Enter the sides of the triangle')

side_a = float(input('side a = '))
side_b = float(input('side b = '))
side_c = float(input('side c = '))

peri = side_a + side_b + side_c

print('The perimeter of the triangle is ', peri) 

print(("Enter the length and width of the Rectangle"))

len = float(input('length = '))
wid = float(input('width = '))

area = len * wid
peri = 2 * (len + wid)

print('Area = ', area)
print('Perimeter = ', peri)

print('Enter the raduis of a circle:')

rad = float(input('radius = '))
pi = 3.14

area = pi * (rad**2)
circ = 2 * pi * rad 

print('Area = ', area)
print('Circumference = ', circ)

#calcute the slope, x-intercept and y-intercept form y = 2x - 2
#general eq is y = mx + b, where m is the slope and b is the y-intercept
#define the linear equation coefficient

m = 2 #slope
b = -2 #y-intercept

#calculate y-intercept where x = 0
y_intercept = b

#calculate x-intercept where y = 0
x_intercept = -b/m

print("Slope (m):", m)
print("Y-intercept (b):", b)
print("X-intercept: ", x_intercept )

import math
#slope is m = y2 - y1 / x2 - x1 
#points are (2,2) and (6,10)
#To find the slope

m = (10 - 2) / (6 - 2)
print("The slope = ", m)

#To find the Euclidean distance AKA pythagorean distance 

point1 = [2,2]
point2 = [6,10]
diff_x = point1[0] - point2[0]
diff_y = point1[1] - point2[1]

diff_x_squared = diff_x ** 2
diff_y_squared = diff_y ** 2

sum_of_squared = diff_x_squared + diff_y_squared
distance = math.sqrt(sum_of_squared)

print('The Euclidean distance btw the points = ', distance)

x = int(input('enter the value of x: '))

y = x**2 + 6*x + 9

print('value of y when x is', x, '=', y)

print('length of python is',len('python'))
print('length of dragon is',len('dragon'))

#falsy comparison statement 

print(len('python') != len('dragon'))


print(('on' in 'python') and ('on' in 'dragon'))

print('jargon' in 'i hope this course is not full of jargon')

print('on' not in ('dragon') and ('python'))


length = len('python')
print(length)

float_length = float(length)
print(float_length)

str_length = str(length)
print(str_length)

num = int(input('Number check, please enter a number:'))

if num % 2 == 0:
    print('Number is even, pass!!')

else:
    print('Number is not even, fail!!')


floor_d = 7 // 3
print(floor_d)

converte_d = 2.7
print(int(converte_d))

print(type('10'))
print(type(10))


print(int(9.8))


hrs = float(input('Enter hours: '))
rate = float(input('Enter the rate: '))
weekly_earning = hrs * rate

print('Your weekly earning is: ', weekly_earning)


num_of_years = int(input('Enter the number of years (max = 100): '))
sec_in_year = 60 * 60 * 24 * 365 
total_sec = sec_in_year * num_of_years
if (num_of_years <= 100):
    print('There is ',total_sec, 'in', num_of_years, 'years')
else:
    print('Invalid!')


#Using f-string 

name = "Mubarak Yakubu"
age = 28

#print('Hello,', 'my name is', name, 'and i am', age, 'years old')

greetings = f"Hello, my name is {name} and i am {age} years old"
print(greetings)


def greet(name):
    return f"Hello, {name}!"

message = f"Greeting: {greet('Hafsat')}"
print(message)


a = 5
b = 3
result = f"The sum of {a} and {b} is {a + b}"
print(result)

pi = 3.14159
formated_pi = f"pi rounded to two decimals: {pi:.2f}"
print(formated_pi)

person = {"name":'Sarah', "age": 30}
description = f"{person["name"]} is {person["age"]} years old!"
print(description)

x = 10
y = 20
comparison = f"{x} is less than {y}: {x < y}"
print(comparison)

name = 'Bashir'
age = 17
greeting = "Hello, my name is {} and i am {} years old". format(name, age)
print(greeting)

name = "Musa"
age = 25
greetings = "Hello, my name is %s and i am %d years old" %(name, age)
print(greetings)

print('n  n0  n1  n2  n3')

for n in range(1, 6): #loop the values from 1 to 5
    print(f"{n}  {n**0}   {n**1}   {n**2}   {n**3}")

