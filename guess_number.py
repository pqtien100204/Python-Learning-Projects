from audioop import maxpp
import random

def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0 
    times = 0  
    while int(guess_number) != random_number:
        guess_number = input(f"Enter a number from 1 to {x}: ")
        if int(guess_number) > random_number:
            print("Choose a lower number!")
            times += 1
            continue
        elif int(guess_number) < random_number:
            print("Choose a bigger number!")
            times += 1
            continue
    else:
        print(f"Congrats, you have guessed the correct number with {times} guess")


def computer_guess(x):
    min = 0
    max = x
    times = 0
    feedback = ""
    while feedback != "c":
        if min != max:
            com_ran = random.randint(min, max)
        else:
            com_ran = min
        
        feedback = input(f"Is {com_ran} too low (L), too high (H) or correct (C)")
        if feedback == "l":
            min = com_ran + 1
            times += 1
            continue
        elif feedback == "h":
            max = com_ran - 1
            times += 1
            continue
    
    print(f"You have guessed the correct answer {com_ran} with {times} guesses")

computer_guess(55)