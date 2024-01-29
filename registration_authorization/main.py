from controller import *

passwords = ["password",]
logins = ["master",]

while True:
    Controller.print_txt()
    user_input = input(f"Your choice: ")
    if user_input == "exit":
        break
    else:
        Controller.action(user_input)
