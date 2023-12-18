from random import *


#6
quatntity_numbers = randint(2, 20)
list_of_numbers = []
for _ in range (quatntity_numbers):
  list_of_numbers.append(randint(1, 1000))
print(list_of_numbers)
while True:
  max_number = max(list_of_numbers)

  num_index = list_of_numbers.index(max_number)
  list_of_numbers.pop(num_index)

  number = round(max_number / len(list_of_numbers), 2)

  list_of_numbers.append(number)
  
  if max(list_of_numbers) <= 1:
    break

print(list_of_numbers)

#7
for element in list_of_numbers:
  if element < 0:
    num = list_of_numbers.index(element)
    list_of_numbers[n] = abs(element)

list_of_numbers.sort()
print(f"From 0 to 1.0: {list_of_numbers}")
list_of_numbers.reverse()
print(f"From 1.0 to 0: {list_of_numbers}")

#Change NADO SDELAT 5
max_quantity = randint(2, 20)
num_list = []
for i in range (max_quantity):
  num_list.append(randint(-100, 100))
print(num_list)





#postiindex 4
keys = [1, 2, 3]
dictionary = {
  1: "Tallinn",
  2: "Narva, Narva-Jõesuu",
  3: "Kohtla-Järve",
  4: "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",
  5: "Tartu",
  6: "Tartumaa, Põlvamaa, Võrumaa, Valgamaa",
  7: "Viljandimaa, Järvamaa, Harjumaa",
  8: "Pärnumaa",
  9: "Läänemaa, Hiiumaa, Saaremaa"}
  
while True:
  try:
    postcode = input("Enter the postcode: ")
    if len(postcode) == 5 and postcode.isdigit:
      print(postcode)
      break
    elif postcode == "stop":
      break    
  except:
    print("viga")
print("Wait a minute!")

first_num = int(postcode[0])

for key, value in dictionary.items():
  if key == first_num:
    print(f"The postcode {postcode} belongs to {value}! ")
    if key == list(keys):
      print("Please, Stay at home!")
    else:
      print("Please, wear a mask!")

