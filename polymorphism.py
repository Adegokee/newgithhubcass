# class Car:
    
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Drive!")
#     def tunde(self):
#         print(f'{self.brand} {self.model}')
    

# class Boat:
    
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Sail!")
#     def tunde(self):
#         print(f'{self.brand} {self.model}')

# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Fly!")
#     def tunde(self):
#         print(f'{self.brand} {self.model}')

# car1 = Car("Ford", "Mustang") 
# print(car1.tunde())#Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# print(boat1.tunde())
# plane1 = Plane("Boeing", "747") #Create a Plane class
# print(plane1.tunde())

# for x in (car1, boat1, plane1):
#   x.move()




class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):

    print(x.brand)
    print(x.model)
    print(f'{x.brand} {x.model}')
    x.move()