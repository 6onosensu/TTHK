from functions import *

txt = "translation of a word: t 'word'"
while True:
    enter = input(txt).split()
    if enter == "quit":
        break

    rus: list = read_file("rus.txt")
    eng: list = read_file("eng.txt")

    if enter[0] == "t":
        first_letter = enter[1].split("")[0]
        if is_latin_letter(first_letter):
            rus_w = translate_to_russian(eng, rus, enter[1])
        elif is_russian_letter(first_letter):
            eng_w = translate_to_english(rus, eng, enter[1])
            


