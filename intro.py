import tkinter

# print('Hello world')

#single
# x = 5
# y= "John Smith"
# print(y)

#multiple variables
# x, y, z = 'orange', "banana", 'grape'
# print(x)

# _name= "John"
# print(_name)

# First_name
# first-name=

# outputing variables
# x=5
# y=10
# print(x + 5)
# concatination joining two variables together
# first_name='John'
# last_name="Smith"

# print( "My name is "+ ' ' +first_name + '' + last_name)
# print(f' my name is {first_name} {last_name}')
# print(full_name)

# global variables
# x = "awesome"

# def my_pytho():
#     # x = "Welcome"
#     print('Python is ' + x)
# my_pytho()


# dataTypes
# x = {'orange', 'banana'}
# x = range(10)
# x = None
# print(type(x))

# numbers dataTypes

# x=6
# print(x)
# float datatypes
# x = 1.5
# print(type(x))

# casting
# x = str('1.5')
# print(type(x))
# x = int('srrr1')
# print(type(x))

# x = " Hello, world! "
# print(x[0:7:2])
# print(x[-2::-5])
# print(x.upper())
# print(x.lower())
# print(x.strip())
# print(x.replace('H', 'J'))
# u=['Welcome', "Canada"]
# new_x=x.split()
# new_x.append(u)
# # new_x.reverse()
# print(new_x)
# age=10
# txt = "My name is John, and I am {} years old"
# print(txt.format(age))

# quantity=3
# laptop= "Dell"
# price=500000

# my_favourie="I want {}  {} laptops wihich is not more than {}k "
# print(my_favourie.format(quantity, laptop, price))

# first_name=input('Enter first name   \n')
# last_name= input('Enter last name \n')

# print(f'My name is {first_name} and {last_name}')

# first_number = int(input('Enter first number    \n'))
# last_number= int(input('Enter last name \n'))
# print(first_number + last_number)


# print(10 == 30)

# a=70
# b=50
# x='john'
# print(bool(b))

# if a > b:
#     print("A is the greater number")
# else:
#     print("B is the greater number")

# OPERTATORS
# arithmetic operators +, -, /, *, %, **, //
# num1 = 30
# num2 =10

# print(num1 + num2)
# print(num1 - num2)
# print(num1 / num2)
# print(num1 * num2)
# print(num1 ** num2)
# print(num1 // num2)


#assignment operators =, +=, -=, *=, /=, %=, **
# print(num1 != num2)
# print(num1 += num2)
# print(num1 / num2)
# print(num1 * num2)
# print(num1 ** num2)
# print(num1 // num2)
#comparsion operators ==, !=, >, <, >=, <=,

# print(num1 == num2)
# print(num1 >= num2)
# print(num1 * num2)
# print(num1 ** num2)
# print(num1 // num2)


# logical operators and, or, not 
# age=18
# country= "Nigeria"

# if age == 18 or country == "Nigeria":
#     print('you can vote')
# else:
#     print('you cannot vote')

# x= False
# if not x:
#     print('you cannot vote')
# else:
#     print('you can vote')
   
#list
# mycolor=['yellow', 'green', 'brown', 'blue', 'purple', 'orange']
# y=0
# newcolor=['red', 'orange']
# mycolor.extend(newcolor)
# nextcolor=[]
# mycolor.reverse()
# mycolor.append('black')
# mycolor[1:3]=['tunde', 'apple']
# del mycolor[0]
# mycolor.insert(0, 'black')
# mycolor.sort()
# print(mycolor)

# for i in mycolor:
#     print(i)

# for i in range(len(mycolor)):
#     print(mycolor[4])
    
# while y < len(mycolor):
#     print(mycolor[y])
#     y= y + 1


# [print(x) for x in mycolor]
# mycolor[0]='red'
# nextcolor.append(mycolor)
# print(nextcolor)
# print(mycolor)
# for i in mycolor:
#     if i[1] == 'r':
#         print(i)

