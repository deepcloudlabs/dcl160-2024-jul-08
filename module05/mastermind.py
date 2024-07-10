"""
level: 3
live: 3
maxMoves: 10
secret: 549
player -> 123
          No match
          456
          -2
          574
          +1-1
          ...
          549
level: 4
secret: 3615
...
level:10
"""
import random


def create_digit(digit_min: int = 0, digit_max: int = 9):
    return random.randint(digit_min, digit_max)


def create_secret(level: int = 3) -> int:
    """
    creates secret for the game called mastermind
    :param level: level of the game
    :return: a secret of the game
    """
    digits = [create_digit(1, 9)]
    while len(digits) < level:
        digit = create_digit(0, 9)
        if digit not in digits:
            digits.append(digit)
    number = 0
    for digit in digits:
        number = 10 * number + digit
    return number


game_state = {
    "level": 3,
    "live": 3,
    "maxMoves": 10,
    "secret": create_secret(),
    "moves": []
}


def play(state: dict, guess: int) -> dict:
    pass


def mastermind_app():
    global game_state
    while game_state["level"] < 10:
        guess = int(input("Enter guess: ").strip())
        game_state = play(game_state, guess)
