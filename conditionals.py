################################################ CONDITIONALS ######################################################
"""
a = 20
if a > 0:
    print('A is a +ve number')

a = 0
if a > 0:
    print('A is a +ve number')
elif a < 0:
    print('A is a -ve number')
else:
    print('A is zero')

# short hand - code(statement) if condition else code(statement) 
a = 3
print('A is +ve') if a > 0 else print('A is probably -ve') 

    # nested if condition
a = int(input('Enter an integer: '))
if a > 0:
    if a % 2 == 0:
        print('a is +ve and even integer')
    else:
        print('a is a +ve number')
elif a == 0:
    print('a is zero')
else:
    print('a is -ve number')

     # we can avoid writing nested condition by using the logical op. *and*
a = 5
if a > 0 and a % 2 == 0:
    print('A is an even and +ve integer')
elif a > 0 and a % 2 != 0:
    print('A is an odd and +ve integer')
elif a == 0:
    print('A is zero')
else:
    print('A is a negetive integer')

    # if and *or* logical operators
user = str(input('Enter username:'))
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted.')
else:
    print('Access denied!!')

######################################### EXERCISES ################################################
#Problem 1
age = int(input('Enter your age: '))
if age >= 18:
    print('you are old enough to drive')
else:
    print(f'you need {-(age - 18)} more years')
"""

your_age = 25
my_age = int(input('Enter my age: '))
if my_age < your_age:
    if your_age - my_age > 1:
        print(f'you are {your_age - my_age} years older than me')
    else:
        print(f'you are {your_age - my_age} year older than me')
elif my_age > your_age:
    if my_age - your_age > 1:
        print(f'i am {my_age - your_age} years older than you')
    else:
        print(f'i am {my_age - your_age} year older than you')
else:
    print('we share the same age')
