######################### Tuple #####################
"""
empty_tuple = ()
empty_tuple = tuple() # using the tuple constructor
tple = ('item1', 'item2', 'item3')
fruits = ('apple', 'banana', 'orange', 'mango')
print(len(fruits))

    # accessing tuple items - similar to the list 
    
fruits = ('apple', 'banana', 'mango', 'orange', 'lemon')
first_fruit = fruits[0]
second_fruits = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)


fruits = ('apple', 'banana', 'mango', 'orange', 'lemon')
first_fruit = fruits[-5]
print(first_fruit)
last_fruit = fruits[-1]
print(last_fruit)


    # slicing tuple 
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:]
#all_fruits = fruits[0:4]
orange_mango = fruits[1:3]
orange_rest = fruits[1:]
print(orange_rest)

fruits = ('apple', 'banana', 'orange', 'mango', 'watermelon')
all_fruits = fruits[-5:]
orange_mango = fruits[-3:-1]
orange_totherest = fruits[-3:]
print(orange_totherest)


    # changing tuple to list - tuple is immutable, need to change to list to be modified
fruits = ('banana', 'mango', 'orange', 'watermelon')
fruits = list(fruits)
fruits.insert(0, 'apple')
print(fruits)
#fruits = tuple(fruits)
#print(fruits)


    # checking an item in a tuple
tpl = ('item1', 'item2', 'item3', 'item4')
print('item2' in tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)
fruits[0] = 'apple' #tuple is immutable


    # joining tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
print(tpl3)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'cabbage', 'onion')
fruits_vegetables = fruits + vegetables
print(fruits_vegetables)


    # deleting tuples - it is not possible to remove a single item in a tuple but it is possible
    #                   to delete the tuple itself using del
tpl = ('item1', 'item2', 'item3')
del tpl
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
print(fruits)


####################################  EXERCISES  ##########################################

empty_tuple = tuple()
print(empty_tuple)

brothers = ('Misbahu', 'Abdurrazak', 'Mubarak', 'Halifa')
sisters = ('Mamy', 'Baby', 'Hauwwa')
siblings = brothers + sisters
#print(len(siblings))
siblings = list(siblings)
siblings.insert(0, 'Yakubu')
siblings.insert(1, 'Binta')
family_members = siblings
family_members = tuple(family_members)
#print(family_members)

# unpacking parents and sibling from family members
father, mother, *siblings = family_members
print('Father:', father)
print('Mother:', mother)
print('Siblings:', siblings)

fruits = ('apple', 'banana', 'mango', 'orange', 'watermelon')
vegetables = ('salad', 'potato', 'tomato', 'onion')
animal_product = ('beaf', 'meat', 'steak', 'milk')
food_stuff_tuple = fruits + vegetables + animal_product
print(food_stuff_tuple)
food_stuff_list = list(food_stuff_tuple)
print(food_stuff_list)
print(len(food_stuff_list))
print(food_stuff_list[6])
print(food_stuff_list[0:3])
print(food_stuff_list[-3:])
print(food_stuff_tuple)
del food_stuff_tuple
#print(food_stuff_tuple)
"""
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
