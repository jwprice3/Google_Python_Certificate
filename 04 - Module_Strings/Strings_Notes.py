################################
# Title: Google Python Certificate
# Description: Module 4 Notes
# JP, Created, 12.3.25
################################

'''
What is a string?
'''
name = "Sasha"
color = 'Gold'
# basic string creation

place = "Cambridge'
#This will throw an error, qoutes mismatch

pet = ""
# empty variable but true

name = "Sasha"
color = 'Gold'
print("Name: " + name + ", Favorite color: " + color)

"example" * 3
# prints exampleexampleexample

pet = "loooooooooooooooooooooooooooooooog cat"
len(pet)
# shows the length of text in the variblae with a number i.e 38


'''
Creating Strings
'''
message = "A kong string with a silly typo"
message[2] = "l"
#This will throw an error

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)
# inserts/replaces the k with the l 

message = "This is a new message"
print(message)
message = "And another one"
print(message)

pets="Cats & Dogs"
pets.index("&")
pets.index("C")
pets.index("Dog")
pets.index("s")
# shows the position 

pets="Cats & Dogs"
pets.index("x")
#This will throw an error

pets="Cats & Dogs"
"Dragons" in pets
"Cats" in pets
# checks if the the combintion exist

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email
'''
Creating Strings
'''
'''
Indexing Strings
'''
animals = "lions tigers and bears"
animals.index("g")

animals = "lions tigers and bears"
animals.index("bears")

animals = "lions tigers and bears"
"horses" in animals

animals = "lions tigers and bears"
"tigers" in animals
'''
Indexing Strings
'''
'''
Strings Function
'''
"Mountains".upper()
"Mountains".lower()
# Changes the case for all text

answer = "YES"
if answer.lower() == "yes":
  print("User said yes")
# function to change the check

" yes ".strip()
# Striping spaces and text

" yes ".strip()
" yes ".lstrip() # removes space to the left
" yes ".rstrip() # removes space to the right
# Gets rid of surrondin spaces/tabs/new lines

"The number of times e occurs in this string is 4".count("e")
# Counts the amount of occurences for a given string

"Forest".endswith("rest")
# Checks is the statement is true

"Forest".isnumeric()
"12345".isnumeric()
# Confirms if the string is for data are numbers

int("12345") + int("54321")
#  Converts to an actual number

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])
# to combine/join strings

"This is another example".split()
# Makes a a list of the string
'''
Strings Function
'''
'''
Strings Formatting
'''
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
# Formats the expression

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} #spaces F | {:>6.2f} #decimal space C".format(x, to_celsius(x)))
# {:>3.2f} would align the text three spaces to the right, as well as specify a
#   float number with two decimal places. String formatting can be very handy for outputting easy-to-read textual output.
# formatting through a loop

print(len("abcde"))
# len(string) - Returns the length of the string 
# prints 5

for c in "abcde" # print(c)
# for character in string - Iterates over each character in the string

print("abc" in "abcde") # prints True
print("def" in "abcde") # prints False
# if substring in string - Checks whether the substring is part of the string

print("abcde"[2]) # prints "c"
print("abcde"[-1]) # prints "e"
# string[i] - Accesses the character at index i of the string, starting at zero

print("abcde"[0:2]) # prints "ab"
print("abcde"[2:]) # prints "cde"
# string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted, its value defaults
#  to 0. If j is omitted, Python returns everything from i to the end of the strin

print(test.split()) # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']
# string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)


test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-")) # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']
# string.split(delimiter) - Returns a list of substrings that were separated by whitespace or another string
#  a character or sequence of characters used to separate distinct parts within plain text or data streams

print(test.replace("wood", "plastic"))  # prints "How much plastic would a plasticchuck chuck"
# string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.

print("-".join(test.split())) # prints "How-much-wood-would-a-woodchuck-chuck"
# delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter