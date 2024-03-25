import math

#8
time_min = int(input("Enter the time in minutes: "))
hours = time_min // 60
minutes = time_min % 60
print(f"{hours}:{minutes:02d}") 
# :02d
#02 - esli 4islo menee 4em iz 2 4isel, to ono budet dopolneno 00 sleva do 2 cifr
#d - 4islo predstavleno v vide celogo desjati4nogo chisla

#7
average_speed_km = 29.9
speed_mmin = average_speed_km * 1000 / 60
print("A roller skater covers {0} meters in a minute".format(speed_mmin))

#6
fuel = float(input("Enter the amount of the fuel filled in liters: "))
km_traveled = float(input("Enter the kilometers traveled: "))
calculate_fuel_consumption = (fuel / km_traveled) * 100
print("Your average fuel consumption per 100 km:", calculate_fuel_consumption)
#5
a = float(input("Enter the side 'a' of the rectangle: "))
b = float(input("Enter the side 'b' of the rectangle: "))
P = a * 2 + b * 2
S = a * b
print("Opposite sides of the rectangle {0} and {1}.\nPerimeter of the rectangle is {2}.\nArea of the rectangle is {3}".format(a,b,P,S))

#4
lyrics = """
The train was running tush tush tush,
the peeping duck was the train driver.
Wheels made wheel tat taa,
rat tat taa and tat tat taa.
But there on the train,
do you know who was there
"""
print(lyrics)

new_lyrics = """
The train was going tut tut tut,
the peeping duck was the train driver.
The wheels made kill koll koll,
kill koll koll and kill koll kill.
"""
print(new_lyrics)


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