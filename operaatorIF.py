from datetime import date
#10
try:
    
  float(input("Enter the first number: "))


#9
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
try:
  if a == b == c == d:
    print("Its a square!")
  else:
    print("It is something else")
except: 
  print("Something went wrong.")

#8
cart = []
fullprice = 0
milk = 2
bun = 2.5
bread = 3

q1 = input("would you like to buy milk?: ")
if q1 == "yes":
  cart.append(milk)
else:
  print(cart)

q2 = input("would you like to buy bun?: ")
if q2 == "yes":
  cart.append(bun)
else:
  print(cart)

q3 = input("would you like to buy bread?: ")
if q3 == "yes":
  cart.append(bread)
else:
  print(cart)

for item in cart:
  fullprice = fullprice + item

print(fullprice)


#11
bday = date(int(input("year of your birthday: ")),int(input("mounth of your birthday: ")),int(input("day of your birthday: ")))
now = date.today().year #2023
if (now - bday.year) % 10 == 0: #bday>date(2000,1,1,)
  print("anniversary")
else:
  print("-----------")



#7 
average_heights = {'male': 175, 'female': 162}

height = float(input("Enter your height in centimeters: "))
gender = input("Enter your gender (male/female): ").lower
if gender in average_heights:
  if height < average_heights[gender] - 10:
    print("You are short for your gender.")
  elif average_heights[gender] - 10 <= height <= average_heights[gender] + 10:
    print("You have average height for your gender.")
else:
  print("You are tall for your gender.")

#6
try:
  height = float(input("Enter your height: "))
  
  if height > 60 and height < 160:
    p = print("You are soo small!")
  elif height >= 160 and height <= 175:
    p = print("You have a good height")
  elif height >=175 and height <= 210 :
    p = print("You are tall!")
except:
  print("Its impossible!")

#5
temperature = float(input("What is your room temperature?: "))
if temperature < 18:
  print("It is too low!")
elif temperature >= 18 and temperature <= 30:
  print("Its a good temperature!")
else:
  print("Its too much!")
    
#4
a = float(input("Enter the width of the room: "))
b = float(input("Enter the length of the room: "))
s = a * b
renovation = input("Do you need a room renovation?: ")
if renovation == "yes":
  price = float(input("How much does a square meter cost?: "))
  print("The price will be ",s*price)
else:
  print("Okey, bye!")

#3
name = input("name: ")
name2 = input("name 2: ")
announce = print("You are next door neighbors today!")

#1
name = input("Teie eesnimi: ")
if name == "Juku":
  print("We are going to cinema.")
#2
age = int(input("How old are you, Juku?: "))
if age < 0 and age > 100:
  if age < 6:
    print("Ticket is free for you!")
  elif age >= 6 and age <= 14:
    print("For you we have junior ticket!")
  elif age >= 15 and age <= 65:
    print("For you full price applies!")
  else: 
    print("For you we have dicount ticket!")
else:
  print("We dont have any tickets for you, sorry!")



