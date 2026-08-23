import random
choice= ["rock", "paper", "scissor"]

def valid_input():
    while True:
        user_choice = input("Enter your choice(rock, paper, scissor):")
        if user_choice not in choice:
            print("please enter valid choice")
        else:
            return user_choice
        
def rock_paper_scissor():
    while True:
        comp_gen = random.choice(choice)
        user_choice = valid_input()
        if(comp_gen == user_choice):
            print("Its a tie")
            print(f"user choice -> {user_choice} and comp generated -> {comp_gen}")
        elif (comp_gen == "rock" and user_choice == "scissor") or (comp_gen == "paper" and user_choice == "rock") or (comp_gen == "scissor" and user_choice == "paper"):
            print("computer wins")
        else:
            print("user wins")
        break

while True:
    rock_paper_scissor()
    again = input("Do you want to play again? (y/n):")

    if again.lower() != "y":
        print("Thankyou for playing")
        break