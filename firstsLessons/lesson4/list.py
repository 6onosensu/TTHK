import string
# 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number * "*")

# 2
# some = [] ; k= set(some) - po 1 dublikatu

random_names = input("Enter 5 random names using space button: ").split(" ")
random_names = list(random_names)
random_names.sort()
print(random_names)

last_element = random_names.pop()
print("The last name of the list is", last_element)

change_name = input("Would you like to change the names? yes/no: ").lower()
if change_name == "yes":
    try:
        to_change = float(input("number of the name, that you want to change: "))
        print(to_change)
        for name in random_names:
            if to_change == name.index() - 1:
                name_to_change = input("Enter a new name: ")
                name_to_change = random_names[name]
            print(random_names)
    except ValueError:
        print("There must be an integer!")
elif change_name == "no":
    print("Okey! There is your list of names:", random_names)

random_names_by1 = set(random_names)
print(random_names_by1)

# 1
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
signs = string.punctuation

vowels_count = 0
consonants_count = 0
spaces_count = 0
signs_count = 0
numbers_count = 0
sentence = input("Enter your word or sentence: ").lower()
for element in sentence:
    if element == " ":
        spaces_count += 1
    elif element in signs:
        signs_count += 1
    elif element in vowels:
        vowels_count += 1
    elif element in consonants:
        consonants_count += 1
    elif element.isdigit():
        numbers_count += 1
    else:
        print(f"There is no such: a {element} element here!")
print(f"This text have: Vowels - {vowels_count},",
      f"Consonants - {consonants_count},",
      f"Spaces - {spaces_count},",
      f"Signs - {signs_count},",
      f"Numbers {numbers_count}")

####
text = input("Input your text: ")

text_list = list(text)
length = len(text_list)
sum = 0

if text.isdigit():
    for t in range(length):
        num = int(text_list[t])
        text_list.pop(t)
        text_list.insert(t, num)

for number in text_list:
    sum += num

print("Sum :", sum)
print(text_list)


element = input("Element: ")

if element.isalpha():
    index = text_list.index(element)
else:
    index = text_list.index(int(element))
print(f"Element: {element} in {index}")
