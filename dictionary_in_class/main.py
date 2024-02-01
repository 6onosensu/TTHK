from functions import *


txt = "your command 'find/edit/add country/capital 'country itself'/'capital itself ': "
while True:
    enter = input(txt).lower().split()
    if enter == "quit":
        break

    country_capital = txt_to_dict("countries.txt")
    if enter[0] == "find":
        key, value = show_country(country_capital, enter[1], enter[2])
    elif enter[0] == "edit":
        pass
    elif enter[0] == "add":
        pass