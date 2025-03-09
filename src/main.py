#!/usr/bin/env python3
import argparse
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()
STUDENT_ID = os.getenv("STUDENT_ID")

FILE_PATH = "..\\result.txt"

MAX_NUMBER = 100
MIN_NUMBER = 0
MIN_OPERAND = 3
MAX_OPERAND = 5

def main():
    parser = argparse.ArgumentParser(description="Generate a series of mathematical expressions.")
    parser.add_argument("n", help="number of mathematical expressions to write")
    args = parser.parse_args()
    n = int(args.n)
    if not validate_n(n):
        print("The number of expression must be at least 1.")
        quit()
    clear_file()
        
    write_in_file(str(STUDENT_ID))
    for i in range(n):
        expression = generate_expression()
        result = str(round(eval(expression),2))
        final_string = expression + "=" + result
        write_in_file(final_string)

def validate_n(n):
    if n<=0:
        return False
    else:
        return True

def clear_file():
    with open(FILE_PATH, "w") as file:
        file.write("")

def generate_expression():
    operations = ["+","-","*","/"]
    expression = str(randint(MIN_NUMBER, MAX_NUMBER))
    operands_number = randint(MIN_OPERAND, MAX_OPERAND)
    for i in range(operands_number):
        operand = operations[randint(0,len(operations)-1)]
        if operand == "/" and MIN_NUMBER == 0:
            number = randint(MIN_NUMBER+1,MAX_NUMBER)
        else:
            number = randint(MIN_NUMBER, MAX_NUMBER)
        expression = expression + operand + str(number)
    return expression

def write_in_file(expression):
    with open(FILE_PATH, "a" ) as file:
        file.write(expression + "\n")

if __name__ == "__main__":
    main()