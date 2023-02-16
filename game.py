
import random

# constant = variable that doesn't change

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():   # function = reusable block of codes that user can call multiple times
    code = []
    # "_" is like placeholder. we can use it for the i or x when u don't care what iteration u on
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code


def guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ")   # split("") = "G G G G" -> ["G","G","G","G"]

        if len(guess) != CODE_LENGTH:
            print(f"you must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in guess:
                print(f"Invalid color: {color}, Try again.")
                break

        else:
            break

    return guess

# step1 : determine the guessing color matches the real code color.
# step2 : determine how many colors are in the right position.
# step3 : determines colors that are in the code but that are not in the correct position.


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    """
    zip = combine elements in the same position into tuples then give a list of that
    
    guess = ["G", "R"]
    real = ["W", "Y"]
    [("G", "W"), ("R", "Y")]
    """

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to the mastermind, you have {TRIES} to guess the code....")
    print("The valid colors are", COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"you guess the code in {attempts} tries!!!")
            break

        print(f"Correct positions: {correct_pos}  |  Incorrect positions: {incorrect_pos}")

    else:
        print("You ran out of tries, the code was: ", code)


if __name__ == "__main__":
    game()