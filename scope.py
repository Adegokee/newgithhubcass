# y=900
# def myfunc():
#     global y
#     x = 300
#     print(x + y)
# myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()