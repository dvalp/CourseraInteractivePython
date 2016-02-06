# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

upper_limit = 100

# helper function to start and restart the game

def new_game():
    # initialize global variables used in your code here
    global number_guesses
    global secret_number

    # 2 ** n >= high - low + 1
    number_guesses = int(math.ceil(math.log(upper_limit + 1, 2)))
    
    secret_number = random.randrange(0, upper_limit)
    
    print ""
    print "New game. Range is from 0 to", upper_limit
    print "Number of remaining guesses is", number_guesses
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global upper_limit
    
    upper_limit = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global upper_limit

    upper_limit = 1000 
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global number_guesses
    current_guess = int(guess)
    print ""
    print "Guess was", guess
    number_guesses -= 1
    print "Number of remaining guesses is", number_guesses
    
    if current_guess == secret_number:
        print "Correct!"
        new_game()
    elif current_guess > secret_number:
        print "Lower!"
    elif current_guess < secret_number:
        print "Higher!"

    if number_guesses == 0:
        print "You ran out of guesses. Try again!"
        new_game()
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game 
new_game()
frame.start()

