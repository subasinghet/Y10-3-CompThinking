import random


def number_guessing_game():
  print("Welcome to the Number Guessing Game!")
  secret_number = random.randint(1, 100)
  attempts = 0

  while True:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    attempts += 1

    if guess < secret_number:
      print("Too low! Try again.")
    elif guess > secret_number:
      print("Too high! Try again.")
    else:
      print(f"Congratulations! You guessed the secret number {secret_number}!")
      print(f"It took you {attempts} attempts.")
      break


number_guessing_game()
