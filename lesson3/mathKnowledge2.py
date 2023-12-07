import random
import math

correct_answers = 0
count_answers = 0
questions = True

difficulty = input("Select level: Level1/Level2/Level3 :  ").strip().capitalize()
questions_count = int(input("How many questions would you like to solve?: ")) 

if difficulty == "Level1":
  operators = ['+', '-']
  min_number = 0
  max_number = 20
elif difficulty == "Level2":
  operators = ['+', '-', '*', '/']
  min_number = -100
  max_number = 100
elif difficulty == "Level3":
  operators = ['+', '-', '*', '/', '**']
  min_number = -1000
  max_number = 1000
else: 
  print(f"There is no such: a {difficulty} complexity here!")

while questions:
  if count_answers == questions_count:
    questions = False
  else:
    num1 = random.randint(min_number, max_number)
    operator = random.choice(operators)
    num2 = random.randint(min_number, max_number)

  if operator == "/" and num2 == 0:
    num2 += 1
    print("here1")
  elif operator == "**" and num2 > 10 and num2 < -10:
    print("here2")
    while num2 < -10 and num2 > 10:
      if num2 > 100:
        num2 -= 100
      elif num2 > 20:
        num2 -= 10
      else: 
        num2 += 100

  question = f"{num1} {operator} {num2}"
  correct_answer = round(eval(question),2) #eval() - vq4isljaet stroku

  user_answer = float(input(f"The right answer is: {question} = "))
  round(user_answer, 2)
  

  #raznica v otvete:
  if abs(user_answer - correct_answer) < 0.01:  #abs(-5) => 5
    print("You are right!")
    correct_answers += 1
  else:
    print(f"You are wrong! The correct answer was: {correct_answer}")
  count_answers += 1
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