from typing import List

def shift_only(n: int, a_list: List[int]) -> int:
    count = 0
    while all(a%2 == 0 for a in a_list):
        a_list = [a/2 for a in a_list]
        count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(shift_only(n, a))