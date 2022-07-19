import random

#First way of using random
    #r = random.randrange(-5, 11) #the formula is random.ranrage(start, end), when the start is not mentioned => start at 0
    #print(r)
#Second way
    #q = random.randint(-5, 11) # the same as randrange, but has 11 included
    #print(q)

choose_number = input("Please type a number: ")
guesses = 0

if choose_number.isdigit():# checks whether all the characters are digit, a number
    choose_number = int(choose_number)
    if choose_number <= 0:
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, choose_number)
# print(random_number)

while True:
    guesses += 1
    user_guess = input("Choose a number: ")
    if user_guess.isdigit(): # checks whether all the characters are digit, a number
        user_guess = int(user_guess)
    else:
        print("Please type a correct number next time")
        continue # this bring back to the top of the loop
    #break # stop the loop

    if user_guess == random_number:
        print("You got it")
        # guesses += 1
        break # when we have correctly gussed it, we have to stop. If we don't break, then the loop will continue again
    else:
        print("You got it wrong")
        # guesses += 1
        if user_guess > random_number:
            print("You should choose a smaller number")
        else:
            print("You should choose a bigger number")

print("You have guessed " + str(guesses) + " times")
    
