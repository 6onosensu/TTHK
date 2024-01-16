def print_actions(people: list, salaries: list):
    print("")
    print("Add to the list: add person salary")
    print("Delete from the list: delete person salary")
    print("The highest salary: max")
    print("The lowest salary: min")
    print("To sort ((higher-from higher/lower-from lower) salary): sort salaries higher/lower")
    print("To see each person with salary: show each")
    print("Find peopele with same salary: same salary")
    print("")


def controller(people: list, salaries: list, action):
    if action[0] == "add":
        person = action[1]
        salary = action[2]
        people, salaries = add_to_list(people, salaries, person, salary)
        person_salary(people, salaries)  
    elif action[0] == "delete":
        person = action[1]
        salary = action[2]
        people, salaries = delete_from_list(people, salaries, person)
        person_salary(people, salaries)
    elif action[0] == "max":
        maximum, names = highest(people, salaries)
        for name in names:
            print(f"This person has the highest salary: {name} with the salary: {maximum} Eur")
    elif action[0] == "min":
        minimum, names = lowest(people, salaries)
        for name in names:
            print(f"This person has the lowest salary: {name} with the salary: {minimum} Eur")
    elif action[0] == "sort" and action[1] == "salaries":
        if action[2] == "lower" or action[2] == "higher":
            s_people, s_salaries = sort_salaries(people, salaries, action[2])
            print(s_people, s_salaries)
        else:
            print("Wrong action 3, must be 'lower' or 'higher'")
    elif action[0] == "show" and action[1] == "each":
        person_salary(people, salaries)
    elif action[0] == "same" and action[1] == "salary":
        find_same_salary(people, salaries)



def person_salary(people: list, salaries: list):
    if len(people) == len(salaries):
        for i in range(len(people)):
            print(f"Person: {people[i]}, Salary: {salaries[i]}")
    else:
        print("The lists are empty or incomplete")

# 1
def add_to_list(people: list, salaries: list, person, salary):
    salary = int(salary)
    people.append(person)
    salaries.append(salary)
    return people, salaries
 
# 2
def delete_from_list(people: list, salaries: list, person):
    if person in people:
        index = people.index(person)
        people.pop(index)
        salaries.pop(index)
    else:
        print(person, " is not in the list!")
    return people, salaries
'''
def delete(people, salaries, person):
    i = 0
    length = len(people)
    while i < length:
        if person == people[i]:
            people.pop(i)
            salaries.pop(i)
            length = len(people)
        else:
            i += 1
    return people, salaries
'''


# 3
def highest(people: list, salaries: list):
    list_of_names = []
    maximum = max(salaries)

    quantity = salaries.count(maximum)
    a = 0
    for _ in range(quantity):
        index = salaries.index(maximum, a)
        name = people[index]
        a += 1
        list_of_names.insert(name)
    return maximum, list_of_names  

# 4
def lowest(people: list, salaries: list):
    list_of_names = []
    minimum = min(salaries)
    quantity = salaries.count(minimum)
    a = 0
    for _ in range(quantity):
        index = salaries.index(minimum, a)
        name = people[index]
        a += 1
        list_of_names.insert(name)
    return minimum, list_of_names  

# 5
def sort_salaries(people: list, salaries: list, sortby):
    # zip(list1, list2) - Combines two lists into a list of tuples
    # zip(*variable) - The * operator for unpacking a list of tuples
    # sorted(list, reverse=False) - in sscending order (default)
    # sorted(list, reverse=True) - in descending order
    # return list() - zip returns tuples
    if sortby == "lower":
        sorted_pairs = sorted(zip(salaries, people))
        sorted_salaries, sorted_people = zip(*sorted_pairs)
    else:
        sorted_pairs = sorted(zip(salaries, people), reverse=True)
        sorted_salaries, sorted_people = zip(*sorted_pairs)
    return list(sorted_people), list(sorted_salaries)

# 6
def find_same_salary(people: list, salaries: list):
    dictionary = {}
    for salary, person in zip(salaries, people):
        if salary in dictionary:
            dictionary[salary].append(person)
        else:
            dictionary[salary] = [person]
    for salary, names in dictionary.items():
        if len(names) > 1:
            print(f"Salary {salary}: {', '.join(names)}")


# 7
def find_salaries_by_name():
    pass


def sort_list(people: list, salaries: list):
    salaries = salaries.sort()
    people = people.sort()
    return people, salaries
