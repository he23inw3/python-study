from main import product

def test_product_case1():
    assert product(3, 4) == "Even"

def test_product_case2():
    assert product(1, 21) == "Odd"