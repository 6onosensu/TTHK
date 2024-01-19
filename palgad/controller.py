from functions import *

def print_actions(people: list, salaries: list):
    print("")
    print("Add to the list: add person salary")
    print("Delete from the list: delete person salary")
    print("The highest salary: max")
    print("The lowest salary: min")
    print("To sort ((higher-from higher/lower-from lower) salary): sort salaries higher/lower")
    print("To see each person with salary: show")
    print("Find peopele with same salary: same")
    print("Find salary by name: find 'name'")
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
        result = largest_salary(people, salaries)
        print(f"These people: {result[1]} receive the highest salary: {result[0]} Eur")
    elif action[0] == "min":
        result = smallest_salary(people, salaries)
        print(f"These people: {result[1]} receive the lowest salary: {result[0]} Eur")
    elif action[0] == "sort" and action[1] == "salaries":
        if action[2] == "lower" or action[2] == "higher":
            result = sort_salaries_with_people(people, salaries, action[2])
            people = result[0]
            salaries = result[1]
            print(people, salaries)
        else:
            print("Wrong action 3, must be 'lower' or 'higher'")
    elif action[0] == "show":
        result = person_salary(people, salaries)
    elif action[0] == "same":
        result = find_same_salary(people, salaries)
    elif action[0] == "find":
        result = find_salary_by_name(people, salaries, action[1])
        print(result[0], result[1])
