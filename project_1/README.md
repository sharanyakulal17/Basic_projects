# Number Guessing Game
A simple command-line game where the computer picks a random number 
between 1 and 100, and the player has a limited number of attempts 
to guess it correctly.

## Features
- Random number generation
- Limited number of attempts (10)
- Input validation (rejects non-numeric input and out-of-range guesses)
- Tracks and displays how many guesses it took to win
- "Play again?" option to restart without rerunning the script
- Personalized messages using the player's name

## How to run
1. Make sure Python 3 is installed
2. Run the script:
   \`\`\`bash
   python number_guessing_game.py
   \`\`\`
3. Enter your name, then start guessing numbers between 1 and 100

## What I learned
- Using functions to organize code and separate concerns
- Variable scope — passing values between functions with parameters and return values
- Input validation using try/except
- Using while/else to detect when a loop ends without a break
- f-strings for formatting output

## Possible improvements
- Track a high score across multiple games
- Add difficulty levels (adjustable range or attempt count)
