"""
 This program is a dice rolling game. The user and other player rolls a dice.
 Your original roll is either subtracted, divided, floor division,
 or squared depending on the users choice. The results are judged by who
 has the largest number after the initial roll and the math applied. Winner
 of the round gets two points, the loser gets no points, and a tie gives no
 points as well. Either roll again or exit the game.

 Sources: w3schools.com, stackoverflow.com
"""
__author__ = "George Stephen"

import random


def main():
    """This is the start of the program, from here the program is sent
    around to different functions to complete the game cycle"""
    intro()


def intro():
    """
    This function Introduces the Player to the game and gets user input
    for a Player Name
    """

    player1_score = 0
    player2_score = 0

    # Introduction/greeting
    player1 = input("Welcome to Dice Game!\n" + "Please type your name: ")
    # end="" Used Here
    print("Hello ", player1, sep="")
    randomNum = random.randint(1, 20)
    # * and % are used to have a variety of different player names
    randomNum = randomNum * 3 % 2
    if randomNum >= 1:  # RELATIONAL OPERATORS ' >= '
        player2 = "Pike"
    elif randomNum <= 0:  # RELATION OPERATORS '< '
        player2 = "Jimmy"
    else:
        player2 = "Zach"
    print("Let's get started! " + player1, player2, sep=" VS ")  # sep="" and
    # "+" used with string
    start_game(player1, player2, player1_score, player2_score)


def start_game(player1, player2, player1_score, player2_score):
    """
    This function allows the user to input how many sides of the dice
    they would like to roll and what operator they would like to use.


    """
    operators = None
    try:
        sides_of_dice = int(
            input("How many sides of the dice would you like to "
                  "roll? (6 - 20) "))
        if sides_of_dice < 6 or sides_of_dice > 20:
            print("Please enter a number between 6 and 20")
            start_game(player1, player2, player1_score, player2_score)
        else:
            operators = input("Please choose an operator (**, /, -,//)")
        if operators == '**' or operators == '/' or operators == '-' or \
                operators == '//':
            roll_dice(sides_of_dice, operators, player1, player2,
                      player1_score, player2_score)
        else:
            print("Please enter an operator given")
            start_game(player1, player2, player1_score, player2_score)
    except RuntimeError:
        print("An exception occurred")
        start_game(player1, player2, player1_score, player2_score)
    except ValueError:
        print("An exception occurred")
        start_game(player1, player2, player1_score, player2_score)


def roll_dice(sides_of_dice, operators, player1, player2, player1_score,
              player2_score):
    """
    This function rolls the dice for both the user and opponent.The
    original roll total is put into an equation based on what operator you
    chose.
    """
    player1_roll = None
    player2_roll = None

    for x in range(1):
        player1_roll = random.randint(1, sides_of_dice)
        player2_roll = random.randint(1, sides_of_dice)
    print("Player 1 Original Roll: ", player1_roll)
    print("Player 2 Original Roll: ", player2_roll)
    if operators == "//":  # RELATIONAL OPERATORS ' == '
        # // operators are used with players rolls
        player1_roll = player1_roll // 40 // 2 + 5
        player2_roll = player2_roll // 40 // 2 + 5
        print("Player 1 roll after operator is applied: ", player1_roll)
        print("Player 2 roll after operator is applied: ", player2_roll)
    elif operators == "**":
        # ** operators are used with players rolls
        player1_roll = player1_roll ** 40 // 2 + 5
        player2_roll = player2_roll ** 40 // 2 + 5
        print("Player 1 roll after operator is applied: ", player1_roll)
        print("Player 2 roll after operator is applied: ", player2_roll)
    elif operators == "-":
        # - operators are used with players rolls
        player1_roll = player1_roll - 40 // 2 + 5
        player2_roll = player2_roll - 40 // 2 + 5
        print("Player 1 roll after operator is applied: ", player1_roll)
        print("Player 2 roll after operator is applied: ", player2_roll)
    elif operators == "/":
        # / operators are used with players rolls
        player1_roll = player1_roll / 40 // 2 + 5
        player2_roll = player2_roll / 40 // 2 + 5
        print("Player 1 roll after operator is applied: ", player1_roll)
        print("Player 2 roll after operator is applied: ", player2_roll)

    determine_winner(player1, player2, player1_roll, player2_roll,
                     player1_score, player2_score)


def determine_winner(player1, player2, player1_roll, player2_roll,
                     player1_score, player2_score):
    """
    This function checks who won the round!
    """
    if player1_roll > player2_roll:
        player1_score += 2
        hits_ten(player1, player2, player1_score, player2_score, player1_roll,
                 player2_roll)
        print((player1 + " Wins!!!\n") * 5, "Player1 Score: ", player1_score,
              "\nPlayer2 Score: ", player2_score)
        restart(player1, player2, player1_score, player2_score,
                player1_roll, player2_roll)

    elif player2_roll > player1_roll:
        player2_score += 2
        hits_ten(player1, player2, player1_score, player2_score, player1_roll,
                 player2_roll)
        print((player2 + " Wins!!!\n") * 5, "Player1 Score: ", player1_score,
              "\nPlayer2 Score: ", player2_score)
        restart(player1, player2, player1_score, player2_score,
                player1_roll, player2_roll)

    elif player1_roll == player2_roll:
        print("Its a Tie!!!\n" * 5)
        print("Nobody gets a point\n", "Player1 Score: ", player1_score,
              "\nPlayer2 Score: ", player2_score)
        restart(player1, player2, player1_score, player2_score,
                player1_roll, player2_roll)


def hits_ten(player1, player2, player1_score, player2_score, player1_roll,
             player2_roll):
    """
    This function checks both players scores to see who hits ten first.
    First to ten wins.
    """
    if player1_score == 10 and player2_score == 0:
        print("PERFECT!")
        print("Player 1 Score: ", player1_score, "\nPlayer 2 Score: ",
              player2_score)
        x = 5
        # not is used
        if not (x > 5):
            restart(player1, player2, player1_score, player2_score,
                    player1_roll,
                    player2_roll)

    elif player2_score == 10 and player1_score == 0:
        print("Dude, you suck")
        print("Try again")
        restart(player1, player2, player1_score, player2_score, player1_roll,
                player2_roll)


def restart(player1, player2, player1_score, player2_score, player1_roll,
            player2_roll):
    """
    This function is used to restart the game.
    """
    restart_game = str(input("Roll again? Y/N"))
    if restart_game == "Y":
        start_game(player1, player2, player1_score, player2_score)
    elif restart_game == "N":
        exit()
    else:
        print("Please type Y or N to continue.")
        restart(player1, player2, player1_score, player2_score, player1_roll,
                player2_roll)


main()
