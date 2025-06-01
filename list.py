"""
#using built-in function
lst = list()
empty_list = list()
print(len(empty_list))

#using square bracket []
lst = []
empty_list = []
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_tech = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MangoDB']
countries = ['Nigeria', 'Yemen', 'Rwanda', 'Medina', 'Dubai']
print('Fruits:', fruits)
print('Number of Fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of Vegetables:', len(vegetables))
print('Animal Products:', animal_products)
print('Number of Animal products:', len(animal_products))

#list can have items of different data type
lst = ['Musa', 250, True, {'Counter: France', 'City: Paris'}]
print(lst)

#accessing list items using +ve indexing
fruits = ['banana', 'orange', 'watermelon', 'lemon', 'mango']
print(fruits[0])
print(len(fruits) - 1)
print(fruits[4])

#accessing list items using -ve indexing
fruits = ['apple', 'banana', 'mango', 'watermelon', 'orange']
first_fruit = fruits[-5]
print(first_fruit)
print(fruits[-1]) #last fruit
second_last = fruits[-2]
print(second_last)

#unpacking list items
lst = ['item0', 'item1', 'item2', 'item3', 'item4', 'item5']
first_itm, secong_itm, third_itm, *rest, last = lst
print(first_itm)
print(secong_itm)
print(third_itm)
print(last)
print(rest)


#slicing items from a list
fruits = ['apple', 'banana', 'mango', 'orange', 'lemon', 'lime']
# +ve indexing 
all_fruits = fruits[:6]
all_fruits0 = fruits[0:6]
all_fruits1 = fruits[0:]
mango_orange = fruits[2:4]
orange_mango_lemon = fruits[2:5]
banana_lemon = fruits[1:5:3]
print(all_fruits)
print(all_fruits0)
print(all_fruits1)
print(mango_orange)
print(orange_mango_lemon)
print(banana_lemon)

# -ve indexing
all_fruits = fruits[-6:]
orange_mango = fruits[-4:-2]
mango_orange_lemon = fruits[-4:-1]
reverse_fruits =fruits[::-1]
print(all_fruits)
print(orange_mango)
print(mango_orange_lemon)
print(reverse_fruits)

#modifying list
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'watermelon']
fruits[0] = 'avocado'
fruits[1] = 'apple'
print(fruits)

#checking items in a list
fruits = ['banana', 'apple', 'orange', 'mango', 'lemon']
does_exist = 'lime' in fruits
print(does_exist)

#adding items to a list
fruits = ['banan', 'mango', 'orange', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('watermelon')
print(fruits)

#inserting items into a list
fruits = ['apple', 'orange', 'mango', 'lemon', 'watermelon' ]
fruits.insert(1, 'banana')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

#removing item from a list
fruits = ['banana', 'orange', 'watermelon', 'mango', 'lime', 'banana']
print(fruits)
fruits.remove('banana')
print(fruits)
fruits.remove('lime')
print(fruits)

#removing items using pop()
fruits = ['banana', 'orange', 'mango', 'watermelon', 'lime']
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

#removing items using del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
#print(fruits)
#del fruits[0]
#print(fruits)
#del fruits[1]
#print(fruits)
#del fruits[1:3]
#print(fruits)
del fruits
print(fruits)

#clearing list items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

#copying a list
fruits = ['banana', 'apple', 'ornage', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits)
print(fruits_copy)

#joining list (concatenate) using +
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ['banana', 'ornage', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

#joining using extend() method
num1= [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers: ', num1)

negetive_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negetive_numbers.extend(zero)
negetive_numbers.extend(positive_numbers)
print('Numbers: ', negetive_numbers)

#counting items in a list
#fruits = ['banana', 'orange', 'mango', 'lemon']
#print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

#finding index of an item
#fruits = ['apple', 'banana', 'orange', 'mango', 'lemon']
#print(fruits.index('orange'))
age = [22, 24, 24, 28, 29, 24, 19, 26]
print(age.index(24))

#reversing a list 
#fruits = ['apple', 'banana', 'orange', 'mango', 'lemon']
#fruits.reverse()
#print(fruits)

ages = [22, 19, 24, 29, 28, 21, 24, 27, 26]
ages.reverse()
print(ages)

#sort() - modifies the original list
fruits = ['banana', 'watermelon', 'apple', 'orange', 'mango', 'lemon']
fruits.sort() # ascending order
print(fruits)
fruits.sort(reverse=True)
print(fruits)

ages = [22, 19, 25, 29, 24, 26, 28, 23]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

#sorted() - doesn't modify the original list
fruits = ['watermelon', 'banana', 'apple', 'orange', 'mango', 'lemon']
fruit = sorted(fruits)
print(fruit)
print(fruits)
print(sorted(fruits, reverse=True))


#####################   Exercises   ###################  

list = []
print(list)
print(len(list))

list = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7']
print(len(list))
print(list[0], list[3], list[6])
"""

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[6])
it_companies[5] = 'X'
print(it_companies)
it_companies.append('OpenAI')
print(it_companies)
it_companies.insert(4, 'DeepMind')
print(it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)

