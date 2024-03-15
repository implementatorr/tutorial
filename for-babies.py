name = "Bro"
age = 21
attractive = True

name, age, attractive = "Bro", 21, True

print(name)
print(age)
print(attractive)

x = y = e = t = 30
print(x, e, t ,y)

name = "Bro Code"

print(len(name))
print(name.find("B"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count(" "))
print(name.replace("o","b"))
print(name * 3)

x = 1
y = 2.0
z = "3"

print("X is " + str(x*3))
print("Y is " + str(y))
print(str(x) + (z*3))

name = input(str("What is your name?: "))
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age += 1

print("Hello " + name)
print(("You are " + str(age) +" years old"))
print("You are " + str(height) + "cm tall ")

import math

pi = 9.5
x = 1
z = 2
y = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(pi))
print(max(pi, x, z ,y))
print(min(pi, x, z ,y))

name = "Yury Ivashka"

first_name = name[:4]
last_name  = name[5:]
fynky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(fynky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice1 = slice(7,-4)

print(website1[slice1])
print(website2[slice(7, -4)])

my_string = "Slonim"

print("firts letter: " + my_string[0])
print("second letter: " + my_string[5])
print("from second till last: " + my_string[slice(1, None)])

age = int(input("How old are you: "))
if age == 100:
    print("You are a century old!!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!!")
else:
    print("You are a child!")

temp = int(input("What is the temperature outside?: "))
if temp >= 0 and temp <= 30:
    print("The temperature is good today!! ")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!! ")

temp = int(input("What is the temperature outside?: "))
if not temp <= 0 and temp >= 30:
    print("The temperature is good today!! ")
elif not temp > 0 or temp < 30:
    print("The temperature is bad today!! ")

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("Hello " + name)

name = input("Enter your name: ")
while not name.isalpha():
    name = input("Enter your name: ")
print("Hello " + name)

while True:
    name = input("write your name:")
    if name.isalpha():
        break
    else:
       continue

import time
for index in range(50,0,-1):
    print(index)

x = int(input("Input range: "))
y = int(input("Input range: "))
z = int(input("Input range: "))
for seconds in range(x,y,z):
    time.sleep(1)
    print(seconds)

print("Happy New Year!!")

rows = int(input("How many rows?: "))
colums = int(input("How many colums?: "))
symbols = input("Any symbol?: ")

for i in range(rows):
    for j in range(colums):
        print(symbols, end="")
    print()

while True:
    name = input("Enter your name : ")
    if name != "" and name.isalpha() and len(name) > 1:
        print("Hi, ", name.capitalize())
        break

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,9):
    if i == 3:
        pass
    else:
        print(i, end="")

food = ["pizza", "milk", "potato", "hamburgers", "pudding"]
for i in food:
    print(i)

drinks = ["coffe", "s
