################################
# Title: Google Python Certificate
# Description: Loops
# Change Log:
# JP, Created, 10.31.25
################################

# # Practice 1
#question 3
def is_power_of_two(number):
  
  #This while loop checks if the "number" can be divided by two
  #without leaving a remainder. How can you change the while loop to
  #avoid a Python ZeroDivisionError?
  while number % 2 == 0 and number != 0:
    number = number / 2
  #If after dividing by 2 "number" equals 1, then "number" is a power
  #of 2.
  if number == 1:
    return True
  return False
  
Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

#Question 4
def sum_of_integers(n):
    if n < 1:
        return 0


    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        i = i + 1
        # Point of learning: You got confused by adding a print statement to see if it went through each iteration.
        
    return sum

print('this is round 1',sum_of_integers(3))  # should print 6
print('this is round 2',sum_of_integers(4))  # should print 10
print('this is round 3',sum_of_integers(5))  # should print 15

# Practice 2
# I want to get the sum of each iteration up to the value of n
# Total = sum of each n
def sum_of_integers(n):
    if n < 1:
        return 0


    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        i = i + 1
#         # Point of learning: You got confused by adding a print statement to see if it went through each iteration.
        
    return sum

print('this is round 1',sum_of_integers(3))  # should print 6
print('this is round 2',sum_of_integers(4))  # should print 10
print('this is round 3',sum_of_integers(5))  # should print 15

#Fill in the blanks to complete the function, which should output a multiplication table. 
    #The function accepts a variable “number” through its parameters. 
    #This “number” variable should be multiplied by the numbers 1 through 5, and printed in a format similar to “1x6=6” (“number” x “multiplier” = “result”). The code should also limit the “result” to not exceed 25. To satisfy these conditions, you will need to:
#Initialize the “multiplier" variable with the starting value
#Complete the while loop condition
#Add an exit point for the loop
#Increment the “multiplier" variable inside the while loop

def multiplication_table(number):
    # Initialize the appropriate variable
    # create a variable for the iteration
    multiplier = 1

    # Complete the while loop condition.
    while multiplier < 6:
        result = number * multiplier 
        if  result > 25:
            # Enter the action to take if the result > 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Point of learning: Add to the iteration after it goes through the iteration
            # variable += 1 is the same as variable = variable + 1
        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3) 
# Should print: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15


multiplication_table(5) 
# Should print: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25


multiplication_table(8) 
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24
