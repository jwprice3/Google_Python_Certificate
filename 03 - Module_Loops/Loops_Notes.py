# ################################
# # Title: Google Python Certificate
# # Description: Loops
# # Change Log:
# # JP, Created, 11.6.25
# ################################

# # Addittional Resources
#     # https://www.tutorialsteacher.com/python/python-map-function
#     # https://pythonprogramming.net/zip-intermediate-python-tutorial/

# #### WHILE LOOP ####
# '''
# A while loop will continuously execute code depending on the value of a condition. It begins with the keyword while, followed by a comparison to be evaluated, then a colon. On the next line is the code block to be executed,
# indented to the right. Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. What sets a while loop apart, however, is that this code block will keep executing as 
# long as the evaluation statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.
# '''

# # example 1
# x =   0
# while x < 5:
#     print("Not there yet, x=" + str(x))
#     x = x + 1
# print("x=" + str(x))

# # example 2
# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x += 1
#     print("Done")
# attempts(5)

# # example_break
# # This function outputs an addition table. It is written to end after
# # printing 5 lines of the addition table, but it will break out of the
# # loop if the "my_sum" variable exceeds 20.

# # The function accepts a "given_number" variable through its
# # parameters.
# def addition_table(given_number):

# 	# The "iterated_number" and "my_sum" variables are initialized with
# 	# the value of 1. Although the "my_sum" variable does not need any
# 	# specific initial value, it still must be assigned a data type
# 	# before being used in the while loop. By initializing "my_sum"
# 	# with any integer, the data type will be set to int.
# 	iterated_number = 1
# 	my_sum = 1

# 	# The while loop will run while it is True that the
# 	# "iterated_number" is less than or equal to 5.
# 	while iterated_number <= 5:

# 		# The "my_sum" variable is assigned the value of the
# 		# "given_number" plus the "iterated_number" variables.
# 		my_sum = given_number + iterated_number

# 		# Test to see if the "my_sum" variable is greater than 20.
# 		if my_sum > 20:
# 			# If True, then use the break keyword to exit the loop.
# 			break

# 		# If False, the Python interpreter will move to the next line
# 		# in the while loop after the if-statement has ended.

# 		# The print function will output the "given_number" plus
# 		# the "iterated_number" equals "my_sum".
# 		print(str(given_number), "+", str(iterated_number), "=", str(my_sum))

# 		# Increment the "iterated_number" before the while loop starts
# 		# over again to print a new "my_sum" value.
# 		iterated_number += 1


# addition_table(5)
# addition_table(17)
# addition_table(30)

# #example_4
# greeting = 'Hello'
# index = 0
# while index < len(greeting):
# 	print(greeting[index])
# 	index += 1

# # Expected output:
# # 5 + 1 = 6
# # 5 + 2 = 7
# # 5 + 3 = 8
# # 5 + 4 = 9
# # 5 + 5 = 10
# # 17 + 1 = 18
# # 17 + 2 = 19
# # 17 + 3 = 20
# # None

# #### FOR LOOP ####
# '''
# # For loops iterate over a sequence of elements, executing the body of the loop for each element in the sequence
# # For loops when there's a sequence of elements that you want to iterate.
# # 	An important distinction is that for loops are suited for objects that have iterable structures.
# # 	So lists, strings, ranges of integers. Individual integers are not iterable, but can be looped over
# # 	by the use of the range() function, which is covered below. While loops do not iterate per se, rather they watch a truth condition 
# '''

# # example_1
# '''
# The in keyword with the range() function generates a sequence of integer numbers, which can be used with a for loop to configure the
# iterations of the code. The range of numbers [0, 1, 2] correlates to ordinal index positions (1st, 2nd, 3rd), rather than the cardinal 
# (quantity) values of the numbers 0, 1, and 2. For example, range(5) means the five index positions in the range [0, 1, 2, 3, 4].
# Range Method = range(start,stop,step).
# FYI: upper limit of range is not included
# '''
# product = 1
# for n in range(1,10):
#   product = product * n

# print(product)

# def to_celsius(x):
#   return (x-32)*5/9

# for x in range(0,101,10):
#   print(x, to_celsius(x))

# #### NESTED LOOP ####
# '''
# for x in sequence:
#     # start of the outer loop body
#     for y in sequence:
#         # start of the inner loop body
#         # end of of the inner loop body
#     # continue body of the outer loop
#     # end of the outer loop body
# '''
# # examle_1
# for left in range(7):
#   for right in range(left, 7):
#     print("[" + str(left) + "|" + str(right) + "]", end=" ")
#   print()

# # example_2
#   teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#   for away_team in teams:
#     if home_team != away_team:
#       print(home_team + " vs " + away_team)

# # example_3_strings
# greeting = 'Hello'
# for char in greeting:
# 	print(char)

# '''
# When you slice a string, you extract a subset of the original string—sometimes referred to as indexing a string.
# Joining strings is the process of linking two or more strings together to create a bigger string.
# '''
# # example_1
# string1 = "Greetings, Earthlings"
# print(string1[0])   # Prints “G”
# print(string1[4:8]) # Prints “ting”
# print(string1[11:]) # Prints “Earthlings”
# print(string1[:5])  # Prints “Greet”

# # example 2_error
# # Prints “” 
# print(string1[55:])

# # example_3 string_step
# # Prints “Getns atlns”
# print(string1[0::2])

# # Prints “sgnilhtraE ,sgniteerG”
# print(string1[::-1])

# #example_4 joining_strings
# greetings = ["Hello", "world"]
# print(" ".join(greetings))  # Prints "Hello world"

# # You can also concatenate a combination of strings and variables like in the following example.
# name = "Alice"
# print("Hello, " + name + "!")  # Prints "Hello, Alice!"

# # List Comprehension
# '''
# The concepts for loops are similar between other languages, but in Python,
# list comprehensions provide a concise way to create lists based on existing lists or sequences. 
# '''
# sequence = range(10)
# new_list = []
# for x in sequence:
#     if x % 2 == 0:
#         new_list.append(x)
        
# # or 

# sequence = range(10)
# new_list = [x for x in sequence if x % 2 == 0]

# # Recursion
'''
Limit of 1000 nested levels
'''
'''
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
'''

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    # this will iterate from 3 to 1 or 5 to 1
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15