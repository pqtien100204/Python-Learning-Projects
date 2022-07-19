import random
from hangman_words import words
import string
print("Hello world")
def get_valid_word(words):
    word = random.choice(words)
    # lengthh = len(words)
    # random_number = random.randint(0, len(words))
    # word = words[random_number]
    while "-" or " " in word:
        word = random.choice(words)
        # random_number = random.randint(0, len(words))
        # word = words[random_number] 
    upper_word = word.upper()
    return upper_word

def hangman():
    print("Hello world")
    valid_word = random.choice(words).upper()
    letters_of_the_word = set(valid_word) # Create a set object => sets are used to store multiple items in a single variable(letters in the word).
    alphabet = set(string.ascii_uppercase) #give the uppercase letters
    used_letters = set()

    lives = 6
    while len(letters_of_the_word) > 0 and lives > 0: 

        user_letter = input("\nGuess a letter: ").upper()
        if user_letter not in alphabet:
            print("\nInvalid letter!!! Please try again")     
        elif user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in letters_of_the_word:
                letters_of_the_word.remove(user_letter)
                print('')
            else:
                lives -= 1
                print(f"You have {lives} left" )

        elif user_letter in used_letters:
            print("You have guessed that letter, choose another one!")

        # joining = " ".join(used_letters) #" ".join(["a", "bc", "d"]) => "a bd d"
        print("\nYou have used these letters:", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in valid_word]

        print("\nCurrent word:", ' '.join(word_list))

    if lives == 0:
        print("You died :)")
    else:
        print("Yeahhhh, you have guessed the word :(")

if __name__ == '__main__':
    print(hangman())