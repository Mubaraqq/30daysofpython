################################ SET ###############################

st = set() # built-in functions
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
#print(len(fruits))
#print('mango' in fruits)

    # add() method adds one method to a set
fruits.add('apple') 
print(fruits)

    # update() allows to add multiples items, it takes a list argument
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item6', 'item7'])
print(st) # unordered and un-indexed

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage'}
fruits.update(vegetables)
print(fruits)


    # removing items from a set
st = {'item1', 'item2', 'item3', 'item4'}
#st.remove('item5') # item is not found so it raises error
#st.remove('item1')
#st.discard('item5') # discard() method doesn't raise any error even if item isn't found
st.pop()            # pop() removes random item from a set and it takes no argument
removed_item = st.pop() # if we're interested in the removed item
print(removed_item)
print(st)

    # clearing items in a set
fruits = {'banana', 'apple', 'mango', 'orange'}
#fruits.clear()
#print(fruits)
del fruits  # deleting a set 
print(fruits)

    # converting list to set 
lst = ['item1', 'item2', 'item3', 'item4', 'item5', 'item4', 'item1']
st = set(lst)
print(st)  # order is random $ remove duplicates

    # joining a set
st1 = {'item1', 'item2', 'item3', 'item4', 'item5'}
st2 = {'item6', 'item7', 'item8', 'item9'}
#st3 = st1.union(st2)  # union() returns a new set
#print(st3)

st1.update(st2)  # update() insert a set into a given set
print(st1)
print(st2)

    # finding intersection item
st1 = {'item1', 'item2', 'item3', 'item4', 'item5'}
st2 = {'item3', 'item2'}
st3 = st1.intersection(st2)  # intersetion() returns a new set
print(st3)

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
the_inters = python.intersection(dragon)
print(the_inters)

    # checking subset() and superset() of a set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1))
print(st1.issubset(st2))
print(st1.issuperset(st1))
print(st2.issuperset(st1))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.issubset(dragon))
print(dragon.issubset(python))
print(python.issuperset(dragon))
print(dragon.issuperset(python))

    # checking the difference() between 2 sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1))
print(st1.difference(st2))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.difference(dragon))
print(dragon.difference(python))

    # finding symmetric difference between 2 sets - returns a set that contains all items from both sets
    # execept items that are present in both sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st1.symmetric_difference(st2))
print(st2.symmetric_difference(st1))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.symmetric_difference(dragon))
print(dragon.symmetric_difference(python))

    # isdisjoint() - if two sets do not have a common item(s) we call them disjoint sets
    # we can check if two set are joint or disjoint using isdisjoint method
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1))
print(st1.isdisjoint(st2))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.isdisjoint(dragon))
print(dragon.isdisjoint(python))

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))
print(odd_numbers.isdisjoint(even_numbers))


###################################### EXERCISE ############################################

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 24, 25, 26, 24, 28, 27}
age = {22, 19, 24, 25, 26, 24, 25, 24}

#it_companies_length = len(it_companies)
#print(it_companies_length)

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['X', 'DeepMind', 'Tesla', 'Meta'])
print(it_companies)

it_companies.pop()
it_companies.remove('DeepMind')
print(it_companies)