# mycolor=['yellow', 'green', 'zig', 'brown', 'blue', 'purple', 'orange']
# newcolor=[x for x in mycolor if 'a' in x]
# newcolor=[x for x in range(10) if x < 5]
# print(newcolor)
# num=range(1, 10)
# product=0
# for i in num:
#     product= product + 1
#     if product > 5:
#         print(product)
# newcolor= [i.upper() for i in mycolor]
# print(newcolor)
# print(num)
# mycolor.sort(reverse = True)
# print(mycolor)

# tunde=mycolor.copy()
# tunde= list(mycolor)
# print(tunde)
# for x in mycolor:
#     if 'y' in x:
#         newcolor.append(x)
# print(newcolor)

# nubers= [10, 20, 40]
# alpha= ['a', 'b', 'c', 'd', 'e', 'f']

# list3= nubers + alpha
# print(list3)

# for x in nubers:
#     alpha.append(x)
# print(alpha)

# nubers.append(alpha)
# print(nubers)


#Tuples

# mycolor=('yellow', 'green', 'zig', 'brown')
# newcolor=('red', 'black')

# new = mycolor+ newcolor
# print(new)
# tunde = mycolor * 2
# print(tunde)
# for i in mycolor:
#     print(i)


# for i in range(len(mycolor)):
#     print(mycolor[i])
# y = list(mycolor)
# y=list(mycolor)
# y.append("orange")
# tunde=tuple(y)
# print(tunde)
# mycolor=tuple(y)
# print(mycolor)
# print(mycolor)
# y[1]='tunde'
# tobi=tuple(y)
# print(tobi)
# y=('orange', )
# mycolor += y
# print(mycolor)

# score= {20, 30, 25, 20, 50, 55, 50, 70, 90, 70}
# mycolor={'yellow', 'green', 'zig', 'brown'}
# mycolor=['yellow', 'green', 'zig', 'brown']

# for i in score:
#     print(i)
# print(20 in score)
# print(len(score))
# score.add("orange")
# score.update(mycolor)
# score.remove('zig')
# score.discard('green')
# # score.clear()
# del score
# print(score)


# students = {
#     "name": 'Shade',
#     "locaton": 'Ikeja',
#     "status": "single",
#     "Year": "2015",
    
# }
# # students["Year"]=2018
# students["email"]='shade@yahoo.com'
# students.update({"stata": 'lagos'})
# students.pop("email")
# students.popitem()
# # x = students.get("name")
# x = students.values()
# for i in students:
#     print(students[i])

# newStudent=students.copy()   
# print(newStudent)

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily["child2"]["name"])




# my_list = [1, 2, 3]
# my_list.extend([4, 5])
# print(my_list)  # Output: [1, 2, 3, 4, 5]

# my_list.extend([6, 7])
# print(my_list) 






# num1=10
# num2=30
# if num1 > num2:
#   print('Num1 is greater')
# else:
#   print('Num2 is greater')

# name="John Smith"
# print(name.upper())

# score=input("Enter a score   \n")
# score=score.upper()
# if score == 'A':
#   print('Excellent')
# elif score == 'B':
#   print('Second Position')
# elif score == 'C':
#   print('Third Position')
# elif score == 'D':
#   print('Fourth Position')
# elif score == 'E':
#   print('Fail')
# else: 
#   print('Invalid Score')  


# while loop
# num=0
# product=5
# while num <= 10:
#   # print(num)
#   num+=1
#   if num % 2==0:
#     print(num)

# fruits= ["apple", "banana", "training", "orange", "tech"]
# index=0

# while index < len(fruits):
#   # if fruits[index].startswith("t") or fruits[index].startswith("T"):
#   print(fruits[index])
#   index += 1
#   print(index)
# password = input("Enter the password: ")

# while password != "python123":
#     print("Incorrect password. Try again.")
#     password = input("Enter the password: ")

# print("Access granted!")


# for i in fruits:
#   if i[0] == 't':
#     print(i)


# num=range(0, 11)
# product=4
# for i in range(0, 11):
#   # if i % 2 == 0:
#   product * i
#   print(f'{product} * {i} = {product * i}')

# def my_name():
#   print("John Smith")

