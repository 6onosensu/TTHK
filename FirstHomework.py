import math
#4

#3
phrase_1 = "kill-koll"
phrase_2 = "killadi-koll"
phrase_3 = "killkoll"

for i in range(1, 10):
  if i == 3 or i == 6:
    print(phrase_2, end=' ')
  else:
    print(phrase_1, end=' ')
print(phrase_3)
print(phrase_1)

#2.2 Radius of the Earth -6378km. Diameter of a 2 euro coin is 25.75 millimeters
earth_radius_km = 6378
coin_diameter_mm = 25.75

earth_radius_m = earth_radius_km * 1000
coin_diameter_m = coin_diameter_mm / 1000

circumference_of_earth_m = 2 * math.pi * earth_radius_m
number_of_coins = circumference_of_earth_m / coin_diameter_m

print(f"Number of coins: {number_of_coins:.0f}")

#2.1 Ruudu sees asub ring. Ringi raadius on R. S,P-SQUARE; S,P-CIRCLE ???
r = float(input("There is a circle inside a square, write the radius for it: "))
S_circle = round(math.pi * r ** 2, 2)
C_circle = round(2 * math.pi * r, 2)
S_square = round((2 * r) ** 2, 2)
P_square = round(4 * 2 * r, 2)
print("Area and perimeter of a circle:", S_circle, C_circle, "and of a square:", S_square, P_square)

#2 
answer1 = 3 + 8 / (4 - 2) * 4 #tut sna4ala to 4to v skobkah, zatem 8/2 i poslednim 3+4*4 
answer2 = 3 + 8 / 4 - 2 * 4 #1) 8/4 2)3+2 3)5-2*4
#Ispolzovanije skobok vlijajet na porjadok v vqrazenii
print("Task 2:", answer1, answer2)

#1 Kirjuta programm, mis sind tervitab.
name = input("What is your name?: ").capitalize()
print("Hi!", name)