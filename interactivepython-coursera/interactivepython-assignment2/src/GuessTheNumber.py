__author__ = 'andrucuna'

# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


# Define globals.
secret_number = 0
guess_range = 100
number_of_guesses = 7
remaining_guesses = 7


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global guess_range
    global number_of_guesses
    global remaining_guesses
    secret_number= random.randrange(guess_range)
    if guess_range == 100:
        number_of_guesses = 7
        remaining_guesses = 7
    elif guess_range == 1000:
        number_of_guesses = 10
        remaining_guesses = 10
    print "New game. Range is from 0 to "+str(guess_range)
    print "Number of remaining guesses is "+str(remaining_guesses)
    print ""


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global guess_range
    global number_of_guesses
    global remaining_guesses
    guess_range = 100
    number_of_guesses = 7
    remaining_guesses = 7
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global guess_range
    global number_of_guesses
    global remaining_guesses
    guess_range = 1000
    number_of_guesses = 10
    remaining_guesses = 10
    new_game()


def input_guess(guess):
    # main game logic goes here
    global remaining_guesses
    remaining_guesses = remaining_guesses-1

    if remaining_guesses > 0:
        print "Guess was " + guess
        print "Number of remaining guesses is "+str(remaining_guesses)
        guess_into_number = int(guess)
        if guess_into_number<secret_number:
            print "Higher!"
        elif guess_into_number>secret_number:
            print "Lower!"
        else:
            print "Correct!"
            print ""
            new_game()
        print ""
    else:
        print "Guess was " + guess
        print "Number of remaining guesses is "+str(remaining_guesses)
        guess_into_number = int(guess)
        if guess_into_number == secret_number:
            print "Correct!"
            print ""
        else:
            print "Awww... you ran out of guesses, you lose!"
            print ""
        new_game()


# create frame
game_frame = simplegui.create_frame("Guess the number!", 220, 180)


# register event handlers for control elements and start frame
game_frame.add_button("Range is [0, 100)", range100, 180)
game_frame.add_button("Range is [0, 1000)", range1000, 180)
game_frame.add_input("Enter a guess:", input_guess, 180)
game_frame.start()


# call new_game
new_game()


# always remember to check your completed program against the grading rubric
