print("~~ Welcome to my computer quiz ~~")

want_to_play = input("Do you want to play games? ")

if want_to_play.lower() != "yes":
    print("Ok, thank you")
    quit()

print("Ok, let's play :)")
score = 0
answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1 #this is equal to score = score + 1
else:
    print("No problem, let's take another quiz")

answer = input("What is the biggest country in the world?")
if answer == "China":
    print("Correct!")
    score += 1
else:
    print("Let's move on")

answer = input("Who has invented the rule of relativity?")
if answer == "Albert Eistein":
    print("Correct!")
    score += 1
else: 
    print("That's the end")


print("Your Score:" + str(score)) # or print("Your Score:", score) 
print("You got " + str(score/4 * 100) +"%")