import random

def guess(x):
    """
    Takes in an argument of the higher bound for the guessing range.
    Function stores a random integer within that range and user must
    guess the number through a series of inputs until correct.
    """
    rand_num = random.randint(1, x)
    response = 0    #we do this to make sure response is never accidentally correct from the get-go.
    
    while response != rand_num:
        response = int(input(f"Make your guess between 1 and {x}: "))
        if response > rand_num:
            print("Your guess was too high. Try going lower.")
        elif response < rand_num:
            print("Your guess was too low. Try going higher.")
            
    print("CONGRATS! You guess the number correctly!")
            

def computer_guess(x):
    """
    Takes in an argument of the higher bound for the guessing range
    and the function 'guesses' an integer within that range until the
    user gives feedback that it has guessed correctly
    """
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low    # could also be high because low == high here.
            
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f"Yay! The computer guessed your number, {guess}, correctly!")
    
    
#guess(10)    
#computer_guess(10)