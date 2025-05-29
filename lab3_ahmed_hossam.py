##################################################################################
# 1-The program takes a command line argument, this argument is the name of a text file. 
# the program reads all the text and split them and calulate the 20 most used workds in the 
# file and then write them to a file called popular_words.txt
##################################################################################

# with open("./mockingjay.txt", 'r', encoding='utf-8') as f:
#     text = f.read().lower()
# #Remove punctuation
# for char in '.,!?;:"()[]{}<>*/\\|\'`~@#$%^&-_+=\n\r':
#     text = text.replace(char, ' ')
# #Split to words
# words = text.split()
# #Count words
# word_counts = {}
# for word in words:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
# #Sort and get top 20
# sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
# top_20 = sorted_words[:20]
# #Write to file
# with open('popular_words.txt', 'w', encoding='utf-8') as out_file:
#     for word, count in top_20:
#         out_file.write(f"{word}: {count}\n")
# print("Top 20 words written to popular_words.txt")

##################################################################################
# 2-Given two points represented as x1, y1, x2, y2, r the (float)return (float) distance 
# between them considering the following distance equation. 
##################################################################################

# def distance(x1: float, y1: float, x2: float, y2: float) -> float:
#     return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
# d = distance(1, 0, 4, 4)
# print(d)  

##################################################################################
# 3-Create a Vehicle class without any variables and methods 
##################################################################################

# class Vehicle:
#     def __init__(self):
#         pass

##################################################################################
# 4-Create a Vehicle class with max_speed and mileage instance attributes
##################################################################################

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

##################################################################################
# 5-Write a Python program to reverse a string word by word
##################################################################################

# def reverse_fn(a_string):
#     words_list = a_string.split()           
#     reversed_words = words_list[::-1]       
#     return ' '.join(reversed_words)    

# input = "my name is ahmed hossam"
# reversed_str = reverse_fn(input)
# print(reversed_str)

##################################################################################
# 6-Write a Python class which has two methods get_String and print_String. get_String 
# accept a string from the user and print_String print the string in upper case.
##################################################################################

# class Taxt_editor:
#     def __init__(self):
#         self.text = ""
#     def get_String(self):
#         self.text = input("enter string: ")
#     def print_String(self):
#         print(self.text.upper())

##################################################################################
# 7-Write a Python class named Circle constructed by a radius and two methods which will 
# compute the area and the perimeter of a circle.
##################################################################################

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def get_perimeter(self):
#         return 2*(3.14)*self.radius
    
#     def get_area(self):
#         return (3.14)*(self.radius**2)

##################################################################################