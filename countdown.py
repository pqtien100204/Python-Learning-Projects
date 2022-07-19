import time

# amount_of_time = input("Enter the time in seconds: ")
# i = amount_of_time
# horizon = []
# for i in range(int(amount_of_time), -1, -1):
#     horizon.append(i)
#     i -= 1
# print(horizon)

t = int(input("Enter the time in seconds: "))
def countdown(t):
    while t:
        mins, secs = divmod(t, 60) # return the pairs of quotient and remainder of the pairs of given values
        #The format() method formats the specified value(s) and insert them inside the string's placeholder.
        countdowner = '{:02d}:{:02d}'.format(mins, secs) #formats an integer (d) to a field of minimum width 2 (2), with zero-padding on the left
        # "\r" is an escape character(keep replacing your characters one by one until it takes all the contents left in that string ). \n is also an escape character(creates a new line)
        print(countdowner, end="\r")
        time.sleep(1)
        t -= 1

countdown(t)
time.sleep(5) # suspends 5 more minutes and then print !!!Ringggg
print("!!!Ringggg Ringgg Ringgg!!!")
        
