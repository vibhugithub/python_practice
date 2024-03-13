"""
    Q6. Ask number of games played in a tournament. Ask the user number of
    games won and number of games loss. Calculate number of tie and total
    Points. (1 win= 4 points, 1 tie =2 points)
"""

user_input = int(input("enter number of games played in a tournament: "))
win_input = int(input("ENter how many games won: "))
loss_input = int(input("ENter how many games loss: "))

win = 4
tie = 2
tie_match = user_input - (win_input + loss_input)

points = win_input * win
if tie_match != 0:
    tie_point = tie_match * tie
    total_point = tie_point + points
    print(f"Total points is {total_point}")
else:
    print(f"Total points is {points}")
