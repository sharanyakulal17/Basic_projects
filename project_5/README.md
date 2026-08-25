# Mad Libs Generator
A command-line Mad Libs story generator that builds a random short story from user-submitted words.

## Features
- Collects an adjective, noun, verb, place, and animal from the user
- Randomly picks one of multiple story templates each time
- Input validation (rejects numbers as words)
- Personalized prompts using the user's name
- Story history — shows every story created in the session
- Create another story option

## How to run
```bash
python mad_libs_generator.py
```

## What I learned
- Using `random.choice()` to select between multiple pre-written templates
- Passing extra context (word type) into a reusable validation function
- Avoiding unreachable code after a `return` statement
- Building and displaying history across multiple rounds
