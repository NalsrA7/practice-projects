import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter
    
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = None
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
                
        return val
    
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # randomly choose
        else:
            # get square based off minimax algorithm
            square = self.minimax(game, self.letter)
        return square
    
    def minimax(self, state, player):
        max_player = self.letter    # yourself.
        other_player = 'O' if player == 'X' else 'X'
        
        # first, we want to check if the previous move is a winner
        # this is our base case
        # state is just the current state of the game at that moment
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_square() + 1) if other_player == max_player else -1 * (state.num_empty_square() + 1)
                    }
            
        elif not state.empty_square():  # no empty squares
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}   # each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf}    # each score should minimize
            
        for possible_move in state.available_moves():
            pass
            # step 1: make a move, try that spot
            
            # step 2: recurse using minimax to simulate a game after making that move
            
            # step 3: undo the move
            
            # step 4: update the disctionaries if necessary
        
        
            