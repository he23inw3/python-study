
def two_anagrams(s: str, t: str) -> str:
    return "Yes" if sorted(list(s)) < sorted(list(t), reverse=True) else "No"

if __name__ == '__main__':
    s = input()
    t = input()
    print(two_anagrams(s, t))