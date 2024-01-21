def find_smallest(list: list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index

def find_largest(list: list):
    largest = list[0]
    largest_index = 0
    for i in range(1, len(list)):
        if list[i] > largest:
            largest = list[i]
            largest_index = i
    return largest_index

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
def largest_salary(people: list, salaries: list):
    index = find_largest(salaries)
    largest = salaries[index]
    list_of_names = []
    for i in range(len(salaries)):
        if salaries[i] == largest:
            list_of_names.append(people[i])
    # list_of_names = [people[i] for i in range(len(salaries)) if salaries[i] == largest]
    return largest, list_of_names

# 4
def smallest_salary(people: list, salaries: list):
    index = find_smallest(salaries)
    smallest = salaries[index]
    list_of_names = []
    for i in range(len(salaries)):
        if salaries[i] == smallest:
            list_of_names.append(people[i])
    return smallest, list_of_names

# 5
'''
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
'''
def sort_salaries_with_people(people: list, salaries: list, sortby):
    sorted_people = []
    sorted_salaries = []
    if sortby == "lower":
        for i in range(len(salaries)):
            smallest = find_smallest(salaries)
            sorted_salaries.append(salaries.pop(smallest))
            sorted_people.append(people.pop(smallest))
    else:
        for i in range(len(salaries)):
            largest = find_largest(salaries)
            sorted_salaries.append(salaries.pop(largest))
            sorted_people.append(people.pop(largest))
    return sorted_people, sorted_salaries

# 6
'''
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
'''
def find_same_salary(people: list, salaries: list):
    checked = []  # or checked = set()
    for i in range(len(salaries)):
        if salaries[i] in checked:
            continue
        same_salary_people = [people[i]]
        for j in range(i + 1, len(salaries)):
            if salaries[i] == salaries[j]:
                same_salary_people.append(people[j])
        if len(same_salary_people) > 1:
            print(f"Salary {salaries[i]}: {', '.join(same_salary_people)}, Quantity: {len(same_salary_people)}")
            checked.append(salaries[i])  # or checked.add(salaries[i]) if 164 is set

# 7
def find_salary_by_name(people: list, salaries: list, name: str):
    name = name.capitalize()
    salary_list = []
    for i, person in enumerate(people):
        person = person.capitalize()
        if person == name:
            salary_list.append(salaries[i])
    return name, salary_list
# enumerate() - used for to simultaneously obtain the index and value of elements when iterating through a list
            
# 8
def filter_by_salary(people: list, salaries: list, amount, mode="more"):
    result = []
    amount = float(amount)
    for i in range(len(salaries)):
        salary = float(salaries[i])
        if (mode == "more" and salary > amount) or (mode == "less" and salary < amount):
            print(f"{people[i]}: {salary}")
            result.append((people[i], salary))
    return result

# 9
def top(people: list, salaries: list):
    poorest_index = find_smallest(salaries)
    richest_index = find_largest(salaries)
    poorest_person = people[poorest_index]
    richest_person = people[richest_index]
    print("The poorest:", poorest_person, salaries[poorest_index])
    print("The richest:", richest_person, salaries[richest_index])

# 10
def average(people: list, salaries: list):
    average_salary = sum(salaries) / len(salaries)
    closest_salary_difference = abs(salaries[0] - average_salary)
    closest_people = [people[0]]

    for i in range(1, len(salaries)):
        difference = abs(salaries[i] - average_salary)
        if difference <= closest_salary_difference:
            if difference < closest_salary_difference:
                closest_salary_difference = difference
            closest_people.append(people[i])
            salary = salaries[i]
    print(f"The average salary is: {salary}, and it is received by: {', '.join(closest_people)}")
    return closest_people, salary

# 11
def net_salary(people: list, salaries: list, tax_rate=0.2):
    net_salaries = []
    for gross_salary in salaries:
        net_salary = gross_salary - (gross_salary * tax_rate)
        net_salaries.append(net_salary)
    for net_salary in net_salaries:
        for person in people:
            print(f"{person}: Net salary is {net_salary}")
    return net_salaries

# 12
def sort_list(people: list, salaries: list, param):
    if param == "za":
        people.sort(reverse=True)
    else:
        people.sort()

    sorted_salaries = []
    for person in people:
        index = people.index(person)
        sorted_salaries.append(salaries[index])
    person_salary(people, sorted_salaries)
    return people, sorted_salaries

# 13
def remove_below_average(people: list, salaries: list):
    _, average_salary = average(people, salaries)
    to_remove = []
    for i, salary in enumerate(salaries):
        if salary < average_salary:
            to_remove.append(i)

    for index in reversed(to_remove):
        del people[index]
        del salaries[index]

    print(people, salaries)
    return people, salaries

# 14
def format_lists(people: list, salaries: list):
    formatted_people = []
    formatted_salaries = []
    for person in people:
        person = person.capitalize()
        formatted_people.append(person)
    for salary in salaries:
        salary = int(salary)
        formatted_salaries.append(salary)
    person_salary(formatted_people, formatted_salaries)
    return formatted_people, formatted_salaries

# 15
def calc_new_salary(people: list, salaries: list, years: int, employee, percent=0.05):
    name, salary = find_salary_by_name(people, salaries, employee)
    future_salary = salary * (1 + percent) ** years
    print(f"In {years} years, employee {name} will receive: {future_salary}")
    return future_salary

# 16
def rename_every_third_person(people: list):
    for i in range(2, len(people), 3):
        new_name = input(f"Enter a new name for {people[i]}: ")
        people[i] = new_name
    print(people)
    return people
    
# 17
def edit_data(people: list, salaries: list, choice, index):
    index = int(index)
    if index >= len(people):
        print("Index out of range of the list")
    else:
        if choice == "name":
            new_name = input("Enter a new name: ")
            people[index] = new_name
        elif choice == "salary":
            new_salary = float(input("Enter a new salary: "))
            salaries[index] = new_salary
    person_salary(people, salaries)
    return people, salaries

# 18
def find_names_starting_with(people: list, salaries: list, letter):
    letter = letter.capitalize()
    print(letter)
    for name, salary in zip(people, salaries):
        if name.startswith(letter):
            print(f"{name} - {salary}")

   