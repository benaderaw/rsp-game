import random 

list = []
picks = ["rock", "paper", "scissor"]
emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}




def get_user_input():
    return input("Please pick rock, paper, or scissor: ").lower()


def get_user_choice():
    user_input = get_user_input()
    
    if user_input == 'rock' or user_input == 'paper' or user_input == "scissor":
        return user_input
    if user_input.isdigit():
        print("🔴 Numbers are an invalid user input, please pick rock, paper, or scissor.")
        return
    else:
        print("🔴 Invalid user input, please pick rock, paper, or scissor.")
        return

        # raise Exception("🔴 Invalid user input 🔴")


def get_random_pick():
    return random.choice(picks)


def winner_logic(user, com):
    print(f"You hae picked '{user}', and opponent has picked '{com}'")
    print(f"{emoji[user]}  vs {emoji[com]}")
    # print(f"You hae picked '{user}', and opponent has picked '{com}'")

    # rock
    if user == "rock" and com == "paper":
        return com
    if user == "paper" and com == "rock":
        return  user
    
    # paper
    if user == "paper" and com == "scissor":
        return com
    if user == "scissor" and com == "paper":
        return user

    # scissor
    if user == "scissor" and com == "rock":
        return com
    if user == "rock" and com == "scissor":
        return user
    
    # draw
    if user == com and com == user: 
        print("It's a DRAW, try again")
        main()
    


def get_winner():
    user_pick = get_user_choice()
    com_pick = None
    winner = None

    if user_pick == 'rock' or user_pick == 'paper' or user_pick == "scissor":
        com_pick = get_random_pick()
        winner = winner_logic(user_pick, com_pick)
    else:
        return

    if winner == user_pick:
        print("You have won")
    if winner == com_pick:
        print("You have lost")

    


        
    


def main():
    get_winner()



main()
