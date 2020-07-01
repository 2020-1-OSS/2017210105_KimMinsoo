# list of play options
play = ["Rock", "Paper", "Scissors"]

#st of messages
messages = ["Tie!", "You win!", "You lose!"]
computer = "Rock"
print('Computer: {}'.format(computer))

# get the user input
player = "Paper"
print('Player: {}'.format(player))

# tie
if player == computer:
        print(messages[0])

# rock
elif player == "Rock":
    if computer == "Scissors":
        print(messages[1])
    else:
        print(messages[2])

elif player == "Paper":
    if computer == "Rock":
        print(messages[1])
    else:
        print(messages[2])

elif player == "Scissors":
    if computer == "Paper":
        print(messages[1])
    else:
        print(messages[2])

