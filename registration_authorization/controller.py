from functions import *

class Controller():
    def __init__(self):
        pass

    def print_txt():
        txt = """
            Sign up: signup
            Log in: login
            Change username or password: change
            Forgot your password?: forgot
            Exit the program: exit
        """
        print(txt)

    def action(self, user_input):
        params = user_input.lower().strip().split()
        action = params[0]
        parameters = ' '.join(params[1:])

        if hasattr(self, action):
            getattr(self, action)(parameters)
        else:
            print("Unknown command.")

