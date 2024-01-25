from functions import *


txt = ": "
while True:
    enter = input(txt).split()
    if enter == "quit":
        break

    country_capital, capital_country, countries = txt_to_dict("countries.txt")
    if enter[0] == "find":
        if enter[1] == "capital":
            key, value = show_country(capital_country, enter[2], country_capital)
        elif enter[1] == "country":
            key, value = show_capital(country_capital, enter[2], capital_country)
    elif enter[0] == "":
        pass
