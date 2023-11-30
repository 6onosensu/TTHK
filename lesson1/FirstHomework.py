import math
#2.2 Radius of the Earth -6378km. Diameter of a 2 euro coin is 25.75 millimeters
EARTH_RADIUS_KM = 6378
TWO_EURO_COIN_MM = 25.75


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