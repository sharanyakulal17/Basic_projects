import random
choice= ["rock", "paper", "scissor"]

def valid_name():
     while True:
        name = input("Enter your name:")
        try:
            name = int(name)
            print("Please enetr valid input")
            continue
        except ValueError:
            return name

def valid_input(name, count):
    while True:
        user_choice = input(f"Enter your choice(rock, paper, scissor) chance:{count}:")
        if user_choice not in choice:
            print(f"{name} please enter valid choice")
        else:
            return user_choice

def rock_paper_scissor(name, score, history):
    count = 1
    print("You have 4 chance to play")
    while count <= 4:
        comp_gen = random.choice(choice)
        user_choice = valid_input(name, count)
        count += 1

        if(comp_gen == user_choice):
            result = f"Its a tie {name}"
            print(result)
            score["tie"] += 1
        elif (comp_gen == "rock" and user_choice == "scissor") or (comp_gen == "paper" and user_choice == "rock") or (comp_gen == "scissor" and user_choice == "paper"):
            result = "computer wins"
            print(result)
            score["loses"] += 1
        else:
            result = f"{name} wins"
            print(result)
            score["wins"] += 1
        print(f"your choice -> {user_choice} and comp generated -> {comp_gen}")
        print(f"tie: {score["tie"]}, lose: {score["loses"]}, win: {score["wins"]}")
        history.append(f"user choice -> {user_choice} and comp generated -> {comp_gen} ----------> {result}")
    return name

history= []
name = valid_name()
score = {"tie":0, "loses":0, "wins":0}
while True:
    player_name = rock_paper_scissor(name, score, history)
    again = input(f"Do you want to play again? (y/n) {player_name}:")

    if again.lower() != "y":
        print(f"Thankyou for playing {player_name}")
        print("final score:")
        print(f"tie: {score["tie"]}, lose: {score["loses"]}, win: {score["wins"]}")
        print("History:")
        for entry in history:
            print(entry)
        break