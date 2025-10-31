################################
# Title: Google Python Certificate
# Description: Loops
# Change Log:
# JP, Created, 10.31.25
################################

# # Practice 1
# def is_power_of_two(number):
  
#   # This while loop checks if the "number" can be divided by two
#   # without leaving a remainder. How can you change the while loop to
#   # avoid a Python ZeroDivisionError?
#   while number % 2 == 0 and number != 0:
#     number = number / 2
#   # If after dividing by 2 "number" equals 1, then "number" is a power
#   # of 2.
#   if number == 1:
#     return True
#   return False
  
# # Calls to the function
# print(is_power_of_two(0)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False

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
        # Point of learning: You got confused by adding a print statement to see if it went through each iteration.
        
    return sum

print('this is round 1',sum_of_integers(3))  # should print 6
print('this is round 2',sum_of_integers(4))  # should print 10
print('this is round 3',sum_of_integers(5))  # should print 15