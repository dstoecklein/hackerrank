import argparse
from typing import Type

def mult(a, b):
    return a * b

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args()
    print(mult(**vars(args)))