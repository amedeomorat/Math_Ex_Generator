#!/usr/bin/env python3
import argparse
from random import randint
import time

STUDENT_ID = 2359267

def main():
    parser = argparse.ArgumentParser(description="Generate a series of mathematical expressions.")
    parser.add_argument("n", help="number of mathematical expressions to write")
    args = parser.parse_args
    n = int(args.n)
    start = time.localtime()
    write_in_file(str(STUDENT_ID))
    for i in range(n):
        expression = generate_expression()
        result = eval(expression)
        final_string = expression + "=" + result
        write_in_file(final_string)
    stop = time.localtime()
    time_elapsed = stop-start

def generate_expression():
    MAX_NUMBER = 100
    MIN_NUMBER = 0
    MIN_OPERAND = 3
    MAX_OPERAND = 5
    operations = ["+","-","*","/"]
    expression = str(randint(MIN_NUMBER, MAX_NUMBER))
    operands_number = randint(MIN_OPERAND, MAX_OPERAND)
    for i in range(operands_number):
        operand = operations[randint(0,len(operations))]
        if operand == "/" and MIN_NUMBER == 0:
            number = randint(MIN_NUMBER+1,MAX_NUMBER)
        else:
            number = randint(MIN_NUMBER, MAX_NUMBER)
        expression = expression + operand + str(number)
    return expression

def write_in_file(expression):
    with open("result.txt", "a" ) as file:
        file.write(f"%s\n",expression)

if __name__ == "__main__":
    main()