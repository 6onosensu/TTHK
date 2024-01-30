from functions import *


txt = """
translation of a word: t 'word'
to show all words: show
to edit a word: edit

    : """
while True:
    user_input = input(txt).lower().strip()
    if not user_input:
        continue

    if user_input[0] == "quit":
        break

    try:
        rus: list = read_file("./sonastik/rus.txt")
        eng: list = read_file("./sonastik/eng.txt")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        continue

    if user_input.startswith("t "):
        word_to_translate = user_input.split(maxsplit=1)[1]
        first_letter = word_to_translate[0]
        if is_latin_letter(first_letter):
            translated_word = translate_to_russian(eng, rus, word_to_translate)
            if translated_word == "Translation not found":
                eng, rus = question(eng, rus, word_to_translate)
                write_to_file("./sonastik/eng.txt", eng)
                write_to_file("./sonastik/rus.txt", rus)
        elif is_russian_letter(first_letter):
            translated_word = translate_to_english(eng, rus, word_to_translate)
            if translated_word == "Translation not found":
                eng, rus = question(eng, rus, word_to_translate)
                write_to_file("./sonastik/eng.txt", eng)
                write_to_file("./sonastik/rus.txt", rus)
    elif user_input.startswith("show"):
        show_words(eng, rus)
    elif user_input.startswith("edit"):
        eng, rus = edit(eng, rus)
        write_to_file("./sonastik/eng.txt", eng)
        write_to_file("./sonastik/rus.txt", rus)
    elif user_input.startswith("test"):
        pass
