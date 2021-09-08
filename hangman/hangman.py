import random
from wordslist import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    
    lives = 6
    
    # getting the user's imput
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("\nYou have used these letters: ", ' '.join(used_letters))
        
        # what the current word is (e.g. W -  R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -= 1  # takes away a life if wrong.
                print(f"The letter {user_letter} is not in the word.")
                
        elif user_letter in used_letters:
            print('You have already submitted that letter. Please try again.')
            
        else:
            print('Invalid character. Please try again.')
    
    if lives == 0:
        print("You ran out of lives! Sorry, the word was: ", word)
    else:
        print("HOORAY! You found the word: ", word, "!")
        
hangman()
