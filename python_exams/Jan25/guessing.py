"""
Number Guessing Game
- Develop a program where the computer generates a random number between 1 and 100,
and the user guesses the number.
- Provide hints like "Too High" or "Too Low"
- Use a loop to allow multiple attempts.
"""
import random
    
def main():
    num = random.randrange(1, 100)
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == num:
            print("You guessed the number!")
            return
        elif guess < num:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

main()