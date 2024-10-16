import random

def guessing_game():
    number_to_guess = random.randint(1, 1000)
    guess = None
    attempts = 0
    max_attempts = 11

    print("I am thinking of a number between 1 and 1000.")
    
    while guess != number_to_guess and attempts < max_attempts:
        print("Take a guess, round {}: ".format(attempts + 1))
        guess = int(input("Enter number: ")) 
        attempts += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print("Good job! You guessed my number in {} guesses!".format(attempts))
    
    if guess != number_to_guess:
        print("Sorry, you did not guess the number within 11 attempts. The number was {}.".format(number_to_guess))

guessing_game()