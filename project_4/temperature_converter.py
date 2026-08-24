def valid_name():
    while True:
        name = input("Enter your name:")
        try:
            name = int(name)
            print("Please Enter valid name")
            continue
        except ValueError:
            return name

def valid_choice(name):
    while True:
        choice = input(f"Enter your choice {name}:")
        try:
            choice = int(choice)
        except ValueError:
            print(f"{name} Please Enter valid input")
            continue
        if choice < 1 or choice > 6:
            print(f"{name} Please Enter chouce between 1 - 6")
        else:
            return choice

def valid_temp(name):
    while True:
        temp = input(f"Enter a temperature {name}:")
        try:
            temp = float(temp)
            return temp
        except ValueError:
            print(f"{name} Please Enter valid input")
            continue

def temp(name):
    print("1. Celisus -------------> Fahrenhiet")
    print("2. Fahrenhiet ------------> Celisus")
    print("3. Celisus --------------> Kelvin")
    print("4. Kelvin --------------> Celisus")
    print("5. Fahenheit -----------> Kelvin")
    print("6. Kelvin ------------> Fahenheit")
    
    while True:
        choice = valid_choice(name)
        temp = valid_temp(name)

        temperature = {1:"C -> F", 2:"F -> C", 3:"C -> K", 4:"K -> C", 5:"F -> K", 6:"K -> F"}
        if (choice == 1):
            result = (temp * 9/5) + 32
            print(result)
        elif (choice == 2):
            result = (temp -32) * 5/9
            print(result)
        elif (choice ==3):
            result = (temp + 273.15)
            print(result)
        elif (choice == 4):
            result = (temp - 273.15)
            print(result)
        elif (choice == 5):
            result = (temp -32) * 5/9 + 273.15
            print(result)
        elif (choice == 6):
            result = (temp -273.15) * 9/5 + 32
            print(result)
        
        print(f"you entered: {temp} -----> converted {temperature[choice]} ------ {result}")
        history.append(f"{temp} --> {temperature[choice]} -------------- {result}")
        break
    return name

history = []
name = valid_name()
while True:
    name = temp(name)
    again = input(f"Do you want to convert again {name}? (y/n):")

    if again.lower() != "y":
        print(f"Thankyou {name}")
        print("History:")
        for entry in history:
            print(entry)
        break