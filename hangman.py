#Hangman Game
#Import Timer for Time
import time


#Steps
#Set Timer

#Ask for name of user using input method
name= input("Enter your first name: ")
print ("Hello, " + name, "Time to play the hangman game!")


time.sleep(1) #wait for 1 second
print("Happy guessing...")


time.sleep(0.5) #wait for half a second

#select a word and ask a user to start guessing the characters in it
word = ("Coded")

guesses = ''
#define the number of attempts the user can take

turns = 10


#use while loop to repeatedly ask the user to guess character until the attempts are exhausted
while turns > 0:

#conditionals, if the user is able to guess all the characters of the word within the max number of attempts, they win the game
# make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

        # see if the character is in the players guess
        if char in guesses:

            # print then out the character
            print(char, end=""),

        else:

            # if not found, print a dash
            print("_", end=""),

            # and increase the failed counter with one
            failed += 1

            # if failed is equal to zero

    # print You Won
    if failed == 0:
        print(" You won")
        # exit the script
        break
        # ask the user go guess a character
    guess = input("guess a character:")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

        # turns counter decreases with 1 (now 9)
        turns -= 1

        # print wrong
        print("Wrong")

        # how many turns are left
        print("You have", + turns, 'more guesses')

        # if the turns are equal to zero
        if turns == 0:
            # print "You Lose"
            print("You Lose")

    #otherwise they lose