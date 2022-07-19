import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter 
        # user = input("Choose your letter (X or O): ").upper()
        # if user not in ["X", "O"]:
        #     print("Please choose a valid letter.")
        # if user == "X":
        #     computer = "O"
        # else:
        #     computer = "X"
        
    def get_next_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_next_move(self, tic_tac_toe_game):
        move_spot = random.choice(tic_tac_toe_game.available_move())
        return move_spot

class UserPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_next_move(self, tic_tac_toe_game):
        valid_square = False
        val = None
        while not valid_square:
            choice = input(f"It\'s your turn, {self.letter}. Choose a square: ")
            try:
                val = int(choice)
                if val not in tic_tac_toe_game.available_move():
                    print("That square has been chosen")
                else:
                    valid_square = True
            except:
                print("That\'s not a valid number")
                continue
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_next_move(self, tic_tac_toe_game):
        if len(tic_tac_toe_game.available_move()) == 9:
            choice = random.choice(tic_tac_toe_game.available_move())  # randomly choose a square
        else:
        # get the square based off the minimax algorithm
            choice = self.minimax(tic_tac_toe_game, self.letter)["position"]
        return choice
    

    def minimax(self, state, player):
        max_player = self.letter                                       # you're the max_player
        other_player = "O" if max_player == "X" else "X"

    # first checks if the previous move has a winner
        if state.winner == other_player:
            return {"position": None,
                    "score": 1 * (state.num_of_empt() + 1) if player == max_player else -1 * (state.num_of_empt() + 1)} #the formula is based on the minimax rule: (+1 or -1 depending who wins) * (empty space + 1{so that te result won't be a negative number(lose)})
        elif state.num_of_empt() == 0:
            return {"position": None,
                    "score": 0}

    #initialize dictionaries to make sure the computer win
        if player == max_player:
            best = {"positon": None, "score": -math.inf} # if you're the player => minimize your score => maximize the score for the computer to win
        else:
            best = {"position": None, "score": math.inf} # maximize the score 

        for single_move in state.available_move():
            #  1. make a move, try that move
            state.make_move(single_move, player) # single_move and player are the args for the make_move func(required parameters are square and letters)
            # 2. recurse using minimax to simulate the game after that move
            sim_score = self.minimax(state, other_player) #alternate player
            # 3. undo the move
            state.board[single_move] = " "
            state.winner = None
            sim_score["position"] = single_move
            # 4. update the best dict if the score the move gets is larger than the existing one in the dict
            if player == max_player:
                if sim_score["score"] > best["score"]:          # trying to maximize the max player
                    best["position"] = sim_score["position"]
                    best["score"] = sim_score["score"]
            else:
                if sim_score["score"] < best["score"]:          # and minimize the other player
                    best = sim_score
        return best