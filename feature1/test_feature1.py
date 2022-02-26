from feature1 import add


def test_add():
    assert add(1, 2) == 3
    assert add(10000, 1) == 10001