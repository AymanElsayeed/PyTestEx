"""

This file contains fixtures that are used in the test cases.

"""
from pytest import fixture


@fixture(scope="session", params=[(2, 1, 1), (3, 2, 1)])
def data_to_add(request):
    """
    Fixture for add function
    :param request: request object
    :return: tuple of parameters for add function
    """
    yield request.param


@fixture(scope="session", params=[(2, 3, 1), (3, 4, 1)])
def data_to_sub(request):
    """
    Fixture for sub function
    :param request: request object
    :return: tuple of parameters for sub function
    """
    yield request.param
