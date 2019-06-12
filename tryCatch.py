# Example-1
# x = 12
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# Example-2
print()
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
# else keyword to define a block of code to be executed if no errors were raised


# Example-3
print()
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
# finally block, if specified, will be executed regardless if the try block raises an error or not


# Example-4
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
