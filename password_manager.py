master_pwd = input("What is the master password? ")

def view(): # a function is a excuatable and reuseable block of code, you can add para into the ()
    with open("password.txt", "r") as f: 
        for line in f:
            data = line.rstrip() #rstrip removes blank space
            account, pwd = data.split("|") # this would convert a database seperated by | into a list ["", ""]
            print("User:", account, "| Password:", pwd)

def create():
    account = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f: # the file that you’re working with is automatically closed so that you don’t have to remember to use file.close(). after the file = open("password.txt")
        f.write(account + "|" + pwd + "\n")

while True: 
    actions = input("Would you like to view your password or create a new one?Press q to quit: ").lower()
    if actions == "q":
        quit()
        break
    elif actions == "view":
        view() # this is for calling a function.
    elif actions == "create":
        create()
    else:
        print("Please select a valid option")
        continue