from multiply import multiply

def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_zero():
    assert multiply(0, 5) == 0
