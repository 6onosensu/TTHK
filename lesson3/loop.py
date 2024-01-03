import math
from random import randint as rand

# break, continue, pass
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue  # continue skips to the next iteration of the loop
    print(i, end="")
while True:
    name = input("Enter your name: ")
    if name == "":
        break  # Break used to terminate the loop entirely
for i in range(1, 21):
    if i == 13:
        pass  # pass does nothing, acts as a placeholder
    else:
        print(i)

# 29
print("task 29")
for i in range(9):
    for x in range(9):
        if x == 0 or i == x:
            print("x", end=" ")
        else:
            print("0", end=" ")
    print()

# 17,1
a = int(input("Enter the first factor: "))
b = int(input("Enter the second factor: "))
for i in range(1, a + 1):
    for j in range(1, b + 1):
        product = i * j
        str_product = len(str(product))
        if str_product < 1:
            product = str(product) + "   |"
        elif str_product < 2:
            product = str(product) + "  |"
        elif str_product < 3:
            product = str(product) + " |"
        else:
            product = str(product) + "|"
        print(product, end="")
    print()

# 17
for num in range(1, 10):
    print("multiplication by", num)
    for num2 in range(1, 10):
        expression = f"{num} * {num2}"
        multiplication = eval(expression)
        print(expression, "=", multiplication)

# 16,1
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# 16
for i in range(1, 10):
    for x in range(1, 10):
        if x == i and i != 0:
            print(i, end=" ")
        else:
            print("0", end=" ")
    print()

# 15
print(" ")
for y in range(10):
    for x in range(10):
        print(x, end=" ")
    print()

# 14
N = rand(1, 100)
product = 1
for i in range(1, N):
    product *= i
print(product)

# 13
count = 0
sum = 0
for i in range(100, 1000):
    if i % 7 == 0:
        count += 1
        sum += i
print(count, sum)

# 13 chatgpt:
sum = 0
numbers = [n for n in range(100, 1001) if n % 7 == 0]  # list
count = len(numbers)
for i in numbers:
    sum += i
print(count, sum)

# 12
N = rand(2, 10)
m = rand(1, 10)
sum = m
print("Hay mowers: ", N)
print("Hours:", m)
for t in range(N-1):
    m = (m / 6) * 7
    sum += m
print("Hay movers were work:", round(sum, 2), "hr")

# 11
product = 1
a = rand(2, 99)
for num in range(11, 100, 2):
    if num % a == 0:
        print("num is", num)
        product *= num
        print(f"a: {a}, product: {product}")

# 10
txt = "Enter 10 pairs of numbers in this form(1,2; 3,4; ...): "
list_of_pairs = input(txt).split("; ")
for pair in list_of_pairs:
    two_num = pair.split(",")
    txt = "The bigger number is:"
    if two_num[0] > two_num[1]:
        print(txt, two_num[0])
    else:
        print(txt, two_num[1])

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
for i in range(1, 20):
    i *= one_inch
    count += 1
    print("{0} inch is equel: ".format(count), i, "cm")

# 7
K = int(input("7:Enter a multiple number: "))
A = int(input("Enter start of the interval: "))
B = int(input("Enter end of the interval: "))
for i in range(A, B):
    if i % K == 0:
        print(i)

# 6
positive_numbers = []
negative_numbers = []
inputNumbers = input("6:Enter your numbers using space button: ")
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
inputNumbers = input("5:Enter your numbers using space button: ")
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
