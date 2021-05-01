from main import not_so_diverse

def test_not_so_diverse_case1():
    assert not_so_diverse(5, 2, [1, 1, 2, 2, 5]) == 1

def test_not_so_diverse_case2():
    assert not_so_diverse(4, 4, [1, 1, 2, 2]) == 0

def test_not_so_diverse_case3():
    assert not_so_diverse(10, 3, [5, 1, 3, 2, 4, 1, 1, 2, 3, 4]) == 3
