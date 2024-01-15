import math

def sum3(a: float, b: float, c: float)->float:
    """
    Return sum of the a, b and c

    :param float a
    :param float b
    :param float c
    :rtype: float

    """
    sum = a + b + c
    return sum

def cacl(a, sign, b)->any:
    """
    simple calculator 
    a: the first number
    c: sign
    b: the second number
    """
    signs = ["+", "-", "*", "/"]
    if sign in signs:
        if b == 0 and sign == "/":
            asnwer = "DIV/0"
        else:
            expression = eval(str(a)+sign+str(b))
            answer = f"{a}{sign}{b} = {expression}"
    else:
        answer = "Incorrect actions"
    return answer

def is_year_leap(year)->bool:
    """
    
    """
    year = int(year)
    if year % 4 == 0:
        answer = True
    else: answer = False
    return answer

def square(a)->any:
    a = float(a)
    P = a * 4
    S = a ** 2
    d = round(a * math.sqrt(2), 2)
    answer = f"Perimeter: {P}, Area: {S}, and diagonal: {d}" 
    return answer

def year_seasons(mounth)->str:
    seasons = {[1, 2, 12]: "winter", [3, 4, 5]: "spring",
               [6, 7, 8]: "summer", [9, 10, 11]: "autumn"}
    for mounths, season in seasons:
        if mounth in mounths:
            return season

def bank(a: float, years: int)->float:
    for year in range(years):
        a *= 1.1
    return a

def is_prime(a)->bool:
    answer = False
    for i in range(2, a):
        if a % i == 0:
            answer = True
    return answer

def date(day, mounth, year)->bool:
    if day in range(1, 31) and mounth in [1,3,5,7,8,10,12]:
        answer = True
    elif day in range(1, 29) and mounth == 2 and is_year_leap(year):
        answer = True
    elif day in range (1, 30) and mounth in [2,4,6,9,10]:
        answer = True
    else:
        answer = False
    return answer

def XOR_cipher(string, key)->str:
    pass