
list = []
emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}


def get_user_input():
    return input("Please write rock, paper, or scissor: ").lower()


def get_user_choice():
    user_input = get_user_input()
    
    if user_input == 'rock' or user_input == 'paper' or user_input == "scissor":
        return user_input
    else:
        print("🔴 Invalid user input")
        
    


def main():
    print("=========================")
    print("App Started...")
    print("=========================")

    print(get_user_choice())






main()
