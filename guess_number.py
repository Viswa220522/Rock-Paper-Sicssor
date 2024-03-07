import random
import PySimpleGUI as sg

# initialize global variables used in your code
secret_number = random.randrange(0, 100)
secret_number_range = 100
number_allowed_guess = 0

# helper function to start and restart the game
def new_game():
    """ This function starts a new game and prints out some introductions."""
    global secret_number, number_allowed_guess
    print()
    print("=== A new game starts ===")
    if secret_number_range == 100:
        number_allowed_guess = 7
        secret_number = random.randrange(0, 100)
    else:
        number_allowed_guess = 10
        secret_number = random.randrange(0, 1000)
    print("Range: [0, " + str(secret_number_range) + "]")
    print()

# define event handlers for control panel
def range100():
    """ This function gets a secret number in the range of [0, 100]."""
    global secret_number, secret_number_range
    secret_number = random.randrange(0, 100)
    secret_number_range = 100
    new_game()

def range1000():
    """ This function gets a secret number in the range of [0, 1000]."""
    global secret_number, secret_number_range
    secret_number = random.randrange(0, 1000)
    secret_number_range = 1000
    new_game()

def input_guess(guess):
    """ This function deals with the number that the player entered."""
    global number_allowed_guess
    # Using a try-except to catch wrong input
    try:
        guess = int(guess)
        end = False
        print("Your guess number is: " + str(guess))
        if guess > secret_number:
            print("Lower")
        elif guess < secret_number:
            print("Higher")
        else:
            print("Correct!")
            end = True
        number_allowed_guess -= 1
        if end:
            print("You win!")
            print()
            new_game()
        elif not end and number_allowed_guess == 0:
            print("You lose!")
            print()
            new_game()
        else:
            print("You remain " + str(number_allowed_guess) + " times to guess.")
            print()
    except Exception as e:
        print("Error:")
        print("Something wrong with the number you've entered,")
        print("please to enter an integer.")
        print()

# define layout for PySimpleGUI
layout = [
    [sg.Button('Range: [0, 100]', size=(20, 1), key='-RANGE100-'), sg.Button('Range: [0, 1000]', size=(20, 1), key='-RANGE1000-')],
    [sg.Text('Enter a number to guess:'), sg.InputText(size=(10, 1), key='-GUESS-')],
    [sg.Button('Submit', size=(10, 1))]
]

# create the window
window = sg.Window('Guess the number', layout)

# event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-RANGE100-':
        range100()
    elif event == '-RANGE1000-':
        range1000()
    elif event == 'Submit':
        input_guess(values['-GUESS-'])

window.close()
