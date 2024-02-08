number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != 'q':
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        guess = 'q'
    else:
        if guess > number:
            guess = input("You guessed too high! Guess again or q to quit: ")
        else:
            guess = input("You guessed too low! Guess again or q to quit: ")
