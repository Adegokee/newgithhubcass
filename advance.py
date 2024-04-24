from PyQt5.QtWidgets import *
# OOP - Object oriented programming language
# everything is an object
#Object has a properties and sometimes a method
# A class is a template that defines an objects

# class Building_Plan:
#     def __init__(self, name, rooms, color):
#         self.name = name
#         self.rooms = rooms
#         self.color = color
    
#     def __str__(self):
#         return f' The building is {self.name} which has {self.rooms} rooms and painted with {self.color} color'
    
#     def intro(self):
#         return f'The house is called {self.name}'

#     def type(self):
#         return f' there are {self.rooms} rooms'
    

# house1= Building_Plan('Bungalow', 4, 'purple')
# print(house1)
# print(house1.intro())
# print(house1.type())
# house2= Building_Plan('Duplex', 10, 'green')
# print(house2)
# print(house2.intro())
#print(house2.type())
# ---------------------------------------
# class Dog:
#     def __init__(self, name, age):
#        self.name = name
#        self.age = age
       
#     def __str__(self):
#         return f'{self.name} {self.age}'
    
#     def mention_name(self):
#         print(f'My name is {self.name}')
    
#     def mention_age(self):
#         print(f'My age is {self.age}')
        
        
    

# my_dog= Dog('Puppy', 10)
# print(my_dog)
# my_dog.mention_name()
# my_dog.mention_age()

#----------------------------------


# class Resturants():
    
#     def __init__(self, resturant_name, cusine_type):
#         self.resturant_name = resturant_name
#         self.cusine_type = cusine_type
        
#     def __str__(self):
#         return f'{self.resturant_name}, {self.cusine_type}'
#     def name_of_resturant(self):
#         print(f'The Resturant {self.resturant_name} is open ')
    
# restuarant= Resturants("Mr Biggs", "Fast Food")
# print(f'Restuarant Name: {restuarant.resturant_name}' ) 
# restuarant.name_of_resturant()  
# -----------------------------------


#inheritance
# class Person:
#     def __init__(self, name, age):
#         self.name= name
#         self.age= age
    
#     def __str__(self):
#         return f'My name is {self.name} and my age is {self.age} years'
    
    
# class Employee(Person):
#     def __init__(self, name, age, job_title, gender):
#         super().__init__(name, age)
#         self.job_title = job_title
#         self.gender = gender
#     def __str__(self):
#         return f'My name is {self.name} and my age is {self.age} years, and my job title is {self.job_title} and my gender is {self.gender}'
    
# Employee1= Employee('Adegoke', 25, 'full stack developer', 'male')
# print(Employee1)
# Person1=Person('Naski', 12)
# print(Person1)


# class Computer:
#     def __init__(self):
#         self.__maxprice=900
#     def sell(self):
#         return f'Selling price is {self.__maxprice}'
#     def setMaxPrice(self,price):
#         self.__maxprice=price
# dell=Computer()
# dell.maxprice=500
# print(dell.sell())

# dell.setMaxPrice(1500)
# print(dell.sell())


# Polymorphysm when a function can operate in more than one form

# class Nigeria():
#     def capital(self):
#         return("Abuja is the capital city of Nigeria")
    
#     def currency(self):
#         return("Naira and Kobo is the currency spent in Nigeria")

# class Ghana():
#     def capital(self):
#         return("Accra is the capital city of Ghana")
    
#     def currency(self):
#         return("Cedi and Peswes is the currency spent in Ghana")
    
# def poly__func(x):
#     return(x.capital(), x.currency())
# user1= Nigeria()
# user2= Ghana()

# print(poly__func(user1))
# print(poly__func(user2))


# abstract class and interfaces




