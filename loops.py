############################################## LOOPS ###################################################

count = 0
while count < 5:
    print(count)
    count = count + 1

count = 5
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

count = 0
while count < 10:
    print(count)
    count = count + 1
    if count == 7:
        break # we use *break* when we want to get out or stop the loop

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue # we use *continue* when we want to skip the current iteration and continue with the next
    print(count)
    count = count + 1


    # for loop with list 
numbers = [0, 1, 2, 3, 4, 5]
for a in numbers:  # *a* is called iterator, a temporary name to refer to the list's items, valid only inside the loop
    print(a)

    # for loop with string
language = 'python'
#for letter in language: # here *letter* is the iterator
    #print(letter)

for letter in range(len(language)):
    print(language[letter])

    # for loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

    # for loop with dict
student_dict = {
    'firstname':'Aliyu',
    'lastname':'Sadi',
    'gender':'male',
    'age':'27',
    'is_married': False,
    'skills':['Trade', 'Communication', 'Reading', 'Writing'],
    'country':'Nigeria',
    'city':'kano',
    'address': {
        'street':'Musa Gammo Street',
        'bus stop':'gidan qanqara, sabon titin Mandawari'
    },
}
for key in student_dict:
    print(key)
for key, value in student_dict.items(): # items() - changes dict to list
    print(key, value)

    # for loops in set()
it_companies = {'X', 'APPLE', 'META', 'AMAZON', 'GOOGLE', 'ORACLE'}
for company in it_companies:
    print(company)

numbers = {0, 1, 2, 3, 4, 5}
for num in numbers:
    if num == 4:
        break
    print(num)

numbers = {0, 1, 2, 3, 4, 5}
for num in numbers:
    if num == 3:
        print('skipping 3 here')
        continue
    print(num)
print('loops end')


    # the range() function
lst = list(range(11)) # 1 to 10
print(lst)

st = set(range(1, 11))
print(st)

st = set(range(0, 11, 2))
print(st)

for num in range(6):
    print(num)

    # nested for loop
student_dict = {
    'firstname':'Aliyu',
    'lastname':'Sadi',
    'gender':'male',
    'age':'27',
    'is_married': False,
    'skills':['Trade', 'Communication', 'Reading', 'Writing'],
    'country':'Nigeria',
    'city':'kano',
    'address': {
        'street':'Musa Gammo Street',
        'bus stop':'gidan qanqara, sabon titin Mandawari'
    },
}
for key in student_dict:
    if key == 'skills':
        for skill in student_dict['skills']:
            print(skill)

    # for else
for num in range(11):
    print(num)
else:
    print('the loop stops at ', num)

    # pass - we write *pass* when a statement is required to avoid errors or as a placeholder
for num in range(1, 9):
    pass

################################################ EXERCISES ##############################################

