##################################################################################
# 1- Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white. 
##################################################################################

# class Vehicle: 
#     color = "white"
    
#     def __init__(self, name, max_speed, mileage): 
#         self.name = name 
#         self.max_speed = max_speed 
#         self.mileage = mileage 

# class Bus(Vehicle): 
#     pass 

# class Car(Vehicle): 
#     pass

##################################################################################
# 2- (Bus child class that inherits from the Vehicle class)
# You need to override the fare() method 
##################################################################################

# class Vehicle: 

#     def __init__(self, name, mileage, capacity): 
#         self.name = name 
#         self.mileage = mileage 
#         self.capacity = capacity
    
#     def fare(self):
#         return self.capacity * 100
        

# class Bus(Vehicle): 
    
#     def __init__(self, name, mileage, capacity): 
#         super().__init__(name, mileage, capacity)

#     def fare(self):
#         base = super().fare()
#         additional = base * 0.10
#         return base + additional

# School_bus = Bus("School Volvo", 12, 50) 
# print("Total Bus fare is:", School_bus.fare()) 

##################################################################################
# 3- Determine if School_bus is also an instance of the Vehicle class
##################################################################################

# class Vehicle: 
#     def __init__(self, name, mileage, capacity): 
#         self.name = name 
#         self.mileage = mileage 
#         self.capacity = capacity 

# class Bus(Vehicle): 
#     pass 

# School_bus = Bus("School Volvo", 12, 50)

# # To check if School_bus is an instance of Vehicle 
# # we use Python’s built-in function isinstance()
# print(isinstance(School_bus, Vehicle))  

##################################################################################
# 4- Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area. 
##################################################################################

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def compute_area(self):
#         area = self.length * self.width
#         return area
        
# #test it:
# new_rectangle = Rectangle(10,20)
# print("Area of out New Rectangle is:", new_rectangle.compute_area())

##################################################################################
# 5- Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case.
##################################################################################

# class HandleString:
#     def __init__(self):
#         self.string_from_console = ""
        
#     def get_string(self):
#         self.string_from_console = input("please enter a string: ")

#     def print_string(self):
#         print(self.string_from_console.upper())

# #test it:
# new_handler = HandleString()
# new_handler.get_string()
# new_handler.print_string()

###################################################################################
# 6-Define a class Person and its two child classes: Male and Female. All classes have a 
# method "getGender" which can print "Male" for Male class and "Female" for Female class.
##################################################################################

# class Person:
#     gender = "not defined yet"

#     @classmethod
#     def get_gender(cls):
#         print(cls.gender)

# class Male(Person):
#     gender = "male"

# class Female(Person):
#     gender = "female"

# #test it
# Male.get_gender()  
# Female.get_gender()  
    
###################################################################################
# 7- Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid 
# but "[)", "({[)]" and "{{{" are invalid
##################################################################################

# class ParenthesesHandler:
#     def is_valid(self, input_string):
#         stack = []
#         mapping = {')': '(', '}': '{', ']': '['}

#         for char in input_string:
#             if char in mapping.values():
#                 #opening bracket
#                 stack.append(char)
#             elif char in mapping:
#                 #closing bracket
#                 if not stack or stack[-1] != mapping[char]:
#                     return False
#                 stack.pop()
#             else:
#                 # Invalid input
#                 return False

#         return len(stack) == 0

# #test it:
# new_instance = ParenthesesHandler()

# print(new_instance.is_valid("()"))         
# print(new_instance.is_valid("()[]{}"))     
# print(new_instance.is_valid("[)"))         
# print(new_instance.is_valid("({[)]"))      
# print(new_instance.is_valid("{{{"))        