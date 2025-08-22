    # classes and objects
# - python is an object oriented programming language
# - everything in python is an object with properties and methods
# - we create a class to ceeate and object
# - class difines attributes and the behaviour of the object, while 
# - the object represent the class

num = 10
print(type(num)) # class - int

# creating a class 
class ClassName:
    code goes here

class Person:
    pass
print(Person)

# creating and object - we can create an object by calling the class
p = Person()
print(p)

# class constructor - a class without a constructor is not really useful in real apps
# the init() is python built in constructor function
# it has self parameter which is a reference to the current instance of the class

class Person:
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name
p = Person('Abba')
print(p.name)
print(p)

# let us add more parameter to the constructor function
class Person:
    def __init__(self, fname, lname, age, city):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.city = city
p = Person('Abba', 'Musa', 28, 'Daura')
print(p.fname)
print(p.lname)
print(p.age)
print(p.city)

# object methods - objects can have methods 
# the methods are functions which belong to the object
class Person:
    def __init__(self, fname, lname, age, city):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.city = city
    def person_info(self):
        return f'{self.fname} {self.lname} is {self.age} years old. He lives in {self.city}'
p = Person('Isa', 'Muhammad', 28, 'Doha')
print(p.person_info())

# object default methods - we can give default values for the parameter in the constructor
class Person:
    def __init__(self, fname = 'Joe', lname = 'Paul', age = 28, city = 'Abuja'):
        self.fname = fname 
        self.lname = lname
        self.age = age
        self.city = city
    def person_info(self):
        return f'{self.fname} {self.lname} is {self.age} years old. He lives in {self.city}'
p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 26, 'Noman city') # overrides the default parameters 
print(p2.person_info())

# method to modify class default values 
class Person:
    # all the constructor parameters have default values
    def __init__(self, fname = 'Musa', lname = 'Ali', age = 19, city = 'Tehran'):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.city = city
        #skills parameter than can be access using a method
        self.skills = [] # initializes the skills attribute, empty list
    def person_info(self):
        return f'{self.fname} {self.lname} is {self.age} years old. he lives in {self.city}'
    def add_skill(self, skill):
        self.skills.append(skill)
p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('js')
p2 = Person('John', 'Doe', 30, 'Noman')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

    # inheritance - reuse parent class code
# allows us to define a class that inherits all the methods and properties from parent class
# parent class/super/base class is the class which gives all methods and properties 
# child class is the class that inherits from another or parent class

# a student class that inherits from parent class
class Student(Person):
    pass
s1 = Student('Eyob', 'Salman', 20, 'Niamey')
s2 = Student('Salim', 'Shehu', 24, 'Kano')

print(s1.person_info())
s1.add_skill('React')
s1.add_skill('Node.js')
s1.add_skill('Go')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Marketing')
s2.add_skill('Organizing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# overriding parent method - we can add a new method to the child or override the parent class methods
# we can use super() built-in function or the parent name to automatically inherit the methods and properties
class Student(Person):
    # constructor of the child class, adding new gender parameter
    def __init__(self, fname='Musa', lname='Ali', age=19, city='Tehran', gender = 'male'):
        # calling the parent's constructor
        super().__init__(fname, lname, age, city)
        self.gender = gender
        # overrides the person_info() methods from the parent class
    def person_info(self):
        gender =  'he' if self.gender == 'male' else 'she'
        return f'{self.fname} {self.lname} is {self.age} years old. {gender} lives in {self.city}'
s1 = Student()
s2 = Student('Sara', 'Shuaib', 26, 'Doha', 'female')
print(s1.person_info())
s1.add_skill('js')
s1.add_skill('C')
s1.add_skill('C#')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Management')
s2.add_skill('Marketing')
s2.add_skill('Organizing')
print(s2.skills)


