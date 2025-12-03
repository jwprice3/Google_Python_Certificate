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