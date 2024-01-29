

def txt_to_dict(f: str):
    country_capital = {}
    capital_country = {}
    countries = []
    file = open(f, "r", encoding="utf-8-sig")
    for line in file:
        key, value = line.strip().split("-")
        country_capital[key] = value
        capital_country[value] = key
        countries.append(key)
    file.close()
    return country_capital, capital_country, countries

def question(param: str, c: str, dicty: dict):
    txt = f"Would you like to add this {param} to list?: "
    i = input(txt)
    if i[1] == "y":
        add_to_dict(param, c, dicty)
    else:
        return False

def show_capital(dicty: dict, country: str, dict2: dict):
    param = "capital"
    country = country.capitalize()
    for key, value in dicty.items():
        if country == key:
            print(f"{key}: {value}")
        else:
            question(param, country, dict2)
    return key, value

def show_country(dicty: dict, capital: str, dict2: dict):
    param = "country"
    capital = capital.capitalize()
    for key, value in dicty.items():
        if capital == key:
            print(f"{key}: {value}")
        else:
            question(param, capital, dict2)
    return key, value

def add_to_dict(param: str, c: str, co_ca: dict, ca_co: dict):
    if param == "country":
        capital = input(f"Enter the capital of {c}: ")
        co_ca.update({c: capital})
        ca_co.update({capital: c})
    else:
        country = input(f"Enter the country of {c}: ")
        co_ca.update({c: capital})
        ca_co.update({capital: c})

