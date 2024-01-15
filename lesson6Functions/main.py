from functions import *
from random import randint

mounth = int(input("Enter a mounth as a number: "))
season = year_seasons(mounth)
print(season)

a = input(": ")
b = date(a)
print(b)

a = randint(0, 1000)
prime = is_prime(a)
print(prime)

a = input("Enter how much eur deposit in to your bank account with 10% in year: ")
b = bank(a)
print(b)

square_side = input("Enter a side of the square: ")
func = square(square_side)
print(func)

numbers = input("Enter a, sign and b (separated ˇ ˇ): ").split(" ")
a = numbers[0]
sign = numbers[1]
b = numbers[2]
calculator = cacl(a, sign, b)
print(calculator)

year = input("Enter a year and you will know is it a leap year?: ")
is_leap = is_year_leap(year)
print(is_leap)