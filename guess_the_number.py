import random

def guess_the_number(test_mode=False):  # test_mode is included as a parameter
    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0

    if test_mode:
        # Simulate guesses for testing
        for guess in range(1, 101):
            attempts += 1
            if guess == number_to_guess:
                print(f"Test passed! Number {guess} guessed in {attempts} attempts.")
                return True
        return False
    else:
        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")


if __name__ == "__main__":
    guess_the_number()

