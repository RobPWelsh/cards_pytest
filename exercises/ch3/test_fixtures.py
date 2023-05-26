import pytest


@pytest.fixture(scope='module')
def some_list():
    """Yields a list of 4 colors"""
    color_list = ['red', 'yellow', 'blue', 'green']
    print('This is printed before yielding color_list')
    yield color_list
    print('This is printed after yielding color_list')


@pytest.fixture()
def some_dict():
    """Returns a dictionary with 2 entries"""
    alien_0 = {'color': 'green', 'points': 5}
    return alien_0


@pytest.fixture()
def some_tuple():
    """Returns a tuple with 4 misc items"""
    misc_tuple = (3, ['tree', 'cloud'], False, {'name': 'Rob', 'ID': 1013, 'role': 'mgr'})
    return misc_tuple


def test_colors(some_list):
    """Demo the list fixture"""
    assert some_list[1] == 'yellow'


def test_add_colors(some_list):
    """Second demo of the list fixture"""
    some_list.append('orange')
    some_list.append('violet')
    assert len(some_list) == 6
    assert some_list[4] == 'orange'


def test_aliens(some_dict):
    """Demo the dictionary fixture"""
    assert len(some_dict) == 2


def test_tuple(some_tuple):
    """Demo the tuple fixture"""
    assert some_tuple[3]['ID'] == 1013
