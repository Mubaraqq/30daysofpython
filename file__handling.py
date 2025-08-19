
"""
# opening file for reading
f = open('./30DaysOfPython/reading_file_example.txt')
print(f) # file object representation

f = open('./30DaysOfPython/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close() # closes the file opened with open() - technically necessary

with open('./30DaysOfPython/reading_file_example.txt') as f: # with(context manager) handles closing files automatically
    txt = f.read()
    print(type(txt))
    print(txt)

# readline() - read only the first line
with open('./30DaysOfPython/reading_file_example.txt') as f:
    line = f.readline()
    print(type(line))
    print(line)

# readlines() - read all text line by line and return as list of lines
with open('./30DaysOfPython/reading_file_example.txt') as y:
    lines = y.readlines()
    print(lines)

# another way to get all the lines as a list using splitlines()
with open('./30DaysOfPython/reading_file_example.txt') as x:
    lines = x.read().splitlines()
    print(type(lines))
    print(lines)

    # opening files for writting and updating 
# to write to an existing file, we must add a mode as parameter to the open() function
# a - append, will append to the end of the file. if the file does not exist it creates new file.
with open('./30DaysOfPython/reading_file_example.txt', 'a') as f: 
    f.write('This text has to be append at the end')

# reading the file
with open('./30DaysOfPython/reading_file_example.txt') as f:
    content = f.read()
    print(content)

# w - write, will overwrite any existing content, if the file does not exist it creates
with open('./30DaysOfPython/reading_file2', 'w') as f:
    f.write('This text will be writiten in a new created file')

# reading the file
with open('./30DaysOfPython/reading_file2') as f:
    print(f.read())


# deleting files - to remove a file we can use os module
import os
#print(os.getcwd())

with open('./30DaysOfPython/reading_file3', 'w') as f:
    f.write('This text will be writiten in a new created file')

print(os.path.exists('./30DaysOfPython/reading_file3')) # check if the file exists
os.remove('./reading_file3')

#if the file does not exist, the remove method will raise an error, so it is good to use a condition
import os
if os.path.exists('./30DaysOfPython/reading_file3'):
    os.remove('./30DaysOfPython/reading_file3')
else:
    print('file not found!')


    # file types
# file with json extension - js object notation - a stringified python dictionary
person_dict = {
    'name': 'Ahmad',
    'country': 'Qatar',
    'city': 'Doha',
    'skills': ['C', 'python', 'matlab']
}

# JSON - a string form of dictionary
person_json = "{'name': 'Ahmad', 'country':'Qatar', 'city':'Doha', 'skills':['JS', 'python', 'matlab']}"

# three quotes and multiple line to make it more readable
person_json = '''{
'name':'Ahmad',
'country':'Qatar',
'city':'Doha',
'skills':['C', 'python', 'matlab']
}
'''
print(person_json)
print(type(person_json))


# changing json to dictionary - we import the json module and then use the loads method
import json

person_json = '''{
"name": "Ahamad",
"country": "Qatar",
"city": "Doha",
"skills": ["C", "python", "js"]
}
'''
person_dict = json.loads(person_json)
print(type(person_dict))
print(person_dict)

# changing dictionary to json - we use dumps method from the json module
import json

person = {
    'name': 'Ahmad',
    'country': 'Qatar',
    'city': 'Doha',
    'skills':['C', 'python', 'js']
}
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. it beautify the json
print(type(person_json))
print(person_json)

# saving as json file - we can also save data as json file. 
# for writing a json file, we use the json.dump() method
# it can take dict, output file, ensure_ascii and indent
import json

person = {
    'name': 'Ahmad',
    'country': 'Qatar',
    'city': 'Doha',
    'skills': ['C', 'python', 'js']
}
with open('./30DaysOfPython/json_file.json', 'w', encoding = 'utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


# file with csv extention - comma seperated values - file format used to store tabular data such as sheets and databases
# csv is a common data format in data science
import csv
# open a file in write mode 'w' creates if doesn't exist
with open('./30DaysOfPython/csv_example.csv', 'w', newline='') as f:
    csv_file = csv.writer(f) # we use writer() method to write csv files

    # write the header (column names) - metadata
    csv_file.writerow(['names', 'country', 'city', 'skills']) 

    # write some rows (data)
    csv_file.writerow(['Mubarak', 'Nigeria', 'Kano', 'Python'])
    csv_file.writerow(['Aisha', 'Ghana', 'Accra', 'JavaScript'])
    csv_file.writerow(['John', 'Kenya', 'Nairobi', 'Go'])

import csv
with open('./30DaysOfPython/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use reader() method to read csv files
    
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names are: {','.join(row)}')
            line_count += 1
        else:
            print(f'\t {row[0]} is a teacher. he lives in {row[1]}, {row[2]}')
            line_count += 1
    print(f'number of lines: {line_count}')


    # python pip
# installing packages using pip
pip install pip  # to install pip on cmd prompy or terminal 
pip --version  # check if pip is install 

# numpy 
#pip install numpy # to install numpy 
import numpy
#print(numpy.version.version) 

lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst) # to perform element-wise operations
print(np_arr)
print(len(np_arr))
print(np_arr * 2)
print(np_arr + 2)

# pandas - python data analysis lib - built on top of numpy, designed specifically for working with structured data
# like tables, spreadsheets, databases and csv files
pip install pandas # to install pandas
import pandas

# webbrowser - help to open any website, preinstalled 
import webbrowser 

# list of urls:
url_lists = [
    'http://www.python.org',
    'http://linkedin.com',
    'http://github.com/mubaraqq',
    'http://x.com/mubaraqabba'
]
# open the above list of website in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

# uninstalling packages 
pip uninstall packagename

# list of packages - to see the install packages 
pip list 

# show package - to show information about a package 
pip show packagename
pip show pandas # to show info about pandas
pip show --verbose pandas # we add --verbose if we want more details 

# pip freeze - gave the packages used, installed and their versions. use it with requirements.txt file for deployment.
pip freeze 


    # reading from URL - to open a network connection, we use a package called requests
# it allows to open a network connection and implement CRUD
import requests 

# text from a website
url = 'https://www.pythonanywhere.com/login/?next=/registration/register/complete/'

# opening a network and fetching a data 
response = requests.get(url)
print(response)

# checking the status of the get operation
print(response.status_code)

# headers information
print(response.headers)

# gives all text from the page
print(response.text)


# let us read from an API 
import requests

# countries api
url = 'https://restcountries.com/v3.1/all?fields=name,capital' 

# opening a network and fetching data
response = requests.get(url) 

# response object
print(response) 

# status_code
print(response.status_code)  
countries = response.json()

#slice only the first countries
print(countries[:1])   


    # creating a package 
# a package is simply a folder containing one or more module files

# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a, b):
    return a - b

def multiple(a, b):
    return a * b

def division(a, b):
    return a / b

def reminder(a, b):
    return a % b

def power(a, b):
    return a ** b

# mypackage/greet.py
# greet.py
def greet_person(fname, lname):
    return f'{fname} {lname}, welcome!'

# modules are called  in main.py file
"""

from my_package import arithmetic
from my_package import greet

print(greet.greet_person('Fatima', 'Hatun'))

