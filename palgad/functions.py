
def main(salaries: list, people: list):
    person_salary(salaries, people)
    print(f"People list: {p} and their salaries: {s}")
    print(f"Add to the list: add person salary")
    print(f"Delete from the list: delete person salary")
    print(f"The largest salary: max")
    palgad = input("Your choice: ").split()

    if palgad[0] == "add":
        person = palgad[1]
        salary = palgad[2]
        people, salaries = add_to_list(people, salaries, person, salary)
        person_salary(people, salaries)  
    elif palgad[0] == "delete":
        person = palgad[1]
        salary = palgad[2]
        people, salaries = delete_from_list(people, salaries, person)
        person_salary(people, salaries)
    elif palgad[0] == "max":
        maximum, names = largest(salaries, people)
        large = "largest"
        for name in names:
            print(f"This person has the larges salary: {name} and the salary is : {maximum} Eur")
    elif palgad[0] == "min":
        minimum, names = smallest(salaries, people)
        small = "smallest"
        for name in names:
            print(f"This person has the smallest salary: {name} and the salary is : {minimum} Eur")
    elif palgad[0] == "sort":
        salaries, people = sort_of_list(salaries, people)
        person_salary(salaries, people)



def add_to_list(people: list, salaries: list, person, salary):
    """
    This function adds to list your input!
    param salaries - list of salaries
    param people - list of people
    """
    salary = int(salary)
    people.append(person)
    salaries.append(salary)
    return people, salaries
 

def delete_from_list(people: list, salaries: list, person):
    for p in people:
        if p == person:
            ind = people.index(p)
            people.pop(ind)
            salaries.pop(ind)
    return people, salaries


def largest(salaries: list, people: list):
    list_of_names = []
    maximum = max(salaries)
    quantity = salaries.count(maximum)
    a = 0
    for _ in range(quantity):
        ind = salaries.index(maximum, a)
        name = people[ind]
        a += 1
        list_of_names.insert(name)
    return maximum, list_of_names  


def smallest(salaries: list, people: list):
    list_of_names = []
    minimum = min(salaries)
    quantity = salaries.count(minimum)
    a = 0
    for _ in range(quantity):
        ind = salaries.index(minimum, a)
        name = people[ind]
        a += 1
        list_of_names.insert(name)
    return minimum, list_of_names  


def person_salary(people: list, salaries: list):
    for p in people:
            for s in salaries:
                print(f"Person: {p} with salary {s}Eur")


def sort_of_list(salaries: list, people: list):
    salaries = salaries.sort()
    people = people.sort()
    return salaries, people


def the_st(st):
    