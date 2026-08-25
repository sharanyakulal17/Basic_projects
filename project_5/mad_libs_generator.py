import random

def valid_name():
    while True:
        name = input("Enter your name:")
        try:
            name = int(name)
            print("please Enter valid name")
            continue
        except ValueError:
            return name

def valid_input(name, word_type):
    while True:
        word = input(f"{name} Enter a {word_type}:")
        try:
            word = int(word)
            print(f"{name} Please Enter valid input")
            continue
        except ValueError:
            return word

def story_time(name, history):
    while True:
        print("A Zoo Story:")
        adjective = valid_input(name, "adjective")
        noun = valid_input(name, "noun")
        verb = valid_input(name, "verb")
        place = valid_input(name, "place")
        animal = valid_input(name, "animal")
        templates = [
            f"Yesterday I went to {place} and I saw a {adjective} {animal}. It was {verb} with a {noun} stick.",
            f"In a land far away, a {adjective} {animal} lived in {place}. One day it {verb} and found a magical {noun}.",
            f"Breaking news from {place}: a {adjective} {animal} was seen {verb} while holding a {noun}!"
        ]
        
        story = random.choice(templates)
        print("your story is:")
        print(story) 
        history.append(story)
        return name
        

history = []
name = valid_name()
while True:
    name= story_time(name, history)
    again = input(f"do you want to create story again {name}? (y/n):")

    if again.lower() != "y":
        print(f"Thankyou {name}")
        for story in history:
            print(story)
        break