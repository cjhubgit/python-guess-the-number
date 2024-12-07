# python-guess-the-number
# Guess the Number Game

A beginner Python project where the user guesses a randomly chosen number between 1 and 100. Includes a CI/CD pipeline using GitHub Actions.

## How to Play
- Run the game:
  ```bash
  python guess_the_number.py

Enter guesses until you find the correct number.

CI/CD Pipeline

The project includes a GitHub Actions workflow to test the game in test_mode.

How to Test

Run the game in test mode:
(bash) python -c "from guess_the_number import guess_the_number; guess_the_number(test_mode=True)"

(bash)
git add README.md
git commit -m "Add README file"
git push origin main
