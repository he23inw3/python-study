from main import round_up_the_mean

def test_round_up_the_mean_case1():
    assert round_up_the_mean(1, 3) == 2

def test_round_up_the_mean_case2():
    assert round_up_the_mean(7, 4) == 6

def test_round_up_the_mean_case3():
    assert round_up_the_mean(5, 5) == 5

