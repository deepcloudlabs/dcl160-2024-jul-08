def evaluate_move(guess: int, secret: int) -> tuple[str, int, int]:
    guessAsStr = str(guess)
    secretAsStr = str(secret)
    perfect_match = 0
    partial_match = 0
    for i in range(len(guessAsStr)):
        g = guessAsStr[i]
        for j in range(len(secretAsStr)):
            s = secretAsStr[j]
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


print(evaluate_move(456, 549))
print(evaluate_move(574, 549))
