#########################   string methods   ##################
"""
    # capitalize() - convert the first character of the string to caps
challenge = 'thirty days of python'
print(challenge.capitalize())

    # count() - 
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14)) # 7 and 14 being the starting and ending indexes
print(challenge.count('th'))

    # endswith() -
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

    # expandtabs() - 
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs(10))
print(challenge.expandtabs(2))


    # find() - returns the index of the first occurrence of a substring, if not found
    #            return -1 
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))
print(challenge.find('m'))


    # rfind() - return the index of the last occurrence of a substring, if not found
    #            return -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))
print(challenge.rfind('m'))


    # index() - return the lowest index of substring, if not found it raises a valueError
challenge = 'thirty days of python'
#substring = 'da'
print(challenge.index('da'))
#print(challenge.index('da', 9)) #additional arguments indicates starting and ending index


    # rindex() - return the highest index of substring, if not found it raises a valueError
challenge = 'thirty days of python'
print(challenge.index('da'))
print(challenge.index('da', 2, 9))


    # isalnum() - checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())
challenge = '30DaysPython'
print(challenge.isalnum())
challenge = 'Thirty Days Of Python'
print(challenge.isalnum())


    # isalpha() - chacks if all string elements are alphabet characters
challenge = 'Thirty days of Python'
print(challenge.isalpha())
challenge = 'ThirtydaysofPython'
print(challenge.isalpha())
num = '123'
print(num.isalpha())


    # isdecimal() - checks if characters in a string are decimal
challenge = 'Thirty days of python'
print(challenge.isdecimal())
challenge = '123'
print(challenge.isdecimal())
challenge = '\u00B2'
print(challenge.isdecimal())
challenge = '12 3'
print(challenge.isdecimal())


    # isdigit() - checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'thirty'
print(challenge.isdigit())
challenge = '\u00B2'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())


    # isnumeric() - check if all characters in a string are numbers or number related
    #               just like isdigit(), just accept more symbols like 1/2
num = '10'
print(num.isnumeric())
num = '\u00BD' #1/2
print(num.isnumeric())
num = '10.5'
print(num.isnumeric())


    # isidentifier() - check for a valid identifier, if a string is a valid variable name
challenge = '30DaysofPython'
print(challenge.isidentifier())
challenge = 'thirt_days_of_python'
print(challenge.isidentifier())


    # islower() and isupper()
challenge = 'thirty days of python'
print(challenge.isupper())
print(challenge.islower())


    # join() - return a concatenated string
web_tech = ['HTML', 'CSS', 'JS', 'React']
result = '-'.join(web_tech)
print(result)

    # strip() - remove all given characters starting from the beginning and end of the string
challenge = 'thirty days of python'
print(challenge.strip('noth'))


    # replace() - replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))


    # split() - split the string, using given string or space as a separator.
challenge = 'thirty days of python'
print(challenge.split(','))


    # title() - returns a title cased string
challenge = 'thirty days of python'
print(challenge.title())


    # swapcase() - convert all uppercase characters to lowercase and vice-versa
challenge = 'thirty days of python'
print(challenge.swapcase())


    # startswith() - checks if a string starts with a specified string
challenge = 'thirty days of python'
print(challenge.startswith('python'))
print(challenge.startswith('thirty'))


################################################ EXERCISES #########################################################

str1 = 'Thirty'
str2 = 'Days'
str3 = 'of'
str4 = 'Python'
concat3n = str1 + str2 + str3 + str4
print(concat3n)


str1 = 'Coding'
str2 = 'For'
str3 = 'All'
conc = str1 + ' ' + str2 + ' ' + str3
print(conc)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
first_word = company[0:6]
print(first_word)

    # checking if 'Coding For All' string contains a word 'Coding' using index and find methods
text = 'Coding For All'
print(text.find('Coding')) # returns -1 if not found

text = 'Coding For All'
print(text.index('Coding')) # throws a ValueError if not found

text = 'Coding For All'
print(text.replace('Coding', 'Python'))

text = 'python for everyone'
print(text.replace('everyone', 'all'))

text = 'Coding For All'
print(text.split(' '))

text = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon,'
print(text.split())

text = 'Coding For All'
print(text[0])

text = 'Coding For All'
last_index = len(text) - 1
print(last_index)

text = 'Coding For All'
print(text[10])

text = 'Coding For All'
print(text.index('C'))
print(text.index('F'))
print(text.rindex('l'))  # last occurence

text = 'Coding For All'
print(text.rfind('l'))

text = 'you cannot end a sentence with becouse becouse becouse is a conjunction'
print(text.find('becouse'))
print(text.index('becouse'))
print(text.rindex('becouse'))
slighhng = text[0:31]
slighhng2 = text[54:]
addng = slighhng + slighhng2
print(addng)
"""
text = 'Coding For All'
print(text.startswith('Coding'))
print(text.endswith('Coding'))
