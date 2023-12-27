import math
from random import randint as rand

# 12
N = rand(2, 10)
m = rand(1, 10)
sum = m
print("Cars: ", N)
print("Hours:", m)
for t in range(N-1):
    m = (m / 6) * 7
    sum += m
    print(m)
print("Cars were work: ", sum, "hr")

# 29
for i in range(9):
    for x in range(9):
        if x == 0 or i == x:
            print("x", end=" ")
        else:
            print("0", end=" ")
    print()

# 15
for y in range(10):
    for x in range(10):
        print(x, end=" ")
    print()

# 9
interest_now = float(input("Enter the deposit interest rate now: "))
money = float(input("""How much money would you like to deposit
                     at {0} percent interest?: """.format(interest_now)))
years = int(input("How many years?: "))
for year in range(years):
    interest = interest_now / 100
    money += money * interest
print("""In {0} years, the amount of your deposit with {1}
      interest rate will be: {2} """.format(years, interest_now, money))

# 8
one_inch = 2.5
count = 0
for i in range(1, 20,):
    i *= one_inch
    count += 1
    print("{0} inch is equel: ".format(count), i, "cm")

# 7
K = int(input("Enter a multiple number: "))
A = int(input("Enter start of the interval: "))
B = int(input("Enter end of the interval: "))
for i in range(A, B):
    if i % K == 0:
        print(i)

# 6
positive_numbers = []
negative_numbers = []
inputNumbers = input("Enter your numbers using space button: ")
listOfNumbers = inputNumbers.split(" ")
numbers = [int(number) for number in listOfNumbers]
for number in numbers:
    if number < 0:
        negative_numbers.append(number)
    else:
        positive_numbers.append(number)
print("Quantity of the positive numbers and zero is ", len(positive_numbers),
      "and quantity of the negative numbers is ", len(negative_numbers))

# 5
answer = 0
inputNumbers = input("Enter your numbers using space button: ")
listOfNumbers = inputNumbers.split(" ")
print(listOfNumbers)
numbers = [int(number) for number in listOfNumbers]
print(numbers)
for number in numbers:
    if number < 0:
        answer += number
print(answer)

# 4
for x in range(10, 20):
    square = x ** 2
    print("Here is sqaure of the {0}: ".format(x), square)

# 3
answer = 1
for x in range(8):
    number = int(input("Enter your 8 numbers: "))
    if number > 0:
        answer *= number
print(answer)

# 3 2 variant
p = 1
string = ""
for x in range(8):
    A = float(input("{0}. samm\nInput A: ".format(x + 1)))
    if A > 0:
        p *= A
        string = string + str(A) + "*"
print(string[:-1], "=", p, end="")

# 2
answer = 0
A = int(input("Enter A: "))
for x in range(1, A + 1, 1):
    answer += x
print(answer)

# 1
t = 0
for x in range(15):
    A = float(input("Enter A: "))
    if A.is_integer():
        t += 1
print(t)

###
for x in range(10):
    R = float(input("{0}.R ".format(x)))
    if R > 0:
        S = math.pi * R ** 2
    else:
        S = "R must be > than 0"
    print("S = {0}".format(S))

x = 0
while True:
    x += 1
    R = float(input("{0}.R ".format(x + 1)))
    if R > 0:
        S = math.pi * R ** 2
    else:
        S = "R must be > than 0"
    print("S = {0}".format(S))
    if x == 10:
        break

while x < 10:
    R = float(input("{0}.R ".format(x)))
    if R > 0:
        S = math.pi * R ** 2
        x += 1
    else:
        S = "R must be > than 0"
    print("S = {0}".format(S))
