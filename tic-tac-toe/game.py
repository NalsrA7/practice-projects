import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)] # creates a 3 by 3 board
        self.current_winner = None  # keep track of winner
        
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
        
    def print_board(self):
        # gets the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        # 0| 1 | 2 etc. Tells us the index where we can input our letter
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + ' |')
            
    def available_moves(self):
        # return []
        # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        return [i for i, x in enumerate(self.board) if x == " "]
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return True. if invalid, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.
        # check for rows
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # check for columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diaganols
        # we know only if the square is an even number (0, 2, 4, 6, 8)
        # then it can be in a diagonal. (our index ranges from 0 - 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal1]):
                return True
            
        # if all these checks fail
        return False
            
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
        
    letter = 'X'    # starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        # let's define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")   # just an empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                
            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'  # switches player
        
        time.sleep(0.8)
            
    if print_game:
        print("It's a tie!")
            
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)