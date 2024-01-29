def read_file(file):
    file = open(file,'r',encoding="utf-8")
    list = [] 
    for row in file:
        list.append(row.strip())
    file.close()
    return list

def is_latin_letter(letter):
    return '\u0400' <= letter <= '\u04FF'

def is_russian_letter(letter):
    return '\u0041' <= letter <= '\u005A' or '\u0061' <= letter <= '\u007A'

def translate_to_russian(eng: list, rus: list, word: str):
    for i, search_w in enumerate(eng):
        if search_w == word:
            return rus[i]

def translate_to_english(rus: list, eng: list, word: str):
    word = word.capitalize()
    for search_w, eng_w in zip(rus, eng):
        if search_w == word:
            return eng_w
        