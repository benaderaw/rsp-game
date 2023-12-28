import random 

PLAY_TO = 5

winner_list = []
picks = ["rock", "paper", "scissor"]
emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}


# return user input
def get_user_input():
    return input("Please pick rock, paper, or scissor: ").lower()

# get user input and check it
def get_user_choice():
    while True:
        user_input = get_user_input()

        if user_input == 'rock' or user_input == 'paper' or user_input == "scissor":
            break
        elif user_input.isdigit():
            print("🔴 Numbers are an invalid input, please pick rock, paper, or scissor. 🔴")
        else:
            print("🔴 Invalid string input, please pick rock, paper, or scissor. 🔴")
    
    return user_input
 
# get randomly generated pick
def get_random_pick():
    return random.choice(picks)

# winner logic
def winner_logic(user, opponent, user_pick, opponent_pick):
    print(f"You have picked {user_pick.upper()}, and your opponent has picked {opponent_pick.upper()}")
    print(f"{emoji[user_pick]} vs {emoji[opponent_pick]}")

    # rock
    if user_pick == "rock" and opponent_pick == "paper":
        return opponent
    if user_pick == "paper" and opponent_pick == "rock":
        return user
    
    # paper
    if user_pick == "paper" and opponent_pick == "scissor":
        return opponent
    if user_pick == "scissor" and opponent_pick == "paper":
        return user

    # scissor
    if user_pick == "scissor" and opponent_pick == "rock":
        return opponent
    if user_pick == "rock" and opponent_pick == "scissor":
        return user
    
    # draw
    if user_pick == opponent_pick and opponent_pick == user_pick: 
        print("🏁 It's a DRAW, try again")
        return "draw"
    


def get_winner():
    user_choice = get_user_choice()
    opponent_choice = get_random_pick()
    winner = winner_logic("user", "opponent", user_choice, opponent_choice)
    
    # winner message
    if winner == user_choice:
        print(f"{user_choice.upper()} beats {opponent_choice.upper()}, You have won 🎉")
    if winner == opponent_choice:
        print(f"{opponent_choice.upper()} beats {user_choice.upper()} You have lost 😭")

    return winner

# starting point for app
def main():
    turn = 1
    
    while turn <= 5:
        print(f"============ Turn {turn} ============")
        winner = get_winner()
        winner_list.append(winner)
        turn += 1


main()
