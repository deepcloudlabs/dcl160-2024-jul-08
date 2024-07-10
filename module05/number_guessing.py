"""
    [1-100]
    max move: 7
    secret: 74
    guess: 50 -> pick a large number
    guess: 75 -> pick a small number
    guess: 63 -> pick a large number
"""
import random


def create_secret(min_value: int = 1, max_value: int = 100) -> int:
    return random.randint(min_value, max_value)


state = {
    "secret": 0,
    "max_moves": 7,
    "moves": []
}

state["secret"] = create_secret(1, 100)


def create_move(guess: int, secret: int) -> tuple[int, str]:
    if guess < secret:
        return guess, "Pick a larger number"
    return guess, "Pick a smaller number"


def print_state(state):
    for move in state["moves"]:
        print(move)


def game_application() -> None:
    global state
    while len(state["moves"]) < state["max_moves"]:
        guess = int(input("Enter your guess: ").strip())
        if guess == state["secret"]:
            print("You won!")
            return
        move = create_move(guess, state["secret"])
        state["moves"].append(move)
        print_state(state)
    print(f"You lost! Secret was: {state['secret']}")


game_application()
