'''This script is for python newbies'''
#If you want to download and install python, visit this website: www.python.org
#Printing hello world
print('Hello world') #In python3 print is always a function...in python2, he is a statement

'''
Python language Primitives

-Variables
##The following are python built-in data types:
-Numbers
-Strings
-Lists
-Tuples
-Dictionary
-Sets
##Each of them can be manipulated using:
-operators
-functions
-Data-type methods
'''
#Numbers in python(Integers,Floats,Booleans,Complex_Numbers)
#Integers are whole numbers
num1 = 10
num2 = -50
num3 = num1 * num2 #Perfoming operations on Integers
print(num3)
num10 = num1 + num2
print(num10)
num11 = num1 // num2
print(num11)
num12 = num1 % num2
print(num12)
#Floats are decimal numbers
num4 = 5.9
num5 = -800.2
num6 = num4 + num5
print(num6) 
num7 = num4 - num5 
print(num7)
num8 = num4 * num5 
print(num8)
num9 = num4 / num5 
print(num9)
#Booleans return either true of false...they can at best be used with comparisons
number1 = 10
number2 = 25

print(number1 < number2)
print(number1 != number2)
print(number1 == number2)

#You can also convert Integers to floats and vice versa
print(int(9.8))
print(float(5))


#Lists in python
names = ['titus', 'jack', 'john', 'jane']
print(names)
print(len(names))
fruits = list()
fruits.append('banana')
print(fruits)

#Tuple in python
archive = ('data', 'people', 'structures')
print(archive)
print(type(archive))
a,b,c = ('one','two','three')
print(a,b,c)

#Dictionary in python
