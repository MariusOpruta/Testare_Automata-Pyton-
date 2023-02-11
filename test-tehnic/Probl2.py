'''
We have the rock, scissors and paper game. Write an algorithm which solves the problem and tells
who the winner is, knowing that you have 2 players that are playing. When building the algorithm take into consideration
that is can be extended with new possibilities when choosing
Eg Rock beat scissors, scissors beat paper, paper beat hammer, hammer beats rock
'''
import random

game = ["rock","scissors","paper"]
player1 = random.choice(game)
player2 = random.choice(game)

if player2==player1:
    print("both wins")
elif player2 == game[0] and player1 == game[1]:
    print("player2 win")
elif player2 == game[1] and player1 == game[2]:
    print("player2 win")
elif player2 == game[2] and player1 == game[0]:
    print("player2 win")
elif player1 == game[0] and player2 == game[1]:
    print("player1 win")
elif player1 == game[1] and player2 == game[2]:
    print("player1 win")
elif player1 == game[2] and player2 == game[0]:
    print("player1 win")

print(f"alegeri: player1={player1} player2={player2} ")