import random
# George Stephen
# Description: FORTY 2 FIVE, This is a dice rolling game. Player must enter
# his/her name,
# Pick a die, then choose an operator. The players roll is either divided
# Using basic
# Division and floor division, subtraction, and apply exponents to their
# number.
# The player with the largest number wins.
# 2 points each win.
#First player to 40 points, wins
# Sources: https://www.w3schools.com/python/default.asp


def main():
    intro()


def intro():
    player2 = ""
    # Greeting and String Operator
    player1 = input(
        "Welcome to Dice Game!\n" + "Please type your name: ")
    print("Hello " + player1, end="\n")  # end="" Used Here
    randomNum = random.randint(1, 20)
    # * and % are used to have a variety of different player names
    randomNum = randomNum * 3 % 2
    # "%" and "*" Used Here
    if randomNum >= 1:  # RELATIONAL OPERATORS ' >= '
        player2 = "Isabelle"
    elif randomNum <= 0:  # RELATIONAL OPERATORS ' < '
        player2 = "Scott"
    else:
        player2 = "George"
    print("Let's get started! " + player1, player2,
          sep=" VS ")  # "sep=""" and "+" With String
    start_game(player1, player2, player1_roll=0, player2_roll=0,
               player1_score=0, player2_score=0)


def start_game(player1, player2, player1_roll, player2_roll, player1_score,
               player2_score):
    player1_roll = 0
    player2_roll = 0
    # Input Function
    sidesofdice = int(input(
        "How many sides of the dice would you like? (6 - 20)"))
    # AT LEAST ONE OF THE FOLLOWING: > >= < <=
    if sidesofdice < 6 or sidesofdice > 20:
        print("Please choose a dice between 6 and 20!")
        start_game(player1, player2, player1_roll, player2_roll)
    operators = input("Last thing, please choose an operator (**, + , -, /)")
    roll(sidesofdice, operators, player1, player2, player1_score,
         player2_score)


def roll(sidesofdice, operators, player1, player2, player1_score,
         player2_score):
    player1_roll = 0
    player2_roll = 0
    rolling = True
    # BOLLEAN OPERATORS 'WHILE'
    while rolling:
        # 'FOR ' 'IN' 'RANGE'
        for x in range(1):
            player1_roll = random.randint(1, sidesofdice)
            player2_roll = random.randint(1, sidesofdice)
        break
    # STANDARD CONDITIONAL STRUCTURES / STATEMENTS:if, if-else, if-elif,
    # if-elif-else
    if operators == "//":  # RELATIONAL OPERATORS ' == '
        # // operators are used with players rolls
        player1_roll = player1_roll // 40 // 2 + 5
        player2_roll = player2_roll // 40 // 2 + 5
    elif operators == "**":
        # ** operators are used with players rolls
        player1_roll = player1_roll ** 40 // 2 + 5
        player2_roll = player2_roll ** 40 // 2 + 5
    elif operators == "-":
        # - operators are used with players rolls
        player1_roll = player1_roll - 40 // 2 + 5
        player2_roll = player2_roll - 40 // 2 + 5
    elif operators == "/":
        # / operators are used with players rolls
        player1_roll = player1_roll / 40 // 2 + 5
        player2_roll = player2_roll / 40 // 2 + 5
    else:
        print("Please choose an operator listed above")
        roll(sidesofdice, operators, player1, player2, player1_score,
             player2_score)
    print("Player 1 Original Roll:", player1_roll)
    print("Player 2 Original Roll:", player2_roll)
    determineRoundWinner(player1_roll, player2_roll, player1_score,
                         player2_score, player1, player2)


def determineRoundWinner(player1_roll, player2_roll, player1_score,
                         player2_score, player1, player2):
    if player1_roll > player2_roll:
        player1_score += 2
        print((player1 + " Wins!!!\n") * 5 + "Player1 Score: ", player1_score,
              "\nPlayer2 Score: ", player2_score)
        restart(player1, player2, player1_score, player2_score,
                player1_roll, player2_roll)

    elif player2_roll > player1_roll:
        player2_score += 2
        print((player2 + " Wins!!!\n") * 5 + "Player1 Score: ", player1_score,
              "\nPlayer2 Score: ", player2_score)
        restart(player1, player2, player1_score, player2_score,
                player1_roll, player2_roll)

    elif player1_roll == player2_roll:
        print("Its a Tie!!!\n" * 5)
        print("Nobody gets a point\n" + "Player1 Score: ", player1_score,
              "\nPlayer2 Score: ", player2_score)
        restart(player1, player2, player1_score, player2_score,
                player1_roll, player2_roll)


def restart(player1, player2, player1_score, player2_score, player1_roll,
            player2_roll):
    restartgame = str(input("Play again? Y/N"))
    if restartgame == "Y":
        start_game(player1, player2, player1_roll, player2_roll, player1_score,
               player2_score)
    elif restartgame == "N":
        exit()
    else:
        print("Please type Y or N to continue.")
        restart(player1, player2, player1_score, player2_score, player1_roll,
                player2_roll)


intro()
