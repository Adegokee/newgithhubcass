# class MyClass:
#   x = 5
  

# p1 = MyClass()
# print(p1.x)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f'{self.name} {self.age}'

 

# p1 = Person("John", 36)
# print(p1)
# print(p1.name)
# print(p1.age)





# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}{self.age}"

# p1 = Person("John", 36)

# print(p1)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()



# class Person:
#   def __init__(mysillyobje, name, age):
#     mysillyobje.name = name
#     mysillyobje.age = age

#   def myfunc(tun):
#     print("Hello my name is " + tun.name)

# p1 = Person("John", 36)
# p1.myfunc()