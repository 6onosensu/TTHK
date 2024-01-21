from controller import *

salaries = [1200, 2500, 2500, 750, 395, 1200, 395, 3200]
people = ["A", "Y", "B", "C", "D", "E", "A", "Leah"]

while True:
    print_actions(people, salaries)
    action = input("Your choice: ").lower().strip().split()
    if action == "quit":
        break
    else:
        controller(people, salaries, action)
