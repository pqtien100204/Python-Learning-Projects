import random

user_wins = 0
computer_wins = 0

option = ["rock", "paper", "scissors"]

while True: #this creates an infinite loop. You’d have to put some exit strategy in the body of the loop, to break it. It executes the while loop until break statement encounter.
    user_input = input("Type Rock/Paper/Scissors or Q for quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in option:
        continue
    
    random_number = random.randint(0, 2)
    computer_guess = option[random_number]
    print("Computer picked", computer_guess, ".")
    
    if computer_guess == 'rock' and user_input == "paper":
        print("You win")
        user_wins += 1
    elif computer_guess == 'paper' and user_input == "scissors":
        print("You win")
        user_wins += 1
    elif computer_guess == 'scissors' and user_input == "rock":
        print("You win")
        user_wins += 1
    else:
        print("You loose")
        computer_wins += 1

print("Your score is:", user_wins)
print("The computer score is:", computer_wins)
print("Goodbye!")
