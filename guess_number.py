number = 10
num_guesses = 3

print("I'm thinking of a number...")
guess = int(input(f"What number am I thinking of? (Amount of guesses left {num_guesses}) "))

while guess != 'q':
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        guess = 'q'
    else:
        num_guesses -= 1
        if num_guesses == 0:
            break
        else:
            if guess > number:
                guess = input(f"You guessed too high! Guess again or q to quit (Amount of guesses left {num_guesses}): ")
            else:
                guess = input(f"You guessed too low! Guess again or q to quit (Amount of guesses left {num_guesses}): ")
        
