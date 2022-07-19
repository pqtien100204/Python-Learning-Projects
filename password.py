import random
import string
import itertools
from unittest import result

num_of_pass = input("Number of passwords: ")
len_of_pass = input("Length of password: ")

# def check_int(value):  
#   try:
#     value_int = int(value)
#   except ValueError:
#     return 'Not an integer'

if num_of_pass.isdigit():
    num_of_pass = int(num_of_pass)
    if len_of_pass.isdigit():
        len_of_pass = int(len_of_pass)
    else: 
        print("That\'s not a number")
else:
    print("That\'s not a number")

rand_num = list(range(0, 10))
rand_lett = list(string.ascii_letters) #ascii_letters is the concatenation of ascii_uppercase and ascii_loowercase
rand_char = list(string.punctuation)

rand = list(itertools.chain(rand_num, rand_lett, rand_char))

password = []
string_of_pass = ""
for single_pass in range(num_of_pass):
    each_pass = ""
    for times in range(len_of_pass):
        each_pass += str(random.choice(rand))
    # iteration = 0
    # result_password = []
    # while iteration < len_of_pass:
    #     single_pass = random.choice(rand)
    #     iteration += 1

    password.append(each_pass)

print("These are your passwords:", password)
