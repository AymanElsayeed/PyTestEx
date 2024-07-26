"""

calculation module

"""


def add(number_one: (str, int, float), number_two: (str, int, float)) -> (int, float):
    """
    Add two numbers
    :param number_one: number one
    :type number_one: int or float
    :param number_two: number two
    :type number_two: int or float
    :return: sum of two numbers
    :rtype: int or float
    """
    try:
        return number_one + number_two
    except TypeError:
        return float(number_one) + float(number_two)


def sub(number_one: (str, int, float), number_two: (str, int, float)) -> (int, float):
    """
    Subtract two numbers
    :param number_one: number one
    :type number_one: int or float
    :param number_two: number two
    :type number_two: int or float
    :return: difference of two numbers
    :rtype: int or float
    """
    try:
        return number_one - number_two
    except TypeError:
        return float(number_one) - float(number_two)
