from typing import List
from math import ceil

def round_up_the_mean(a: int, b: int) -> int:
    return ceil((a+b)/2)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(round_up_the_mean(a, b))