asked_to_add_word = False

def read_file(file):
    file = open(file,'r',encoding="utf-8")
    list = [] 
    for row in file:
        list.append(row.strip())
    file.close()
    return list

def write_to_file(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(item + '\n')


def is_latin_letter(letter):
    return '\u0041' <= letter <= '\u005A' or '\u0061' <= letter <= '\u007A'

def is_russian_letter(letter):
    return '\u0400' <= letter <= '\u04FF'

def show_words(eng: list, rus: list):
    for e, r in zip(eng, rus):
        print(e, ":", r)

def question(eng: list, rus: list, word: str):
    global asked_to_add_word
    if asked_to_add_word:
        return eng, rus

    txt = f"Would you like to add word '{word}' to list?: "
    i = input(txt).lower()
    if i == "yes":
        eng, rus = add_to_list(eng, rus, word)
        asked_to_add_word = True
    else:
        print("OK, maybe later!")
        asked_to_add_word = True
    return eng, rus

# box - коробка
def add_to_list(eng: list, rus: list, word: str):
    txt = f"Enter the translation of the {word}: "
    if is_latin_letter(word[0]):
        translation = input(txt).capitalize()
        eng.append(word)
        rus.append(translation)
    elif is_russian_letter(word[0]):
        translation = input(txt).capitalize()
        eng.append(translation)
        rus.append(word)
    return eng, rus

def translate_to_russian(eng: list, rus: list, word: str):
    translated_word = "Translation not found"
    word = word.lower()
    for i, search_w in enumerate(eng):
        if search_w.lower() == word:
            translated_word = rus[i]
            print(f"{search_w} - {translated_word}")
            break
    return translated_word

def translate_to_english(rus: list, eng: list, word: str):
    translated_word = "Translation not found"
    word = word.lower()
    for search_w, eng_w in zip(rus, eng):
        if search_w.lower() == word:
            translated_word = eng_w
            print(f"{search_w} - {eng_w}")
            break
    return translated_word

def edit(eng: list, rus: list):
    txt = "Enter a word to edit it: "
    enter = input(txt).lower()

    for i, (rw, ew) in enumerate(zip(rus, eng)):
        if rw.lower() == enter or ew.lower() == enter:
            txt1 = "Enter the correct word in Russian: "
            edited_word_rus = input(txt1)

            txt2 = "Enter the correct word in English: "
            edited_word_eng = input(txt2)

            rus[i] = edited_word_rus.capitalize()
            eng[i] = edited_word_eng.capitalize()
            return eng, rus
    print(f"The word '{enter}' not found!")
    return eng, rus