# my_name()

# def last_name(name, day):
#   print(name+ ' ' +day)
# last_name('John Smith', 'Good Morning')


# lambda

# x = 5
# y = lambda x: x + 10
# print(y)

# x=lambda a: a + 10
# print(x(2))

# together= lambda x, y: x + y
# print(together(20,30))

# num=[10, 50, 25, 43, 20, 11, 15, 13]
# mynum = lambda num: num % 2 == 0
# print(mynum)
# for i in num:  
#   if i % 2== 0:
#     print(i)

# print(list(filter(lambda x: x % 2 == 0, num)))
# print(list(map(lambda x: x + x, num)))
# print(max(num))
# print(min(num))
# print(sum(num))

# import random
# num= random.randint(0, 3)
# # print(num)
# guess = int(input('Enter a number   \n'))
# if guess == num:
#   print('You are correct')
# elif guess > num:
#   print("Your guess is low")
  
# else:
#   print("Your guess is high")
# print(guess)


# even = lambda num: num % 2 == 0
# print(even(num))

# print(list(num(num % 2 == 0)))
  


 
# for i in range(1,21,3):
#   print(i)
#   # if i % 2 == 0:
  #   print('Even Number')
  # elif i % 3 == 0:
  #   print("Divisible by 3")
  # elif i % 5 == 0:
  #   print("Divisible by 5")
  # else:
  #   print(i)
  
  
# for i in range(4):
#     for j in range(5):
#         print(f"i: {i}, j: {j}")

#tkinter  intoduction displaying hell world-----
from tkinter import *
# root = Tk()
# #creating the label widget
# mylabel = Label(root, text="Hello world!")
# #showing it on he screen
# mylabel.pack()
# root.mainloop()

# grid system in tkinter for positioning----
root = Tk()
# creating the label widget
mylabel1 = Label(root, text="Hello world!")
mylabel2 = Label(root, text="My name is Adegoke")
mylabel3 = Label(root, text="My country is United States") 
# showing it on he screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=0, column=2)
mylabel3.grid(row=0, column=3)
root.mainloop()
#or---
# root = Tk()
# #creating the label widget
# mylabel1 = Label(root, text="Hello world!").grid(row=0, column=0)
# mylabel2 = Label(root, text="My name is Adegoke").grid(row=1, column=3)
# mylabel3 = Label(root, text="My country is United States").grid(row=1, column=2)
# root.mainloop()


# creating a button in tkinter -----
# root=Tk()

# def my_click():
#   my_label =Label(root, text="Look! I clicked this button")
#   my_label.pack()

# mybutton = Button(root, text="Click Me", command=my_click, fg="blue", bg="green")
# # mybutton = Button(root, text="click me", state=DISABLED, padx=50, pady=50, )

# mybutton.pack()
# root.mainloop()

# my_string = "123456 welcome to digital fortress in akowonjo branches"
# print(my_string[10])




# creating input field with tkinter-------------
# root=Tk()

# my_input = Entry(root, width=50, bg="blue", borderwidth=5)
# my_input.insert(0, "enter your name")
# my_input.pack() 
# def my_click():
#   hello = "Hello " + my_input.get()
# #   # my_label =Label(root, text="Hello "+ " " +my_input.get())
#   my_label =Label(root, text=hello)
#   my_label.pack()
  
# mybutton = Button(root, text="Enter your stock Quote", command=my_click, fg="blue", bg="green")
# mybutton.pack()
# root.mainloop()




# build a calculator with tkinter
# root= Tk()
# root.title("Simple Calculator")
# v= Entry(root, width=35, borderwidth=5)
# v.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# def button_click(number):

#     current= v.get()
#     v.delete(0, END)
#     v.insert(0, str(current) + str(number))
  
# def  button_clear():
#     v.delete(0, END)
    
# def button_plus():
#     first_number = v.get()
#     global f_num
#     global math 
#     math = "addition"
#     f_num=int(first_number)
#     v.delete(0, END)
    
