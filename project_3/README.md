# Rock, Paper, Scissors
A command-line rock-paper-scissors game against the computer.

## Features
- Play against the computer using random choice generation
- Input validation (rejects choices other than rock/paper/scissor)
- Name validation (rejects numbers as names)
- 4 chances per game
- Live score tracking (wins, losses, ties)
- Game history showing every round played
- Replay option after each game

## How to run
```bash
python Rock_Paper_scissor.py
```

## What I learned
- Passing multiple values (name, score, history) into a function as parameters
- Using a dictionary to track and update running scores
- Using a list to log history across multiple rounds
- Input validation with `if x not in list` vs `try/except` for numbers
- Matching function parameters correctly with the values passed in
