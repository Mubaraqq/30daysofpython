"""
import re
txt = 'i love to teach python and js'
# re.match(substring, string, re.I) - searches only in the beginning of the first line of string 
# returns matched object if found, else returns none
# re.I is case ignore 
match = re.match('i love to teach', txt, re.I) 
print(match)

# we can get the starting and ending position of the match as tuple using span
span = match.span()
#print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

import re
text = 'i love to teach python and Rust'
match = re.match('i like to teach', text, re.I)
print(match)


import re
text = "python is the most beautiful language that human being has ever created. i recommend python for a first programming language"
# re.search(substring, text, re.I) - returns an object with span and match
# much better than match becouse it can look for the pattern throughout the text
# returns a match object with the first match that was found, otherwise returns None
search = re.search('first', text, re.I)
print(search)
span = search.span()
#print(span)
start, end = span
print(start, end)
print(text[start:end])

import re
text = "python is the most beautiful language that human being has ever created. i recommend python for a first programming language"

# re.findall(substring, string, re.I) - returns a list of all matches 
findall = re.findall('language', text, re.I)
print(findall)
findall_py = re.findall('python', text, re.I)
print(findall_py)

# since we are using re.I both upper and lowercase are inclined. can be done differently.
findall_py0 = re.findall('python|Python', text) 
findall_py1 = re.findall('[Pp]ython', text)
print(findall_py0)
print(findall_py1)

import re
text = "python is the most beautiful language that human being has ever created. i recommend python for a first programming language"
# re..sub(substring, substring, string) - replacing a substring 
#sub_replaced = re.sub('python', 'GO', text)
sub_replaced = re.sub('Python|python', 'Rust', text)
#sub_replaced = re.sub('[p|P]ython', 'C')
print(sub_replaced)

import re 

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
sub_replaced = re.sub('%', '', txt)
print(sub_replaced)

import re
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
# re.split(pattern, string) - splits a string whereever pattern matches
print(re.split('\n', txt))

import re
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
# to declare a RegEx variable we use r''
regex_pattern = r'apple'
matches = re.findall(regex_pattern, txt)
#print(matches)

# to make case insensitive adding flag
matches = re.findall(regex_pattern, txt, re.I)
#print(matches)

# or we can use a set of characters method
regex_pattern = r'[a|A]pple'
matches = re.findall(regex_pattern, txt)
print(matches)

# escape character (\) in RegEx
import re
regex_pattern = r'\d' # d means match where the string contains digit 0 - 9
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
#print(matches)

regex_pattern0 = r'\d+' # + means one or more time
matches0 = re.findall(regex_pattern0, txt)
print(matches0)

# period (.) RegEx
import re
regex_pattern = r'[a].' # a and any character except new line
txt = 'Apple and banana are fruits'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern1 = r'[a].+' # a and any character one or more time
matches1 = re.findall(regex_pattern1, txt)
print(matches1)

# zero or more times (*)
import re
regex_pattern = r'[a].*' # a and any character zero or more times
txt = 'Apple and banana are good'
matches = re.findall(regex_pattern, txt)
print(matches)

# zero or one time (?)
import re
txt = 'i am not sure if there is a convention how to write the word e-mail. some people write it as email others may write it as Email or E-mail'
regex_pattern = r'[Ee]-?mail' # E or e and - is optional followed by mail
matches = re.findall(regex_pattern, txt)
print(matches)

# curly bracket ({}) in regex
import re
txt = 'this regular expression examaple was made on June 11, 2025 and revised on June 12, 2025'
regex_pattern = r'\d{4}' # only digits exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern1 = r'\d{1,4}' # 1 to 4 
matches1 = re.findall(regex_pattern1, txt)
print(matches1)
"""
# carts ^ - starts with
import re
txt = 'this regular expression examaple was made on June 11, 2025 and revised on June 12, 2025'
regex_pattern = r'^this' # ^ mean start with 
matches = re.findall(regex_pattern, txt)
print(matches)

# neagtion - ^ in set character means negation
regex_pattern1 = r'[^A-Za-z ]' # not A-Z, not a-z, no space
matches1 = re.findall(regex_pattern1, txt)
print(matches1)


