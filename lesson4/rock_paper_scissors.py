import random as r

choices = ["Rock", "Paper", "Scissors"]
player = {1: [], 2: [], 3: []}
player2 = {1: [], 2: [], 3: []}


while True:
    txt = (
        "Do you want to play rock-paper-scissors? "
        "Yes/No: "
    )
    start = input(txt).capitalize().strip()
    if start[0] == "Y":
        try:
            txt = "Enter a number of players (1 to 2): "
            num_players = int(input(txt))
            if 1 <= num_players <= 2:
                txt = "Enter your names separated by a ',' and a space: "
                names = input(txt).split(", ")
                players_moves = {name: {} for name in names}
                print(names, players_moves)
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
    players_moves["Computer"] = {}
    for count in range(1, 4):
        # For player
        txt = "Enter your choice (Rock/Paper/Scissors): "
        player_choice = input(txt).capitalize()
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
                "Player {0},"
                "enter your choice (Rock/Paper/Scissors): "
            ).format(name)
            choice = input(txt).capitalize()
            players_moves[name][count] = choice

print("Final moves:")
for player, moves in players_moves.items():
    print(f"{player}: {moves}")
