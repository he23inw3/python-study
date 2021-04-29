from main import shift_only

def test_shift_only_case1():
    assert shift_only(3, [8, 12, 40]) == 2

def test_shift_only_case2():
    assert shift_only(4, [5, 6, 8, 10]) == 0

def test_shift_only_case3():
    assert shift_only(6, [382253568, 723152896, 37802240, 379425024, 404894720, 471526144]) == 8