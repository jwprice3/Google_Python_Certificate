################################
# Title: Google Python Certificate
# Description: Module 3 Challenge
# JP, Created, 11.18.25
################################
'''
Question 1:
Fill in the blanks to print the numbers 1 through 7.
'''

# number = 1 # Initialize the variable
# while number < 8: # Complete the while loop condition
#     print(number, end=" ") # end creates a new variable with has a space
#     number += 1 # Increment the variable

# # Should print 1 2 3 4 5 6 7 
# print('next question')
'''
Question 2:
Find and correct the error in the for loop below. The loop should check each number
 from 1 to 5 and identify if the number is odd or even.  
'''
# for number in range(1,5+1):
#     if number % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# Should print:
# odd
# even
# odd
# even
# odd

'''
Question 3: 
Fill in the blanks to complete the function “digits(n)” to count how many digits the
 given number has. For example: 25 has 2 digits and 144 has 3 digits. 
'''
 # def digits(n):
#     count = 0
#     if n == 0:
#       count += 1
#     while n != 0:
#         n //=10
#         count += 1
#         # Complete the while loop condition
#         # Complete the body of the while loop. This should include 
#         # performing a calculation and incrementing a variable in the
#         # appropriate order.  
#     return count
    
# print(digits(25))   # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000)) # Should print 4
# print(digits(0))    # Should print 1

# 
# Question 4:
# Fill in the blanks to complete the “multiplication_table” function. 
# This function should print a multiplication table, where each number is 
# the result of multiplying the first number of its row by the number 
# at the top of its column. Complete the range sequences in the nested 
# loops so that “multiplication_table(1, 3)” will print:

# 1 2 3

# 2 4 6

# 3 6 9
# '''

# def multiplication_table(start, stop):
#     # Complete the outer loop range
#     for x in range(1,4): 
#          # Complete the inner loop range
#         for y in range(1,4):
#             # Prints the value of "x" multiplied by "y" 
#             # and inserts a space after each value
#             #print('Multipliers were',str(x),str(y))
#             print(str(x*y), end=" ")
#         # An empty print() function inserts a line break at the 
#         # end of the row 
#         print()


# multiplication_table(1, 3)
# # Should print the multiplication table shown above

'''
Question 5:
Fill in the blanks to complete the “divisible” function. This function 
should count the number of values from 0 to the “max” parameter minus 1 
that are evenly divisible by the “divisor” parameter. This means they 
do not have a remainder when divided by the divisor. Complete the code 
so that a function call like “divisible(100,10)” will return the number
 “10”.
'''
# def divisible(max, divisor):
#     count = 0 # Initialize an incremental variable
#     for x in range(0, max): # Complete the for loop
#         if x % divisor == 0:
#             count += 1 # Increment the appropriate variable
#     return count

# print(divisible(100, 10)) # Should be 10
# print(divisible(10, 3)) # Should be 4
# print(divisible(144, 17)) # Should be 9
'''
Fill in the blanks to complete the “all_numbers” function. This function should
 return a space-separated string of all numbers, from the starting   “minimum” 
 variable  up to and including the “maximum” variable that's passed into the function.
Complete the for loop so that a function call like “all_numbers(3,6)” will return the numbers “3 4 5 6”.  
'''
# def all_numbers(minimum, maximum):

#     return_string = "" # Initializes variable as a string

#     # Complete the for loop with a range that includes all 
#     # numbers up to and including the "maximum" value.
#     for count in range(minimum,maximum + 1):

#         # Complete the body of the loop by appending the number
#         return_string = return_string + str(count) + " "
#         # followed by a space to the "return_string" variable.
#     return return_string.strip(" ")

#     # This .strip command will remove the final " " space 
#     # at the end of the "return_string".
    
# print(all_numbers(2,6))  # Should be 2 3 4 5 6
# print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
# print(all_numbers(-1,1)) # Should be -1 0 1
# print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
# print(all_numbers(0,0))  # Should be 0

print('Hello')