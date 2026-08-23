def valid_name():
    while True:
        name = input("Enter your name:")
        try:
            name = int(name)
            print("Please Enter Valid input")
            continue
        except ValueError:
            return name

def valid_num(name):
    while True:
        num = input("Enter a number:")
        try:
            num = int(num)
            return num
        except ValueError:
            print(f"{name} Please Enter Valid Choice")
            continue
def valid_choice(name):
    while True:
        choice = input(f"Enter your choice, {name}:")
        try:
            choice = int(choice)
        except ValueError:
            print(f"{name} Please Enter Valid Choice")
            continue

        if choice < 1 or choice > 7:
            print(f"{name} Please Enter Choice Between 1  7")
        else:
            return choice

def simple_cal(history):
    name = valid_name()
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. modulus")
        print("6. power")
        print("7. square")
        operators = {1:"+", 2:"-", 3:"*", 4:"/", 5:"%", 6:"**", 7:"**2"}

        choice = valid_choice(name)
        a = valid_num(name)
        if choice == 7:
            b = 2
        else:
            b = valid_num(name)

        if choice == 1:
            result =  a + b
            print(result)
        elif choice == 2:
            result =  a - b
            print(result)
        elif choice == 3:
            result =  a * b
            print(result)
        elif choice == 4:
            if b == 0:
                print("cannot divide by 0")
            else:
                result = a / b
                print(result)
        elif choice == 5:
            if b == 0:
                print("cannot divide by 0")
            else:
                result = a % b
                print(result)
        elif choice == 6:
            result = a ** b
            print(result)
        elif choice == 7:
            result = a ** 2
            print(result)
        history.append(f"choice {choice} -------------> {a} {operators[choice]} {b} -> {result}")
        break
    return name

history = []
while True:
    name = simple_cal(history)
    again = input(f"{name} Do you want to calculate again? (y/n):")

    if again.lower() != "y":
        print(f"Thankyou {name}")
        print("Calculation history")
        for entry in history:
            print(entry)
        break
