# Mastermind, a mini program who is going to guess a four generated color given randomly by the computer and in order 3
"""
* generate 4 colors in the 6 basics ones
* make the user guess the code
* compare the guess
* Tie the game together

"""
import random

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))

    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")   # split will use all the spaces to create elements...

        if len(guess) != 4:
            print(f"you must guess {CODE_LENGTH} colors")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break

        else:
            break
    return guess

def check_code(guess, real_code):
    # check the correct position

    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code): # the zip will create a kind of list of tuple to efficiently compare
        # the guess color and the real color
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code...")
    print("The valid colors are", *COLORS)
    code = generate_code()
    for attempts in range(1, TRIES +1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break
        print(f"Correct Position:{correct_pos} | Incorrect Position: {incorrect_pos}")

    else:
        print("You ran out of tries, the code was:", *code)


if __name__ == "__main__":
    game()









