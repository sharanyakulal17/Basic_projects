import random

def valid_name():
    while True:
        name = input("Enter your name:")
        try:
            name = int(name)
            print("Please Enter Valid name")
        except ValueError:
            return name

def valid_number(name,count):
    while True:
        user_choice = input(f"Enter a Number (count -> {count}):")
        try:
            user_choice = int(user_choice)
        except ValueError:
            print(f"{name}! Please Enter Valid Input")
            continue

        if user_choice < 1 or user_choice > 100:
            print(f"{name}! Please Enter the number b/w 1 - 100")
        else:
            return user_choice

def valid_count(name):
    while True:
        count = input("How Many chance you want to guess a number (1 -10):")
        try:
            count = int(count)
        except ValueError:
            print(f"{name} Please Enter valid number")
            continue

        if count < 1 or count > 10:
            print("Enter Count b/w 1 - 10")
            continue
        else:
            return count       
           
def play_game():
    name = valid_name()
    comp_guess = random.randint(1, 100)
    count = valid_count(name)
    while count > 0:
        user_choice = valid_number(name, count)
        if user_choice == comp_guess:
            print(f"{name} you guessed the number")
            print(f"{name} You got in {count} guess")
            print(f"{name} choice -> {user_choice} and comp_guess -> {comp_guess}")
        elif user_choice > comp_guess:
            print(f"{name}! It's too high")
        elif user_choice < comp_guess:
            print(f"{name}! It's too low")
        count = count - 1
    return name

while True:
    player_name = play_game()
    again = input(f"Do you want to guess again {player_name}? (y/Press any key):")

    if again.lower() != "y":
        print(f"Thankyou for playing {player_name}!")
        break