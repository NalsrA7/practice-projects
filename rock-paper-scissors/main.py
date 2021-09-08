import random
import time

def play():
    user = input("What's your choice?: \n'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p','s'])
    
    print_choices(user, computer)
    time.sleep(0.7)
    print('.')
    time.sleep(0.3)
    print('..')
    time.sleep(0.3)
    print('...')
    time.sleep(0.3)
    
    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def is_win(player, opponent):
    # rules: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

def print_choices(player, opponent):
    print(f"You picked {player}! Your opponent picked {opponent}")

print(play())