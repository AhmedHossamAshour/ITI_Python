##################################################################################
# 1- Given a list of numbers, create a function that returns a list where all similar adjacent  
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3] 
# Note:  You may create a new list or modify the passed in list. 
##################################################################################

# given_list = [1,2,3,3]
# def my_function(my_list):
#     my_set = set(my_list)
#     return list(my_set)
# print(my_function(given_list))

##################################################################################
# 2- Consider dividing a string into two halves  
# Case1:  The length is even, the front and back halves are the same length. 
# Case2:  The length is odd, we’ll say that the extra char goes in the front half. 
# E.g. ‘abced’, the front half is ‘abc’, the back half’de. 
# Given 2 strings, a and b, return a string of the form: 
# (a-front + b-front) + (a-back +b-back) 
##################################################################################

# def divide_string(inp_str):
#     if len(inp_str) % 2 == 0:
#         # even
#         return inp_str[:len(inp_str) // 2], inp_str[len(inp_str) // 2:]   # use // integer division.
#     else:
#         # odd 
#         return inp_str[:len(inp_str) // 2 + 1], inp_str[len(inp_str) // 2 + 1:]
# front, back = divide_string("abcde")
# print("Front: " +  front)  
# print("Back: " + back)    

##################################################################################
# 3- Write a Python function that takes a sequence of numbers and determines  
# whether all the numbers are different from each other. 
# E.X. [1,5,7,9] -> True 
# [2,4,5,5,7,9] -> False 
##################################################################################

# def is_unique_sequence(sequence):
#     len1 = len(sequence)
#     len2 = len(set(sequence))
#     if len1 == len2:
#         return True
#     else:
#         return False
# input_sequence1 = [1,5,7,9]
# input_sequence2 = [2,4,5,5,7,9]
# print(is_unique_sequence(input_sequence1))
# print(is_unique_sequence(input_sequence2))

##################################################################################
# 4- Given unordered list, sort it using algorithm bubble sort 
# (read about  bubble sort and try to implement it) 
##################################################################################

# given_list = [7,5,1,9,4,3,6,8,2]
# def bubble_sort(list1):
#     for i in range (len(list1)):
#         for j in range (len(list1) - i - 1):
#             if (list1[j]>list1[j+1]):
#                 list1[j], list1[j+1] = list1[j+1], list1[j] #swap
#     return list1
# print(bubble_sort(given_list))

##################################################################################
# 5- Gusses game 
# ● Your game generates a random number and gives only 10 tries for the user to 
# guess that number. 
# ● Get a user input and compare it with the random number 
# ● Display a hit message to the user in case the use number is smaller or bigger of 
# the random number 
# ● If the user type number is out of range(100), display a message that is not allowed 
# and don’t count this as try. 
# ● If user type a number that has been entered before, display a hint message and 
# don’t count this as try 
# ● In case the user entered a correct number within the 10 tries, display a 
# congratulations message and let your application guess another random number 
# with the remain number of tries 
# ● If the user finishes all his tries, display a message to ask him if he wants to play 
# again or not.
##################################################################################

# import random
# user_input = []
# my_random = random.randrange(0, 100)
# print(my_random)  # You can remove this after debugging
# right_answer = False  # Initialize outside the loop
# def check_input(trial):
#     global invalid_input
#     try:
#         input_value = int(input("Guess the number: "))
#     except ValueError:
#         print("Invalid input: not a number!")
#         invalid_input = True
#         return None
#     if input_value < 0 or input_value > 100:
#         print("Not allowed input: out of range!")
#         invalid_input = True
#         return None
#     if input_value in user_input:
#         print("You tried this number before!")
#         invalid_input = True
#         return None
#     user_input.insert(trial, input_value)
#     invalid_input = False
#     return input_value

# for trial in range(0, 10):
#     print("Trial number " + str(trial + 1))
#     invalid_input = True
#     guess = None
#     while invalid_input:
#         guess = check_input(trial)
#     if guess == my_random:
#         print("You win!")
#         right_answer = True
#         break
#     else:
#         print("You're wrong!")

# if not right_answer:
#     print("You lost!")
