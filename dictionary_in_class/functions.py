def txt_to_dict(f: str):
    country_capital = {}
    file = open(f, "r", encoding="utf-8-sig")
    for line in file:
        key, value = line.strip().split("-")
        country_capital[key] = value
    file.close()
    return country_capital

def show_country(country_capital: dict, param: str, c: str):
    c = c.capitalize()
    if param == "country":
        for key, value in country_capital.items():
        if c == key:
            print(f"{key}: {value}")
        else:
            question(country_capital, param, c)
    elif param == "capital":
        for key, value in country_capital.items():
            if c == value:
                print(f"{value}: {key}")
            else:
                question(country_capital, param, c)
    return key, value

def question(country_capital: dict, param: str, c: str):
    txt = f"Would you like to add this {param} to list?: "
    i = input(txt)
    if i[1] == "y":
        add_to_dict(country_capital, param, c)
    else:
        return False    

def add_to_dict(country_capital: dict, param: str, c: str):
    if param == "country":
        capital = input(f"Enter the capital of {c}: ")
        co_ca.update({c: capital})
        ca_co.update({capital: c})
    else:
        country = input(f"Enter the country of {c}: ")
        co_ca.update({c: capital})
        ca_co.update({capital: c})

def edit(country_capital: dict,  param: str, c):
    pass