import random 
import math

winner_list = []
picks = ["rock", "paper", "scissor"]
emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}

# return user input on how many turns to play
def get_user_input_turns():
    return input("Hou many turns would you like to play? ")

# return user input
def get_user_input():
    return input("Please pick rock, paper, or scissor: ").lower()

# if float 
def is_float(value):
    # check if a decimal
    periods = 0
    value_to_str = str(value)

    if value_to_str.isdigit():
        return False

    for period in value_to_str:
        if period == ".":
            periods += 1


    if periods > 1:
        return ("You have too many periods")
        return
  
    value_list = value_to_str.split(".")
    xx = []

    if value_list[0] == "":
        value_list[0] = "0"\
        
    if value_list[len(value_list) - 1] == "":
        value_list.remove("")
    
    for values in value_list:
        if values.isdigit():
            xx.append(True)

    if len(xx) == len(value_list):
        return True
    else:
        return False

# get user input on turns and check if valid
def get_user_turns():
    while True:
        turns = get_user_input_turns()
        turns_is_float = is_float(turns)

        if turns.isdigit():
            turns = int(turns)
            break
        elif turns_is_float:
            turns = math.ceil(float(turns))
            break
        else:
            print("🔴 Please enter a number 🔴")
    
    return turns

# get user input and check if valid
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
        print("😭 Your opponent has won this turn")
        return opponent
    if user_pick == "paper" and opponent_pick == "rock":
        print("🎉 You have won this turn")
        return user
    
    # paper
    if user_pick == "paper" and opponent_pick == "scissor":
        print("😭 Your opponent has won this turn")
        return opponent
    if user_pick == "scissor" and opponent_pick == "paper":
        print("🎉 You have won this turn")
        return user

    # scissor
    if user_pick == "scissor" and opponent_pick == "rock":
        print("😭 Your opponent has won this turn")
        return opponent
    if user_pick == "rock" and opponent_pick == "scissor":
        print("🎉 You have won this turn")
        return user
    
    # draw
    if user_pick == opponent_pick and opponent_pick == user_pick: 
        print("🏁 It's a DRAW, try again")
        return "draw"
    


def get_winner_per_turn():
    user_choice = get_user_choice()
    opponent_choice = get_random_pick()
    winner = winner_logic("user", "opponent", user_choice, opponent_choice)
    
    # winner message
    if winner == user_choice:
        print(f"{user_choice.upper()} beats {opponent_choice.upper()}, You have won 🎉")
    if winner == opponent_choice:
        print(f"{opponent_choice.upper()} beats {user_choice.upper()} You have lost 😭")

    return winner


# winner logic based on max turn plays
def get_overall_winner():
    print(winner_list)

    user = 0
    opponent = 0
    draw = 0
    winner_list_without_draw = []
    
    

    # check if it is all a draw
    for winner in winner_list:
        if winner == "draw":
            draw += 1
    
    if draw == len(winner_list):
       return ("🏁 This match was a DRAW 🏁")
    
    # loop thru winner_list and append winners to a list
    # if its a draw don't append it
    for winner in winner_list:
        if winner != "draw":
            if winner == "user":
                user += 1
            elif winner == "opponent":
                opponent += 1
            winner_list_without_draw.append(winner)

    #  check if there is an overall winner or a draw
    most_winner = int((len(winner_list_without_draw)/2) + 1) # 2
    # print(len(winner_list_without_draw))
    # print(xxx)
    # print(user, opponent)
    
    if user == opponent:
        return ("🏁 This match was a DRAW 🏁")
    if user == most_winner:
        return (f"🎉 You have WON this match with {user} out of {len(winner_list_without_draw)} wins 🎉")
    if opponent == most_winner:
        return (f"😭 You have LOST this match with {user} out of {len(winner_list_without_draw)} wins 😭")
        

 

    

    

    

    

        



# starting point for app
def main():
    turns = get_user_turns()
    current_turn = 1

    print("========================================")
    print("========== 🕹️ Match Started 🕹️ ===========")
    print("========================================")


    while current_turn <= turns:
        print("")
        print(f"============ Turn {current_turn} ============")
        winner_per_turn = get_winner_per_turn()
        winner_list.append(winner_per_turn)
        current_turn += 1

    print("")
    print("============ Match over ============")
    winner = get_overall_winner()
    print(winner)
    


main()
