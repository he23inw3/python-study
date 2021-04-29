
def product(a: int, b: int) -> str:
    return "Even" if a * b % 2 == 0 else "Odd"

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(product(a, b))