x=10
try:
  print(x)
except:
  print("An exception occurred")
  
# x=10

# try:
 
#     print(x > 10)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")


# x = 10

# try:
#   print(f'x is {x}')
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")




# try:
#   f = open("./demofile.txt, rt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")
  
  
  
# f = open("demofile.txt", "r")
# print(f.read())

# f = open(r"C:\Users\User\Desktop\python/tboy/myfile.txt", "r")
# print(f.read())


# f = open("./demofile.txt", "r")
# print(f.read(5))

# f = open("./demofile.txt", "r")
# print(f.readline(10))

# f = open("demofile.txt", "r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())


# tunde = open("demofile.txt", "r")
# for x in tunde:
#   print(x[10])


# tunde = open("demofile.txt", "r")
# print(tunde.readline())
# tunde.close()




# opening file  ad writing in a file
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()



# f = open("demofile22.txt", "w")
# f.write("Now the file has more content!")
# f.close()




# f = open("demofile2.txt", "r")
# print(f.read())
# f.close()


# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# f = open("demofile2.txt", "r")
# print(f.read())
# f.close()


# f = open("myfile.txt", "x")

# f = open("myfile2.txt", "w")



# deleting files

# import os
# os.remove("demofile2.txt")



# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")


# import os
# os.rmdir("tboy")



# import os

# try:
#     os.remove("tunde/tb.txt")
#     print("File 'tunde.txt' removed successfully.")
# except OSError as e:
#     print(f"Error: {e.strerror}")