print("Hello! I am your new friend - Python!")

name = input("What is your name?: ")

print(f"{name}, oh, what a beautiful name you have!")

try:
  q = int(input(f"{name}, Can I find out your Body Mass Index? 0-No, 1-Yes! => "))

  if q == 1:
    height = int(input("Your height in cm: "))
    weight = float(input("Your weight in kg: "))
    
    index = weight / (0.01 * height) ** 2
    print(f"{name}! Your body mass index is: {index:.1f}") #.1f - .1 kol-vo znakov posle zapjatoi and f - format plawujuwaja to4ka

    if index < 16:
        print("Underweight dangerous to health")
    elif 16 <= index < 19:
        print("Underweight")
    elif 19 <= index < 25:
        print("Normal Weight")
    elif 25 <= index < 30:
        print("Overweight")
    elif 30 <= index < 35:
        print("Obesity")
    elif 35 <= index < 40:
        print("Severe obesity")
    else:
        print("Obesity is dangerous to health")

  else:
    print("Too bad! This is very useful information!")
    print()
    print(f"See you soon, {name}! Forever yours, Python!")

except ValueError:
  print("Invalid input! Please enter the correct number.")
