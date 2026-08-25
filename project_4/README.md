# Temperature Converter
A command-line temperature converter supporting Celsius, Fahrenheit, and Kelvin.

## Features
- 6 conversion types: C→F, F→C, C→K, K→C, F→K, K→F
- Input validation for name, menu choice, and temperature value
- Conversion history log
- Personalized messages using the user's name
- Convert again option

## How to run
```bash
python temperature_converter.py
```

## Menu options
| Choice | Conversion |
|--------|-----------|
| 1 | Celsius → Fahrenheit |
| 2 | Fahrenheit → Celsius |
| 3 | Celsius → Kelvin |
| 4 | Kelvin → Celsius |
| 5 | Fahrenheit → Kelvin |
| 6 | Kelvin → Fahrenheit |

## What I learned
- Chaining conversion formulas (e.g., F→K by converting F→C→K in one expression)
- Using a dictionary to map menu choices to readable labels
- Storing calculated results in a single variable for reuse in both display and history
- Passing values between functions using parameters and return values
- Building and displaying a history log across multiple conversions
