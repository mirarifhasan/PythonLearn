#Printing on console
print("Hi! My name is Ishan")
st = "Python executes program line by line\n"
print(st)

print("line" in st)

print("-" * 35)

#Datatypes
x = 10 #int
print(type(x))
x = 2.5 #float
print(type(x))
x = 'Mir' #str
print(str(type(x)) + '\n')

#Type casting
price = 10 #Consider as integer
rating = 4.9 #Consider as float
print("Products price is " + str(price) + " taka and rating is " + str(rating) + '\n')
#int(x), float(x), str(x)

#String
a = 'Abdullah'
print("Name: " + a)
print("First letter of name: " + a[0])
print("Last letter of name: " + a[-1])
print("0th to 3rd letter of name: " + a[0:3] + '\n')

print(a.find('d')) #Finding location of a specific charecter
#replace()

a = " Hello"
print('After trim: ' + a.strip()) #returns 'Hello'
print('Length of " Hello" is: ' + str(len(a)) + '\n')

#lower(), upper(), repalce(), split() alsosome string functions

#Taking input from user
name = input("Enter your name: ")
print('Hi ' + name)
print()

#Array
arr = ['Ayon', 'Hasan', 'Abir']
print(arr[1]) #Printing the second element of array
#print(arr) use for print full array
arr.append("Kafi") #Insert in array
arr.insert(1, "Arif")

#Sorting
sorted(arr) #sort in alphabetical order

arr.remove('Abir')
arr.pop() #Remove fron last index
#del arr[3] #Delete the full array
#arr.clear() #delete all values of aray

#Multidimentional-Array
arr2 = [['CMath', 'DSD', 'PHP'], ['DEPT', 'Algo', 'Android']]
print(arr2[1][2]) #Android

#if-else
if "Abir" in arr:
  print("\nYes, 'Abir' found by if-else")

a = 10; b = 15
if b > a:
    print("\nb > a, from if statement")
elif a==b:
    print("b = a, from elif statement")
else:
    print('b < a from else statement')

print("A") if a < b else print("B")

#For loop
print()
for x in arr: #increment by 1
    print(x)

print()
for x in range(2, 15, 3): #it will run from a to b and increment by 3
  print(x)

#range(a) means, it will run for 'a' times
#range(a, b) means, it will run from a to b and increment by 1

#While loop
print()
i = 1
while i < 6:
  print(i)
  i += 1

print()
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


#Dictionary
print()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict['model']) #thisdict.get("model") will also gives the same result
thisdict['model'] = 'Alif' #Update the value of model







