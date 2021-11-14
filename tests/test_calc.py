from src.calc import add, sub


def test_add():
    result = add(1, '1')
    assert result == 2
    assert 2 == add(1, 1)


def test_sub():
    result = sub(2, '1')
    assert result == 1
    assert 1 == sub(2, 1)
