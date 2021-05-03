from main import two_anagrams

def test_two_anagrams_case1():
    assert two_anagrams("yx", "axy") == "Yes"

def test_two_anagrams_case2():
    assert two_anagrams("ratcode", "atlas") == "Yes"

def test_two_anagrams_case3():
    assert two_anagrams("cd", "bbc") == "No"

def test_two_anagrams_case4():
    assert two_anagrams("w", "ww") == "Yes"

def test_two_anagrams_case5():
    assert two_anagrams("zzz", "zzz") == "No"
