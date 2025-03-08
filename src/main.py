#!/usr/bin/env python3
import argparse
from random import randint

def main():
    parser = argparse.ArgumentParser(description="Generate a series of mathematical expressions.")
    parser.add_argument("n", help="number of mathematical expressions to write")
    args = parser.parse_args
    print(type(args))

if __name__ == "__main__":
    main()