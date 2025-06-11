############################  DICTIONARY  #############################

empty_dict = {}
print(empty_dict)

dtc = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    'key4':'value4',
    }

person = {
    'first_name':'Joe',
    'last_name':'Paul',
    'age':25,
    'country':'Finland',
    'is_married': True,
    'skills':['JS', 'CSS', 'Node', 'Python', 'Pytorch'],
    'address':{
        'street':'space road',
        'zipcode':'02210',
    }
    } 


print(person['first_name'])  # accessing item by key name
print(person['country'])
print(person['is_married'])
print(person['skills'][3])
print(person['address']['street'])

print(person.get('first_name'))
print(person.get('country'))
print(person.get('is_marrried'))
print(person.get('skills')[3])
print(person.get('city'))  # the get() returns none if the key doesn't exist instead of error 

    # adding items to a dictionry
dct = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
}
dct['key4'] = 'value4'
print(dct)


dct['key4'] = 'value_four' # modifying a dict
print(dct)


person = {
    'first_name':'Joe',
    'last_name':'Paul',
    'age':25,
    'country':'Finland',
    'is_married': True,
    'skills':['JS', 'CSS', 'Node', 'Python', 'Pytorch'],
    'address':{
        'street':'space road',
        'zipcode':'02210',
    }
    } 

person['first_name'] = 'Eyub'  # modifying person dct
person['age'] = 250

print(person)

person['job_title'] = 'instructor'  # adding item - key:value
person['skills'].append('HTML') 
print(person)

    # checking keys in a dictionary
dtc = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
    'keey4' : 'value4',
}
print('key2' in dtc)
print('key5' in dtc)

    # removing key and value pair from a dict
dtc = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
    'key4' : 'value4',
}
#print(dtc)
dtc.pop('key2')  # pop() - removes item with specified key name
#print(dtc)
dtc.popitem() # popitem() - removes the last item
#print(dtc) 
del dtc['key3'] # del - removes an item with specified key name
print(dtc)

    # changing dictionary to a list of items *tuple*
dtc = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
    'key4' : 'value4',
}
print(dtc.items()) # items() - change dictionary to a list of tuple
print(dtc.clear()) # if we dont want the items in a dictionary we can clear them using clear()

    # deleting a dictionary - del 
dtc = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
    'key4' : 'value4',
}
del dtc
print(dtc)

    # copying a dictionary - copy()
dtc = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
    'keey4' : 'value4',
}
dtc_copy = dtc.copy()
print(dtc_copy)

    # getting a dictionary keys as a list - keys()
dtc = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
    'key4' : 'value4',
}
keys = dtc.keys() # keys() - gives the keys of a dict as a list 
print(keys)

    # getting a dict values as a list - values()
dtc = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
    'keey4' : 'value4',
}
values = dtc.values()
print(values)


###################################### EXERCISES #####################################################
# empty dictionary
#dog = dict()
dog = {}
print(dog)

empty_dtc = {
    'name':'black',
    'color':'black',
    'breed':'cat',
    'legs': 4,
    'age': 6,
}
print(empty_dtc)


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
#print(student_dict)
#print(len(student_dict))

skillz = student_dict['skills']
print(skillz)
print(type(skillz))
