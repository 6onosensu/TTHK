import math

print("Welcome!".center(50))

school = input("Input your school, please: ").capitalize() 
year = int(input("\tWhat is your year of study?: "))

print("Welcome to " + school.upper() + "\nHave a good " + str(year) + " year of study!")

print("Welcome to ",school.lower(),"\nHave a good ",year,"year of study!")

print("Welcome to {0}!\nHave a good {1} year of study!".format(school, year)) 

#It's a comment

print(type(school))

print(type(year))

a = float(input("a: "))
b = float(input("b: "))

# % - remainder; // - a integer number

print(a+b,a-b,a*b,a/b,a**b,a%b,a//b)
print("{0} + {1} = {2}".format(a,b,a+b))

tehe = input("Mida teha: ")
v = eval(str(a)+tehe+str(b))
print(v)

#First task
helloWorld = "Hello World!"
name = input("Input your name: ").capitalize()
age = int(input("Input your age: "))
print(helloWorld,name,"greets! I am ",age,"years old.")

#Second task
age = 18
name = "Jaak"
length = 16.5
doesHeGoToSchool = True
print(type(age))
print(type(name))
print(type(length))
print(type(doesHeGoToSchool))

#Third task
candiesOnTable = int(input("Quantity of candies on the table: "))
print("There are ",candiesOnTable, " candies on the table.")
candiesToRemove = int(input("How many candies should be removed from the table?: "))
remainderOfCandies = candiesOnTable - candiesToRemove
print("There are ",remainderOfCandies," candies left.")

#fourth task
circumferenceOfTheTree = float(input("Circumference of the tree: "))
d = circumferenceOfTheTree/math.pi
print("Tree diameter is ", d)

#Fifth task
n = float(input("n (meters): "))
m = float(input("m (meters): "))
d = math.sqrt(n**2 + m**2)
print("The diagonal of a rectangilar piece of land is ", d ,"m")

#Sixth task
try:
  aeg = float(input("mitu tundi kulus soiduks? "))
  teepikkus = float(input("mitu kilomeetrit soitsid? "))
  kiirus = round(teepikkus / aeg,2)
  print("sinu kiirus oli " + str(kiirus) + " km/h")
except :
  print("Andmetuubi viga!")


#seventh task
inputNumbers = input("Input the numbers using space button: ")
listOfNumbers = inputNumbers.split( )
numbers = [int(number) for number in listOfNumbers]
average = sum(numbers) / len(numbers)
print("Average number is ", average)



#Eighth task
print("  @..@\n (----)\n (\_/)\n ^^ "" ^^")

#NINTH TASK 
A = int(input("A cathetus: "))
B = int(input("B cathetus: "))
C = int(input("C cathetus: "))
P = A + B + C
print("THE PERIMETER OF THE TRIANGLE IS ", P).capitalize()
print("{0} + {1} + {2} = {3}".format(A,B,C,A+B+C))

#Tenth task
pizzaprice = 12.90
tipsinpercent = 10
people = 2
tips = (pizzaprice) * (tipsinpercent) / 100
needtopay = round(((pizzaprice + tips) / people),2)
print("each person should to pay ",needtopay,"euro" )

# comment - ctrl+k + c; !comment - ctrl+k + u;