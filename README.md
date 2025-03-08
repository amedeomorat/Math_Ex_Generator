# Mathematical Expression Generator

A simple command-line tool that generates random mathematical expressions along with their calculated results.

## Description

This tool creates a specified number of random mathematical expressions using operations like addition, subtraction, multiplication, and division. Each expression is displayed along with its exact calculated result.

Example output:
```
33/36+98/34-44=-40.2
85/60-9-27+23+33=21.42
39/31*5*2+64=76.58
```

## Requirements

- Python 3.6 or higher
- Windows, macOS, or Linux

## Installation

1. Clone this repository or download the source code:
```
git clone https://github.com/amedeomorat/Math_Ex_Generator
```

2. Navigate to the project directory:
```
cd expression-generator
```

## Usage

### Windows

Run the program using the provided batch file:
```
.\bin\gen_ex.bat [number-of-expressions]
```

Example:
```
.\bin\gen_ex.bat 10
```
This will generate 10 random mathematical expressions.

### macOS/Linux

Run the program using Python directly:
```
python src/main.py [number-of-expressions]
```

Or use the shell script (may need to grant execute permissions first):
```
chmod +x bin/gen_ex.sh
./bin/gen_ex.sh [number-of-expressions]
```

## Examples

Generate 5 expressions:
```
.\bin\gen_ex.bat 5
```

Output might look like:
```
45/12+67-34*2=-0.25
98+23/46-12=89.5
34*5-67+12=115
56/8+23-45=-16
78*3+45/9=239
```
