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
            





def sort_list(people: list, salaries: list):
    salaries = salaries.sort()
    people = people.sort()
    return people, salaries
