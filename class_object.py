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
print('Name: ' + p1.name)
print('Age: ' + str(p1.age) + ' Before')
p1.age = 37
print('Age: ' + str(p1.age) + ' After')
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#self should be the first paremeter of a function


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
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# self should be the first paremeter of a function

del p1.age # Deleting age attribute


# Pass keyword
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


print()
#Inherite
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
x.printname()
print(x.graduationyear)