# def button_equal():
#     second_number = v.get()
#     v.delete(0, END)
#     if math == "addition":
#         v.insert(0, f_num + int(second_number))
#     if math == "subtraction":
#         v.insert(0, f_num - int(second_number))
#     if math == "multiplication":
#         v.insert(0, f_num * int(second_number))
#     if math == "division":
#         v.insert(0, f_num / int(second_number))
       
    


# def button_sub():
#     first_number = v.get()
#     global f_num
#     global math 
#     math = "subtraction"
#     f_num=int(first_number)
#     v.delete(0, END)
    
# def button_multi():
#     first_number = v.get()
#     global f_num
#     global math 
#     math = "multiplication"
#     f_num=int(first_number)
#     v.delete(0, END)

# def button_div():
#     first_number = v.get()
#     global f_num
#     global math 
#     math = "division"
#     f_num=int(first_number)
#     v.delete(0, END)
    
# button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
# button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
# button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
# button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
# button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
# button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
# button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))

# button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
# button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
# button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
# button_add = Button(root, text="+", padx=39, pady=20, command=button_plus)
# button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
# button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
# button_subtract = Button(root, text="-", padx=41, pady=20, command=button_sub)
# button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multi)
# button_divide = Button(root, text="/", padx=40, pady=20, command=button_div)

# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)

# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)

# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)

# button_0.grid(row=4, column=0)
# button_add.grid(row=5, column=0)
# button_clear.grid(row=4, column=1,  columnspan=2)
# button_equal.grid(row=5, column=1, columnspan=2)
# button_subtract.grid(row=6, column=0)
# button_multiply.grid(row=6, column=1)
# button_divide.grid(row=6, column=2)

# # put button on screen
# root.mainloop()


# Using Images, and Exit Buttons
# from PIL import ImageTk, Image 
# pip install pillow
# root = Tk()
# root.title("Learn Tkinter") 
# button_quit = Button(root, text="Exit Program", command=root.quit)
# button_quit.pack()

# myimg1=ImageTk.PhotoImage(Image.open("fb2.png"))
# myimg2=ImageTk.PhotoImage(Image.open("fb2.png"))
# myimg3=ImageTk.PhotoImage(Image.open("fb2.png"))
# myimg4=ImageTk.PhotoImage(Image.open("fb2.png"))
# myimg5=ImageTk.PhotoImage(Image.open("fb2.png"))

# image_list= [myimg1, myimg2, myimg3, myimg4, myimg5]


# my_label = Label(image=myimg1)
# # my_label.pack()
# my_label.grid(row=0 ,column=0, columnspan=3)
# def foward(image_number):
#   global my_label
#   global button_back
#   global button_forward
  
#   my_label.grid_forget()
#   my_label = Label(image=image_list[image_number-1])
#   button_forward = Button(root, text='>>', command=lambda: foward(image_number + 1))
#   button_back = Button(root, text='<<', command=lambda: back(image_number - 1))
#   my_label.grid(row=0 ,column=0, columnspan=3)
#   button_back.grid(row=1 ,column=0)
#   button_forward.grid(row=1, column=2)
  
#   if image_number == 5:
#     button_forward == Button(root, text=">>", state=DISABLED)
  
  
  
# def back(image_number):
#   global my_label
#   global button_back
#   global button_forward
#   my_label.grid_forget()
#   my_label = Label(image=image_list[image_number-1])
#   button_forward = Button(root, text='>>', command=lambda: foward(image_number + 1))
#   button_back = Button(root, text='<<', command=lambda: back(image_number - 1))
  
#   if image_number == 1:
#     button_back=Button(root, text='>>', state=DISABLED)
#   my_label.grid(row=0 ,column=0, columnspan=3)
#   button_back.grid(row=1 ,column=0)
#   button_forward.grid(row=1, column=2)

# button_back = Button(root, text="<<" ,command=back)
# button_exit = Button(root, text="Exit program", command=root.quit)
# button_forward = Button(root, text=">>", command=lambda: foward(1))

# button_back.grid(row=1 ,column=0)
# button_exit.grid(row=1 ,column=1)
# button_forward.grid(row=1, column=2)

