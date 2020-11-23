from random import randint

from art import logo, end_logo


def choose_random_number():
    return randint(1,100)


def display_text():
    '''
    Prints out the welcoming message for the game
    '''
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100')
    
def choose_difficulty():
    '''
    Has the user set the difficulty and returns the number of guesses they will have based on their choice
    '''
    number_of_guesses = 0
    user_input_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user_input_difficulty == 'easy':
        number_of_guesses = 10
        return number_of_guesses
    elif user_input_difficulty == 'hard':
        number_of_guesses = 5
        return number_of_guesses
        
def take_guess():
    '''
    Get's the users guess as an int and returns the users guess
    '''
    user_guess = int(input('Make a guess: '))
    return user_guess

def check_winner(guess, target, attempts):
    '''
        Checks the users guess against the target number and prints out if the user won the game or if the user has guessed too high or too low. 
        Returns the numbers of attempts remaining
    '''
    if guess == target:
        print(f'Your guess of {guess} is correct. You Win!')
        attempts = 0
        return attempts
    elif guess > target:
        print(f'Your guess of {guess} is too high.')
        print('Guess again')
        attempts -= 1
        return attempts
    else:
        print(f'Your guess of {guess} is too low.')
        print('Guess again')
        attempts -= 1
        return attempts
        
        
def number_guessing_game():
    '''
    Allows the user to keep guessing as long as they have attempts remaining.  When the user has found the correct number or has run out of attempts, the function ends.
    '''
    display_text()
    random_number = choose_random_number()
    attempts = choose_difficulty()
    print(f'The secret number is {random_number}')
    print(f'You have {attempts} attempts remaining to guess the number.')
    while attempts > 0:
        user_pick = take_guess()
        attempts = check_winner(user_pick, random_number, attempts)
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
        if attempts == 0 and random_number != user_pick:
            print(f"You've run out of guesses, you lose. The number was {random_number}")
        
def play_game():
    '''
    Calls the number_guess_game function and ask if the user wants to play again when the game is over
    '''
    play_game = True
    while play_game:
        number_guessing_game()     
        if input('Woudld you like to play again? y/n ').lower() == 'y':
            number_guessing_game()
        else:
            play_game = False
            print(end_logo)
    
    
play_game()
    
      
    
