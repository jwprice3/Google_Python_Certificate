################################
# Title: Google Python Certificate
# Description: Loops_Practice_1
# Change Log:
# JP, Created, 11.7.25
################################

# print('Which option would fix this for loop to print the numbers 12, 18, 24, 30, 36?')
'''
good
'''
# for n in range(0,36+1,6):
#     print(n)

# print('Which for loops will print all even numbers from 0 to 18? Select all that apply.')
# for n in range(19):
#     if n % 2 == 0:
#         print(n)

# for n in range(10):
#   print(n+n)

#print('Question 4 Fill in the blanks so that the for loop will print the first 10 cube numbers (x**3) in a range that starts with x=1 and ends with x=10.')
# for x in range(1,11):
#   print(x**3)

#   print('Write a for loop with a three parameter range() function that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that are not multiples of 7. Remember that 0 is also a multiple of 7. ')
#   for x in range(0,100,7): 
#     print(x)

# print('Which of these options would output just the vowels from the following string? Select all that apply.')
#input = "Four score and seven years ago"
# for c in input:
#   if c.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print(c)

#print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])

#print(input.count("aeiou"))

# for c in range(len(input)):
#   if c in ['a', 'e', 'i', 'o', 'u']:
#     print(c)

# # Practice Quiz Recursion
# def is_power_of(number, base):
#  # Base case: when number is smaller than base.
#     if number < base:
#         # If number is equal to 1, it's a power (base**0).
#         return number == 1

#     # Recursive case: keep dividing number by base.
#     return is_power_of(number / base, base) # this is technically two arguments


# print(is_power_of(8,2))     # Should be True
# print(is_power_of(64,4))    # Should be True
# print(is_power_of(70,10))   # Should be False

# Recurion Quiz Question 4
'''
In the provided code, the count_users function uses recursion to count the number of users that belong
to a group within a company's system. It does this by iterating through each member of a group, and if a
member is another group, it recursively calls count_users to count the users within that subgroup. However,
there is a bug in the code! Can you spot the problem and fix it?
'''
''''
Explanation:
The original code has a subtle off-by-one error: It increments count += 1 for every member, including subgroups. This counts subgroups as if they were users, leading to overcounting in nested structures. For example, if a group has 2 users and 1 subgroup with 1 user, it would count 4 instead of 3.

To fix it, move the increment to only apply when member is not a group (i.e., it's an individual user). Subgroups should only contribute their recursive user count, without being counted themselves.

Here's the corrected version:
'''
# def count_users(group):
#   count = 0
#   for member in get_members(group):
#     if is_group(member):
#       count += count_users(member)
#     else:
#       count += 1
#   return count

# print(count_users("sales")) # Should be 3
# print(count_users("engineering")) # Should be 8
# print(count_users("everyone")) # Should be 18
# ### fix ####
# def count_users(group):
#   count = 0
#   for member in get_members(group):
#     if is_group(member):
#       count += count_users(member)
#     else:
#       count +=1
#   return count


# print(count_users("sales")) # Should be 3
# print(count_users("engineering")) # Should be 8
# print(count_users("everyone")) # Should be 18
'''
####begining sales####
# Rory
# Tony
# Charly
####begining engineering####
development
# Taylor
# Rene
# Alex
testing
# Charlie
# Lio
# Al
# Randall
# Suzanne
####begining everyone####
engineering
development
# Taylor
# Rene
# Alex
testing
# Charlie
# Lio
# Al
# Randall
# Suzanne
engagement
marketing
Kai
Pat
Cal
sales
# Rory
# Tony
# Charly
Sven
Victoria
CEO
CFO
'''
'''
n the while loops practice quiz, you were asked to write a function 
to calculate the sum of all positive numbers between 1 and n. Rewrite 
the function using recursion instead of a while loop. Remember that when n is 
less than 1, the function should return 0 as the answer.
'''
def sum_positive_numbers(n):
    if n < 1:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# Study Guide: Module 3 Graded Quiz
# Module 3 Challenge: Loops
# Fill in the blanks to print the numbers 1 through 7.



