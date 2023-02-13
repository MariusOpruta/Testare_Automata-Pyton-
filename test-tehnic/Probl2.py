'''
We have the rock, scissors and paper game. Write an algorithm which solves the problem and tells
who the winner is, knowing that you have 2 players that are playing. When building the algorithm take into consideration
that is can be extended with new possibilities when choosing
Eg Rock beat scissors, scissors beat paper, paper beat hammer, hammer beats rock
'''
import random

game = ["rock", "scissors", "paper", "hammer"]
player1 = random.choice(game)
player2 = random.choice(game)



# for i in range(len(game)-1):
#     if player2 == game[i] and player1 == game[i+1]:
#         print("player2 win")
#     elif player2 == game[3] and player1 == game[0]:
#         print("player2 win")
#     elif player2 ==game[i] and player1 == game[i+2]:
#         print("player2 win")
#     elif player1 == game[i] and player2 == game[i+1]:
#         print("player1 win")
#     elif player1 == game[3] and player2 == game[0]:
#         print("player1 win")
#     elif player1 == game[i] and player2 == game[i+2]:
#         print("player1 win")
#     elif player1==player2:
#         print("both win")

print(f"alegeri: player1={player1} player2={player2} ")



# if player1 == player2:
#         print("both win")
# elif player1 == game[0] and player2 == game[1]:
#         print("player1 win")
# elif player1 == game[1] and player2 == game[2]:
#         print("player1 win")
# elif player1 == game[2] and player2 == game[3]:
#         print("player1 win")
# elif player1 == game[3] and player2 == game[0]:
#         print("player1 win")
# elif player2 == game[0] and player1 == game[1]:
#         print("player2 win")
# elif player2 == game[1] and player1 == game[2]:
#         print("player2 win")
# elif player2 == game[2] and player1 == game[3]:
#         print("player2 win")
# elif player2 == game[3] and player1 == game[0]:
#         print("player2 win")



