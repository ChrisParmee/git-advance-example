from pythoncalculator.longr import add,divide,multiply


def test_add():
    assert add(1, 3) == 7

    from pythoncalculator import divide

def test_divide():
    assert divide(10, 2) == 5

def test_multiply():
    assert multiply(10, 3) == 30