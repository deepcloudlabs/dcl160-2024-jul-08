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


def initialize_next_level(state):
    state["level"] += 1
    state["live"] += 1
    state["maxMoves"] += 2 * (state["level"] - 3)
    state["moves"] = []
    state["secret"] = create_secret(state["level"])


def initialize_level(state):
    state["live"] -= 1
    state["moves"] = []
    state["secret"] = create_secret(state["level"])


def evaluate_move(guess: int, secret: int) -> tuple[str, int, int]:
    guess_str = str(guess)
    secret_str = str(secret)
    perfect_match = 0
    partial_match = 0
    for i in range(len(guess_str)):
        g = guess_str[i]
        for j in range(len(secret_str)):
            s = secret_str[j]
            if g == s:
                if i == j:
                    perfect_match += 1
                else:
                    partial_match += 1
    if perfect_match == 0 and partial_match == 0:
        return "No match", 0, 0
    message = ""
    if partial_match > 0:
        message = f"-{partial_match}"
    if perfect_match > 0:
        message = f"{message}+{perfect_match}"
    return message, perfect_match, partial_match


def play(state: dict, guess: int) -> dict:
    if state["secret"] == guess:
        initialize_next_level(state)
    else:
        state["moves"].append(evaluate_move(guess, state["secret"]))
        if len(state["moves"]) >= state["maxMoves"]:
            initialize_level(state)
    return state


def mastermind_app():
    global game_state
    print(game_state)
    while game_state["level"] < 10:
        guess = int(input("Enter guess: ").strip())
        game_state = play(game_state, guess)
        print(game_state)


mastermind_app()
