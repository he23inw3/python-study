from typing import List
from collections import Counter, deque

def not_so_diverse(n: int, k: int, a_list: List[int]) -> int:
    a_list = Counter(a_list)
    a_list = [tuple(i) for i in a_list.items()]
    a_list.sort(key=lambda x: x[1])
    a_list = deque(a_list)
    result = 0
    while k < len(a_list):
        result += a_list.popleft()[1]
    return result

if __name__ == '__main__':
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    print(not_so_diverse(n, k, a_list))
