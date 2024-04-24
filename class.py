# class MyClass:
#   x = 5
  
# p1 = MyClass()
# print(p1.x)






# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)








# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)






# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()







# inheritance
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:
# x = Person("John", "Doe")
# x.printname()


# class Student(Person):
#     def __init__(self, fname, lname, graduationyear):
#         super().__init__(fname, lname)
#         self.graduationyear = graduationyear

#     def printname(self):
#         print(self.firstname, self.lastname, self.graduationyear)

# t = Student("Titi", "Adegoke", 2019)
# t.printname()

# tunde = "1234adegoke"  # assigning a string representation of an integer
# mytunde = int(tunde)
# print(mytunde)



# Write a Python function to check if a number is even or odd.
# Create a function that takes two numbers as arguments and returns their sum.
# Write a function that takes a list of numbers and returns the maximum value in the list.
# Implement a function that calculates the factorial of a given number.
# Write a Python function to check if a given string is a palindrome.
# Create a function to generate the Fibonacci sequence up to a specified number of terms.
# Implement a function that takes a list of integers and returns a new list with only the unique elements.
# Write a function to check if a given year is a leap year.
# Create a function that takes a string as input and returns the number of vowels in the string.
# Implement a function that takes a list of words and returns the longest word in the list.

# def tunde():
#     num=int(input("Enter a number   \n"))
#     num2=int(input("Enter a number  \n"))
#     return num + num2
# print(tunde())


# def tunde():
#     num=input("Enter a number")
#     return len(num)
# print(tunde())

# def is_prime(number):
#     if number <= 1:
#         return False
#     elif number <= 3:
#         return True
#     elif number % 2 == 0 or number % 3 == 0:
#         return False
#     i = 2
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 1
#     return True


# number = int(input("Enter your number: "))  
# print(is_prime(number))  
# text=[10, 20, 30, 8, 12, 16, 32]
# def myplus():
#     num1 = int(input("Enter your first score number: "))
#     num2 = int(input("Enter your second score number: "))
#     num3 = int(input("Enter your third score number: "))
#     num4 = int(input("Enter your fourth score number: "))
#     num5 = int(input("Enter your fifth score number: "))
#     num6 = int(input("Enter your sixth score number: "))
    
#     tunde = []
#     tunde.extend([num1, num2, num3, num4, num5, num6])  # Appending all numbers to the list
    
#     for i in tunde:
#         if i % 2 == 0:
#             return i
#         else:
#            return ""

# print(myplus())

            
# def factorial(n):
#     # Base case: factorial of 0 is 1
#     if n == 0:
#         return 1
#     # Recursive case: factorial of n is n multiplied by factorial of (n-1)
#     else:
#         return n * factorial(n - 1)

# # Example usage:
# number = int(input("Enter a number to calculate its factorial: "))
# print("Factorial of", number, "is", factorial(number))



# def is_palindrome(s):
#     # Convert the string to lowercase and remove non-alphanumeric characters
#     s = ''.join(x.lower() for x in s if x.isalnum())
    
#     # Check if the string is equal to its reverse
#     return s == s[::-1]

# # Test the function
# print(is_palindrome("A man, a plan, a canal, Panama!"))  # True
# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))  # False





# def filter_strings(strings):
 #     # Use list comprehension to filter strings with more than five characters
#     filtered_strings = [s for s in strings if len(s) > 5]
#     return filtered_strings 

# # Test the function
# input_strings = ["apple", "banana", "orange", "grape", "kiwi", "pineapple"]
# print(filter_strings(input_strings))


mynum=[20, 30,25, 40, 50, 60, 90]
print(list(filter(lambda x: x % 2 == 0, mynum)))
print(list(map(lambda x: x * x, mynum)))


# def tunde():
#     mynum=[20, 30, 40, 50, 60, 90]
#     return max(mynum)
# print(tunde())
 
# tunde = "123"
# print(tunde.isalnum())

# 1. Write a Python program that prompts the user for their name and then prints a greeting message with their name.
# 2. Create a program that takes two numbers as input from the user and then prints their sum.
#3. Write a Python program that asks the user for their first name, last name, and age, then prints a message greeting them by their full name and stating their age.
# 4. Create a script that prompts the user to enter the name of their favorite color and their favorite animal, then prints a message combining the two preferences.
# 5. Implement a program that takes a user's first name and their birth year as input and prints a message with their name and their age calculated from the current year.
# 6. Write a Python script that asks the user for their hometown and favorite food, then prints a message with both pieces of information.
# Develop a program that prompts the user to enter the title and author of a book they recently read, then prints a message combining both pieces of information.
# 7. Create a Python script that asks the user for the name of a city they visited and the year they visited it, then prints a message with both pieces of information.
# 8. Implement a program that takes the user's favorite movie and the year it was released as input and prints a message combining both pieces of information.
# 9. Write a script that prompts the user to enter their favorite fruit and the number of times they eat it per week, then prints a message with both pieces of information.
# 10. Develop a program that asks the user for their favorite subject in school and their grade level, then prints a message combining both pieces of information.
# 11. Create a Python script that prompts the user to enter their favorite sport and the season in which they play it, then prints a message with both pieces of information.