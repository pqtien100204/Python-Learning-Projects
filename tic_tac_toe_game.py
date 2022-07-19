from tic_tac_toe_player import UserPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.winner = None

    def print_board(self):
        for i in range(3):
            for row in list(self.board):
                row = self.board[i*3:(i+1)*3]
            print("|" + "|".join(row) + "|")

    @staticmethod
    def print_board_number():
        indexing = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in indexing:
            print("|" + "|".join(row) + "|")

    def available_move(self):
        return [inde for inde, valu in enumerate(self.board) if valu == " "] # this list show the valid, un-chosen space 
        # for inde, valu in enumerate(self.board):
        #     if valu == " ":
        #         moves.append(inde)
        #     return moves

#create function to make move
    def make_move(self, square, letter):
        if self.board[square] == str(" "): #and letter in ["X", "O"]
            self.board[square] = letter
            if self.check_for_win(square, letter):
                self.winner = letter
            return True
        else:
            return False

    def check_for_win(self, square, letter):
#if there arae 3 straight same letter in... => wins
    # 1. Check the rows:
        row_inde = square // 3                               # these 2 lines specifying the field of each row 
        row = self.board[row_inde*3 : (row_inde+1)*3]        # on the board 0:3, 3:6, 6:9
        if all(square == letter for square in row):
            return True
# if there is no win on the orw, return True and keep going to check the other cases
    
    # 2. Check the columns:
        col_inde = square % 3                                   # these 2 lines show the position of each every                                                        
        column = [self.board[col_inde+i*3] for i in range(3)]   # single space that make a column(not the already existing list like row)
        if all(square == letter for square in column):
            return True
    
    # 3. Check the diagonals:
        # check if the square move to is an even number
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in range(0,9,4)]
            #diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(square == letter for square in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in range(2,7,2)]
            #diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(square == letter for square in diagonal2):
                return True
    # If all of the above situations fail
        return False

#check whether there is any blank space left
    def empt(self):
        return " " in self.board

    def num_of_empt(self):
        #return len(self.available_move())
        return self.board.count(" ")

        
def play(game, x_player, o_player, print_game=True):
# Return the letter of the winner of the game or None if it is a tie
    if print_game:
        game.print_board_number()
    
    letter = "X"
    while game.empt():
 #check whether there is any blank space left
        if letter == "O":
            square = o_player.get_next_move(game)
        else:
            square = x_player.get_next_move(game)
#create function to make move
        if game.make_move(square, letter):
            if print_game:
                print(f"The {letter} move has been made on the {square} square")
                game.print_board() # reprint the board after having made the change
                print(" ") #empty line
#if there is a winner at this move => don't have to switch letter => end game
                if game.winner != None:
                    if print_game:
                        print(f"The winner is: {letter}")
                    return letter
#after making a move => alternate letter
            #letter = "O" if letter == "X" else "X"
            if letter == "X":
                letter = "O"
            else:
                letter = "X"# Who is the winner on the current move(once a random move has been made, whether there is any winner, if there is...)
        
            if print_game == False:
                time.sleep(0.8)
    if print_game:
        print("It\'s a tie")    
          
if __name__ == '__main__':                           # The variable __name__ for the file/module that is run will be always __main__. 
    x_score = 0
    o_score = 0                  
    ties = 0
    for i in range(1000):     
        x_player = RandomComputerPlayer('X')                     # But the __name__ variable for all other modules that are being imported 
        o_player = GeniusComputerPlayer("O")           # will be set to their module's name.
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == "X":
            x_score += 1
        elif result == "O":
            o_score += 1
        else:
            ties += 1
    print("X wins for", x_score, "times")
    print("Y wins for", o_score, "times")
    print("Ties for", ties, "times")



#board = [" " for _ in range(9)]
# for row in [board[i*3:(i+1)*3] for i in range(3)]:
#     print(row)

# for i in range(3):
#     for row in list(board):
#         row = board[i*3:(i+1)*3]
#     print("|" + "|".join(row) + "|")