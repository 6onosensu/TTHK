from functions import *

salaries = [1200, 2500, 750, 395, 1200]
people = ["A", "B", "C", "D", "E"]

while True:
    print_actions(people, salaries)
    action = input("Your choice: ").lower().strip().split()
    if action == "quit":
        break
    else:
        controller(people, salaries, action)
