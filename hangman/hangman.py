import random
import string
from words import word_list

tries = 6
guessed = False
guessed_char = []

def get_Word():
    word = random.choice(word_list).upper()
    return word

 
def start(word, tries, guessed, guessed_char):
    print(len(word) * "_ ")
    print("Start guessing!")
    print(f"Attempts: {tries}")
    word_as_list = list(word)
    progress = []
    for i in range(len(word_as_list)):
        progress.insert(i, "_ ")
    # print(word_as_list)

    while guessed == False:
        guess = input("Which alphabet could possibly be in this word? ").upper()
        if len(guess) == 1 and guess.isalpha():
            #if the char is not yet guessed already
            if guessed_char.count(guess) == 0:
                if guess in word_as_list:
                    print(f"{guess} is in the word!")
                    guessed_char.append(guess)
                    #iterates through word
                    counter = 0
                    for char in word_as_list:
                        if guess == char:
                            progress.pop(counter)
                            progress.insert(counter, char)
                            counter += 1
                        else:
                            counter += 1
                    print(*progress, sep=" ")
                    if word_as_list == progress:
                        guessed = True
                else:
                    print(f"{guess} not in word")
                    guessed_char.append(guess)
                    if tries > 0:
                        tries -= 1
                        drawHangman(tries)
                        print(f"Attempts remaining: {tries}")
                        if tries ==  0:
                            print(f"Game over, the word is {word}! Better luck next time!")
                            return 1
            else: 
                print("Word already guessed")
        else:
            print("Please type in only a character!")
    print("Well done! You have guessed the word successfully!")
                

def drawHangman(tries):
    stages = [  # 0
                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |     / \\
                   -
                """,
                # 1
                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |     / 
                   -
                """,
                # 2
                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |      
                   -
                """,
                # 3
                """
                   --------
                   |      |
                   |      O
                   |     /|
                   |      |
                   |     
                   -
                """,
                # 4
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # 5
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # 6
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    print(stages[tries])

def main():
    print("Hangman")
    drawHangman(tries)
    start(get_Word(), tries, guessed, guessed_char)


if __name__ == "__main__":
    main()
