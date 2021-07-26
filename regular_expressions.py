'''
Regular expressions allow you to Locate and change strings in very powerful ways.
They work in almost exactly the same way in every programming language as well.

Regular expressions (REGEX) are used to:
1 - Search for a specific string in a Large amount of data
2 - Verify that a string has the proper format (Email, phone #)
3 - Find a string and replace it with another string
4 - Format data into the proper form for importing for example
'''

#importando a biblioteca regex
import re

print('Was a match found')
print('** procurando a palavra ape na frase: The ape was at the apex')
#procurando 'ape' na string
if re.search('ape', 'The ape was at the apex'):
    print('There is an ape')

print('\nGet all matches - findall')
#findall() returns a list of matches
#. is used to match any 1 character or space

allApes = re.findall('ape.', 'The ape was at the apex')

for i in allApes:
    print(i)

print('\nGet all matches - finditer')
#finditter() returns an iterator of matching objects
#you can use span to get the location

theStr = 'The ape was at the apex'

for i in re.finditer('ape.', theStr):
    #span() returns a tuple
    locTuple = i.span()
    print('index location range: ', locTuple)

    #slice the match out using the tuple values
    print('string found: ', theStr[locTuple[0]:locTuple[1]])

print('\nMatch 1 of several letters')
#square brackets will match any one of the characters between the brackets not including
#upper or lowercase varieties unless they are listed

animalStr = 'Cat rat mat fat pat'
allAnimals = re.findall('[crmfp]at', animalStr)

print('String: ', animalStr)
print('... procurando as palavras que começam com "c, r, m, f ou p" e terminam com at')
for i in allAnimals:
    print(i)

print('... procurando as palavra que não começam com "C ou r" e terminam com at')

someAnimals = re.findall('[^Cr]at', animalStr)
for i in someAnimals:
    print(i)

print('\nReplace all matches')
owlFood = 'rat cat mat pat'
print(owlFood)

print('... substituindo as palavras que começam com "c" e "r" e terminam com "at" por "owl"')
#you can compile a regex into pattern objects which provide additional methods
regex = re.compile('[cr]at')
#sub() replaces items that match the regex in the string with the 1st attribute string passed to sub
owlFood = regex.sub('owl', owlFood)
print(owlFood)

print('\nSolving Backlash Problems')
#regex use the backlash to designate special characters and Python does the same inside
#strings which causes issues

#let's try to get "\\stuff" ou of  a string
randStr = 'Here is \\stuff'
print(randStr)

#this won't find it
print('Find \\stuff: ', re.search('\\stuff', randStr))

#this does, but we have to put in 4 slashes which is messy
print('Find \\stuff: ', re.search('\\\\stuff', randStr))

#you can get around this by using raw  strings which don't treat backslashes as special
print('Find \\stuff: ', re.search(r'\\stuff', randStr))

print('\nMatching any character')
#we saw that . matches any character, but what if we want to match a period.
#Backslash the period you do the same with [,] and others
randStr = 'F.B.I. I.R.S. CIA'

print(randStr)
print('Qt Matches : ', len(re.findall('.\..\..', randStr)))
print('Matches : ', re.findall('.\..\..', randStr))

print('\nMatching Whitespaces')
#we can match many whitespace characters
randStr = '''This is a long
string that goes
on for many lines'''
print(randStr)

#remove new lines
regex = re.compile('\n')

randStr = regex.sub(' ', randStr)
print('\n', randStr)

#you can also match
#\b : Backspace
#\f : Form Feed
#\r : Carriage Return
#\t : Tab
#\v : Vertical Tab

#you may need to remove \r\n on Windows

print('\nMatching Any Single Number')
#\d can be used instead of [0-9]
#\D is the same as [^0-9] - not
randStr = '12345'
print(randStr)
print('Qt Matches : ', len(re.findall('\d', randStr)))
print('Matches : ', re.findall('\d', randStr))

print('\nMatching Multiple Numbers')
#you can match multiple digits by following the \d with {numOfValues}

#match 5 numbers only
if re.search('\d{5}', '12345'):
    print('It is a zip code')

print()

#you can also match within a range
#match values that are between 5 and 7 digits
numStr = '123 12345 123456 1234567'

print(numStr)
print('Qt Matches (5,7) : ', len(re.findall('\d{5,7}', numStr))) #\d{5,7} - de 5 a 7
print('Matches : ', re.findall('\d{5,7}', numStr))

print('\nMatching Any Single Letter or Number')
#\w is the same as [a-zA-Z0-9_]
#\W is the same as [^a-zA-Z0-9_]

phNum = '412-555-1212'
print(phNum)

#check if it is a phone number
if re.search('\w{3}-\w{3}-\w{4}', phNum):
    print('It is a phone number')

name = 'Ultraman'
print(name)

#check for valid first name between 2 and 20 characters
if re.search('\w{2,20}', name):
    print('It is a valid name')

print('\nMatching Whitespace')
#\s is the same as [\f\n\r\t\v]
#\S is the same as [^\f\n\r\t\v]

name = 'Toshio Muramatsu'
print(name)

#check for valid first and last name with a space
if re.search('\w{2,20}\s\w{2,20}', name):
    print('It is a valid full name')

print('\nMatching One or More')
#+ matches 1 or more characters

randStr = 'a as ape bug'
print(randStr)

#match a followed by 1 or more characters
print('Qt Matches : ', len(re.findall('a+', randStr)))
print('Matches : ', re.findall('a+', randStr))

print('\nProblem')
#create a Regex that matches email adresses from a list
#1 - 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
#2 - an @ symbol
#3 - 2 to 20 lowercase and uppercase letters, numbers, plus .-
#4 - a period
#5 - 2 to 3 lowercase and uppercase letters

emailList = 'db@aol.com m@.com @apple.com db@.com'
print(emailList)

print('Qt Email Matches : ', len(re.findall('[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}', emailList)))
print('Qt Email Matches : ', re.findall('[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}', emailList))
