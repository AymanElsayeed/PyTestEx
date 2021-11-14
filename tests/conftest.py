from pytest import fixture


@fixture(scope="session", params=[(2, 1, 1), (3, 2, 1)])
def data_to_add(request):
    yield request.param


@fixture(scope="session", params=[(2, 3, 1), (3, 4, 1)])
def data_to_sub(request):
    yield request.param
