import random
import re
from time import sleep


def roll():
    number = random.randint(1,6)
    print(f"Your number is {number}")


def main():
    print("Welcome!")
    while True:
        ans = input("Roll a dice?")
        if re.search("^y(es)?$", ans, re.IGNORECASE):
            print("Rolling dice...")
            sleep(0.5)
            roll()

        elif re.search("^no?$", ans, re.IGNORECASE):
            print("See you next time!")
            break

        else:
            print("Punten?")


if __name__ == "__main__":
    main()