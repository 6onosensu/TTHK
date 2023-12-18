import random as r

game = False
choices = ["rock", "paper", "scissors"]
players = []
player = {1:[], 2:[], 3:[]}
player2 = {1:[], 2:[], 3:[]}


while True:
  start = input("Do you want to play rock-paper-scissors? Yes/No: ").capitalize().strip()
  if start[0] == "Y":
    try:
      num_players = int(input("Enter a number of players (1 to 2): "))
      if 1 <= num_players <= 2:
        print("The game has begun!")
        break
      else:
        print("Please enter a number 1 or 2.")
    except ValueError:
      print("Please enter a number!")
  else:
    print("Okey, maybe another time!")
    break

if num_players == 1:
  for count in range(4):
    #For player
    player_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
    for move in player:
      for key, value in move:
        if key == count:
          value.append(player_choice)

    #player2 = computer
    r.shuffle(choices)
    computer_choice = choices[0]
    for move in player2:
      for key, value in move:
        if key == count:
          value.append(computer_choice)
          print(f"Computer chose {computer_choice}")
else:
  players_name = input("Enter your names separated by a ',' and a space.").split(", ")
  







