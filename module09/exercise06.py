import re

tc_kimlik_no = r"^[0-9]{11}$"
with open("dictionary-tur.txt", mode="rt") as dictionary:
    for word in dictionary:
        if re.fullmatch(tc_kimlik_no, word.strip()):
            print(word.strip())
