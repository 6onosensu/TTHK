from functions import *

def print_actions(people: list, salaries: list):
    print("")
    print("Add to/Delete from the list: add/delete person salary")
    print("The highest/lowest salary: max/min")
    print("To sort ((higher-from higher/lower-from lower) salary): sort salaries higher/lower")
    print("To sort by name): sort byname az/za")
    print("To see each person with salary: show")
    print("Find peopele with same salary: same")
    print("Find salary by name: find 'name'")
    print("Top of the poorest and richest people: top")
    print("Filter people by salary: filter 'amount' more(by default)/less")
    print("Average salary: average") 
    print("To calculate net-salary/person`s new salary in n years: net/new")
    print("To delete person`s salary if it below average: below")
    print("To format lists (leah=>Leah and 1 to {1}): format")
    print("To rename every third person: re3p")
    print("To edit data: edit name/salary 'index'")
    print("To find name starting with a letter: fnsw 'letter'")
    print("")


def controller(people: list, salaries: list, action):
    act = action[0]
    if act == "add":
        person = action[1]
        salary = action[2]
        people, salaries = add_to_list(people, salaries, person, salary)
        person_salary(people, salaries)  
    elif act == "delete":
        person = action[1]
        salary = action[2]
        people, salaries = delete_from_list(people, salaries, person)
        person_salary(people, salaries)
    elif act == "max":
        result = largest_salary(people, salaries)
        print(f"These people: {result[1]} receive the highest salary: {result[0]} Eur")
    elif act == "min":
        result = smallest_salary(people, salaries)
        print(f"These people: {result[1]} receive the lowest salary: {result[0]} Eur")
    elif act == "sort" and action[1] == "salaries":
        if action[2] == "lower" or action[2] == "higher":
            result = sort_salaries_with_people(people, salaries, action[2])
            people = result[0]
            salaries = result[1]
            print(people, salaries)
        else:
            print("Wrong action 3, must be 'lower' or 'higher'")
    elif act == "sort" and action[1] == "byname":
        result = sort_list(people, salaries, action[2])
    elif act == "show":
        result = person_salary(people, salaries)
    elif act == "same":
        result = find_same_salary(people, salaries)
    elif act == "find":
        result = find_salary_by_name(people, salaries, action[1])
        print(result[0], result[1])
    elif act == "filter":
        result = filter_by_salary(people, salaries, action[1], action[2])
    elif act == "top":
        result = top(people, salaries)
    elif act == "average":
        result = average(people, salaries)
    elif act == "net":
        result = net_salary(people, salaries)
    elif act == "below":
        result = remove_below_average(people, salaries)
    elif act == "format":
        result = format_lists(people, salaries)
    elif act == "new":
        result = calc_new_salary(people, salaries, action[1], action[2])
    elif act == "re3p":
        result = rename_every_third_person(people)
    elif act == "edit":
        result = edit_data(people, salaries, action[1], action[2])
    elif act == "fnsw":
        find_names_starting_with(people, salaries, action[1])
