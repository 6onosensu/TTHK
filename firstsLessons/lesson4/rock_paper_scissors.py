import random as r

choices = ["Rock", "Paper", "Scissors"]
winning_combinations = {
    ("Rock", "Scissors"): "Rock",
    ("Scissors", "Paper"): "Scissors",
    ("Paper", "Rock"): "Paper"
}

begin = "Do you want to play rock-paper-scissors? Yes/No: "
while True:
    start = input(begin).capitalize().strip()
    if start[0] == "Y":
        try:
            txt = "Enter a number of players (1 to 2): "
            num_players = int(input(txt))
            if 1 <= num_players <= 2:
                txt = "Enter your names separated by a ',' and a space: "
                while True:
                    names = input(txt).split(", ")
                    condition1 = len(names) == num_players
                    condition2 = (num_players == 1 and len(names) == 1)
                    if condition1 or condition2:
                        break
                    else:
                        print("Please enter the correct number of names.")
                players_moves = {name: {} for name in names}
                if num_players == 1:
                    players_moves["Computer"] = {}
                print("\nThe game has begun!")
                break
            else:
                print("Please enter a number 1 or 2.")
        except ValueError:
            print("Please enter a number!")
    else:
        print("Okey, maybe another time!")
        break

if num_players == 1:
    for count in range(1, 4):
        # For player
        txt = "Enter your choice (Rock/Paper/Scissors): "
        player_choice = input(txt).capitalize()
        if player_choice in choices:
            players_moves[names[0]][count] = player_choice
        # player2 = computer
        r.shuffle(choices)
        computer_choice = choices[0]
        print(f"Computer chose {computer_choice}")
        players_moves["Computer"][count] = computer_choice
else:
    for count in range(1, 4):
        for name in names:
            txt = (
                "Player {0}, "
                "enter your choice (Rock/Paper/Scissors): "
            ).format(name)
            choice = input(txt).capitalize()
            players_moves[name][count] = choice

print("\nFinal moves:")
for player, moves in players_moves.items():
    print(f"Player {player} chose: {moves}")

player1, player2 = players_moves.keys()
count1 = 0
count2 = 0

for i in range(1, 4):
    player1_choice = players_moves[player1][i]
    player2_choice = players_moves[player2][i]
    get_value1 = winning_combinations.get((player1_choice, player2_choice))
    get_value2 = winning_combinations.get((player2_choice, player1_choice))
    if player1_choice == player2_choice:
        print(f"Round {i}: Tie")
        count1 += 1
        count2 += 1
    elif get_value1 == player1_choice:
        print(f"Round {i}: {player1} wins")
        count1 += 1
    elif get_value2 == player2_choice:
        print(f"Round {i}: {player2} wins")
        count2 += 1
    else:
        print(f"Round {i}: No clear winner")

if count1 == count2:
    winner = "Tie"
elif count1 > count2:
    winner = player1
else:
    winner = player2

print(f"\nTotal wins: {player1} - {count1}, {player2} - {count2}")
print(f"The winner is {winner}")
