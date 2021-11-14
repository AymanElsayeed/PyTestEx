from src.calc import add, sub
import pytest


def test_add():
    result = add(1, '1')
    assert result == 2
    assert 2 == add(1, 1)


def test_sub():
    result = sub(2, '1')
    assert result == 1
    assert 1 == sub(2, 1)


@pytest.mark.parametrize("expected_result,a,b", [(2, 1, 1), (3, 2, 1)])
def test_add_param(expected_result, a, b):
    result = add(a, b)
    assert result == expected_result


@pytest.mark.parametrize("expected_result,a,b", [(2, 3, 1), (3, 4, 1)])
def test_sub_param(expected_result, a, b):
    result = sub(a, b)
    assert result == expected_result


def test_add_fixture(data_to_add):
    expected_result, a, b = data_to_add
    result = add(a, b)
    assert result == expected_result


def test_sub_fixture(data_to_sub):
    expected_result, a, b = data_to_sub
    result = sub(a, b)
    assert result == expected_result
