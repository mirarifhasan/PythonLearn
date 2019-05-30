#Example_1_ClassObject
class MyClass:
  x = 5

p1 = MyClass() #Creating object
print(p1.x)


print()
#Example_2_ClassObjectConstractor
class Person:
  def __init__(self, name, age): #This is constractor
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)


print()
#Example_3_ClassObjectConstractorMethod
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#self should be the first paremeter of a function