# root.mainloop()


# root = Tk()
# root.title("Learn Tkinter")

# # Replace 'Desktop/python/hero-banner.png' with the correct path to your icon file
# root.iconbitmap(r'Desktop/python/hero-banner.png')

# root.mainloop()














# duplex=1000000
# print(f'The price of the house is {duplex}')
# house_price=int(input("How much is your budget for the house? \n"))
# percent_rate=int(house_price / duplex * 100)

# print(percent_rate)
# if house_price < 500000 or house_price > 300000:
#   print(f" your advance payment is {house_price} which is just {percent_rate} % ")
# elif house_price > 500000:
#   print(f" your {house_price} is just {percent_rate} % ")
  
  
  
# create a programe that takes in different route if a conductor of a buss call Egbeda Igando Iyanaiba. if Egbeda is 200, igando, 300, iyanaba 500 caculate the change of a passanger will get for each of the donmination of money given to a conductor
# place=input("Enter your destination   \n").lower()
# payment=int(input('Enter your payment  \n'))
# place_1="Egbeda"
# place_2="Igando"
# place_3="Iyanaba"

# mony_1=100
# money2= 200
# money3=500
# money4 = 1000

# if place == place_1 or payment == mony_1:
#   print("The amount you have doesnot take you to your destination")
# elif place == place_2 and payment == money2:
#   print()


# y=3
# x = 0
# while x <= 10:
#   print(f'{y} x {x} = {y * x}')
#   x+=1

# import tkinter as tk

# def button_click(symbol):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(0, current + str(symbol))

# def clear_entry():
#     entry.delete(0, tk.END)

# def calculate_result():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(0, str(result))
#     except Exception as e:
#         entry.delete(0, tk.END)
#         entry.insert(0, "Error")

# # Create the main window
# window = tk.Tk()
# window.title("Simple Calculator")

# # Entry widget for input and display
# entry = tk.Entry(window, width=20, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
# entry.grid(row=0, column=0, columnspan=4)

# # Buttons
# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
# ]

# for (text, row, col) in buttons:
#     if text == 'C':
#         btn = tk.Button(window, text=text, width=5, height=2, command=clear_entry)
#     elif text == '=':
#         btn = tk.Button(window, text=text, width=5, height=2, command=calculate_result)
#     else:
#         btn = tk.Button(window, text=text, width=5, height=2, command=lambda s=text: button_click(s))

#     btn.grid(row=row, column=col)

# # Run the Tkinter event loop
# window.mainloop()




# If you're looking to create a guessing game in Python using the sys module for system-related functionality, you can utilize it for exiting the program. Here's a simple implementation:

# python
# Copy code
import random
import sys

# def guessing_game():
#     print("Welcome to the Guessing Game!")
#     print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
# secret_number = random.randint(1, 100)
# attempts = 0
     
# while True:
#         guess = input("Enter your guess (or 'quit' to exit): ")
        
#         if guess.lower() == 'quit':
#             print("Goodbye!")
#             sys.exit()  # Exiting the program gracefully
        
#         if not guess.isdigit():
#             print("Please enter a valid number.")
#             continue
        
#         guess = int(guess)
#         attempts += 1
        
#         if guess < secret_number:
#             print("Too low! Try again.")
#         elif guess > secret_number:
#             print("Too high! Try again.")
#         else:
#             print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
#             sys.exit()  # Exiting the program gracefully

# # guessing_game()


# size = 10

# # Nested loop to generate the multiplication table
# for i in range(1, size+1):
#     for j in range(1, size+1):
#         # Calculate the product
#         product = i * j
#         # Print the product with formatting
#         # Using end='\t' to separate columns with tabs
#         print(f"{product:4}", end='\t')
#     # Move to the next line after each row
#     print()



# main_string = "Hello, World!"

# Find the index of the substring "World"
# start_index = main_string.find("World")

# Extract the substring "World"
# substring = main_string[start_index:start_index + len("World")]

# Print the extracted substring
# print(substring)


# mynname = input("Please enter your name")




# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x: 
#     newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]
# print(newlist)