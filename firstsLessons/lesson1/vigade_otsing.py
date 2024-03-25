import math
from math import sqrt, pi
#bqlo import * from math

print("Ruudu karakteristikud")
a = float(input('Sisesta ruudu külje pikkus => ')) #ne bqlo float() , a bez nego eto obq4naja stroka
S = a ** 2
P = 4 * a
di = a * math.sqrt(2)
print("Ruudu pindala", S)
print("Ruudu ümbermõõt ", P) #ne bqlo " v konce
print("Ruudu diagonaal", round(di,2))

#ubrala pustoi print()

print("Ristküliku karakteristikud") #liwnaja skobka bqla
b = float(input("Sisesta ristküliku 1. külje pikkus => "))
c = float(input("Sisesta ristküliku 2. külje pikkus => "))
S = b * c
P = 2 * (b + c) # ne bqlo *
di = math.sqrt(b ** 2 + c ** 2) #bqlo vmesto vozvedenija v stepen - umnozenie
print("Ristküliku pindala", S) #zamenila na obq4nqe ""
print("Ristküliku ümbermõõt", P)
print("Ristküliku diagonaal", round(di, 1)) #ne bqlo ) + nado bqlo pripisat k round v skobku ", 1"

#ubrala pustoi print()

print("Ringi karakteristikud")
r = float(input("Sisesta ringi raadiuse pikkus => ")) #zamenila kawq4ki
d = 2 * r #d=2r
S = math.pi * r ** 2 #pi - ne funkcia, bqlo: pi() + tut bqlo *2, a nado **2
C = 2 * math.pi * r #C=2pi()*r
print("Ringi läbimõõt", d) #ne bqlo ","
print("Ringi pindala", round(S, 2)) #  round(S))
print("Ringjoone pikkus", round(C, 2)) #round(C) ne bqlo )

#takwe vede gde prinimaetsja 4islo v input dobavila float ili int.