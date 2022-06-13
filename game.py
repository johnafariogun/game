import random
r,p,s=['Rock','Paper','Scissors']
game=True
while game:
    new_round=True
    user_action = input(
    f'Enter a choice R, P, S "R" for "rock", "P" for "paper", "S" for "scissors", "Q" for "Quit". Rock beats Scissors, Paper beats Rock, Scissors beats Paper: ')
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions).lower()
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    while new_round:
        if user_action.lower() == computer_action.lower():
            print(f"It's a tie!")
            new_round=True
        elif user_action.lower() == "r":
            if computer_action.lower() == "s":
                print(f"Player ({r}) : CPU ({s}), you won")
            else:
                print(f"Player ({r}) : CPU ({p}), you lost")
            new_round=False
        elif user_action.lower() == "p":
            if computer_action.lower() == "s":
                print(f"Player ({p}) : CPU ({s}), you won")
            else:
                print(f"Player ({p}) : CPU ({r}), you lost")
            new_round=False
        elif user_action.lower() == "s":
            if computer_action.lower() == "p":
                print(f"Player ({s}) : CPU ({p}), you won")
            else:
                print(f"Player ({s}) : CPU ({r}), you lost")
            new_round=False
        elif user_action.lower() == 'q':
            game=False
            new_round=False
            
        else:
            print('invalid input')
# play_again = input("Play again? (y/n): ")
# if play_again.lower() != "y":
#     game=False