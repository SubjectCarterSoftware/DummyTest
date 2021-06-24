import random

def play():
    user = input("'R' for Rock, 'P' for Paper, 'S' for scissors \n")
    computer = random.choice(['R','P','S'])
    
    if user == computer:
        return 'tie'
    
    if is_win(user, computer):
        return 'You Won!'
    
    return 'You Lost!'

def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') \
        or ( player == 'P' and opponent == 'R'):
        return True

print(play())
PendingDeprecationWarning



exit()