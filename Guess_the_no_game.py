import random

number = random.randint(1, 100)

# guess = int(input("Guess the number (between 1 and 100): "))
# if guess == number:
#     print("Congratulations! You guessed the number.")
# elif guess < number:
#     print("Too low. Try again.")
# else:
#     print("Too high. Try again.")

# while guess != number:
#     guess = int(input("Guess the number (between 1 and 100): "))
#     if guess == number:
#         print("Congratulations! You guessed the number.")
#     elif guess < number:
#         print("Too low. Try again.")
#     else:
#         print("Too high. Try again.")


# guesses_left = 5
# while guess != number and guesses_left > 0:
#     guess = int(input("Guess the number (between 1 and 100): "))
#     guesses_left -= 1
#     if guess == number:
#         print("Congratulations! You guessed the number.")
#     elif guess < number:
#         print("Too low. Guesses left:", guesses_left)
#     else:
#         print("Too high. Guesses left:", guesses_left)
# if guesses_left == 0:
#     print("Sorry, you ran out of guesses. The number was", number)





def guess_the_number():
    number = random.randint(1, 100)
    guesses_left = 5
    while guesses_left > 0:
        guess = int(input("Guess the number (between 1 and 100): "))
        guesses_left -= 1
        if guess == number:
            print("Congratulations! You guessed the number.")
            return
        elif guess < number:
            print("Too low. Guesses left:", guesses_left)
        else:
            print("Too high. Guesses left:", guesses_left)
    print("Sorry, you ran out of guesses. The number was", number)

guess_the_number()