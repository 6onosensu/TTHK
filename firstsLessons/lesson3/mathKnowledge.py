import random

difficulty = input("Select level: Level1/Level2/Level3 :  ").capitalize()
questions_count = int(input("How many questions would you like to solve?: "))

correct_answers = 0
count_answers = 0
questions = True

for _ in range(questions_count):
    if difficulty == "Level1":
        operators = ['+', '-']
        max_number = 10
    elif difficulty == "Level2":
        operators = ['+', '-', '*', '/']
        max_number = 50
    else:
        operators = ['+', '-', '*', '/', '**']
        max_number = 100

while questions:
    if count_answers == questions_count:
        questions = False
    else:
        print(count_answers, questions_count)
        num1 = random.randint(1, max_number)
        num2 = random.randint(1, max_number)
        operator = random.choice(operators)
        print(num1, num2)
        question = f"{num1} {operator} {num2}"
        correct_answer = eval(question)  # eval() - vq4isljaet stroku

        user_answer = float(input(f"The right answer is: {question} = "))

        # raznica v otvete:
        if abs(user_answer - correct_answer) < 0.01:  # abs(-5) => 5
            print("You are right!")
            correct_answers += 1
            count_answers += 1
        else:
            count_answers += 1
            print(f"You are wrong! The correct answer was: {correct_answer}")

score = (correct_answers / questions_count) * 100
if score < 60:
    grade = "Grade 2"
elif score < 75:
    grade = "Grade 3"
elif score < 90:
    grade = "Grade 4"
else:
    grade = "Grade 5"

print(f"Your result: {score:.2f}%. Your grade: {grade}")
