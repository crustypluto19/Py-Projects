import random


# globals 

rps = ['Rock', 'Paper', 'Scissors']
wins = 0
losses = 0
 

def turn(wins, losses, turns):
    while True:
        print("""
        0. Rock
        1. Paper
        2. Scissors
        """)
        if wins == turns:
                print("You have won the game! Congrats!")
                break

        elif losses == turns:
                print("You have lost the game! Better luck next time!")
                break

        else: 
            player_choice = int(input("Enter a number corresponding to your choice! "))
            comp_choice = random.choice(range(len(rps)))

            if player_choice in range(0, 3):
                print(f"You have chosen {rps[player_choice]}!")

                if comp_choice == player_choice: # tie
                    print(f"{rps[player_choice]} vs {rps[comp_choice]}, tie!")
                    print(f"Won: {wins}")
                    print(f"Lost: {losses}")
                
                else:
                    if player_choice == 0: # player picks rock

                        if comp_choice == 1: # comp picks paper
                            print(f"{rps[player_choice]} vs {rps[comp_choice]}, Computer won!")
                            losses += 1
                            print(f"Lost: {losses}")

                        else: # comp picks scissors
                            print(f"{rps[player_choice]} vs {rps[comp_choice]}, You won!")
                            wins += 1
                            print(f"Won: {wins}")
                        
                    elif player_choice == 1: # player picks paper

                        if comp_choice == 2: # comp picks scissors
                            print(f"{rps[player_choice]} vs {rps[comp_choice]}, Computer won!")
                            losses += 1
                            print(f"Lost: {losses}")
                        
                        else: # comp picks rock
                            print(f"{rps[player_choice]} vs {rps[comp_choice]}, You won!")
                            wins += 1
                            print(f"Won: {wins}")

                    else: # player picks scissors

                        if comp_choice == 0: # comp picks rock
                            print(f"{rps[player_choice]} vs {rps[comp_choice]}, Computer won!")
                            losses += 1
                            print(f"Lost: {losses}")
                        
                        else: # comp picks paper
                            print(f"{rps[player_choice]} vs {rps[comp_choice]}, You won!")
                            wins += 1
                            print(f"Won: {wins}")

            else:
                print("Pick a number from 0 to 2")    


def main():
    print("Welcome! Let's play rock paper scissors!")
    turns =  int(input("Times played till win: "))
    turn(wins, losses, turns)


if __name__ == "__main__":
    main()