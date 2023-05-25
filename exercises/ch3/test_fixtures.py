import pytest


@pytest.fixture()
def some_list():
    color_list = ['red', 'yellow', 'blue', 'green']
    return color_list


@pytest.fixture()
def some_dict():
    alien_0 = {'color': 'green', 'points': 5}
    return alien_0

@pytest.fixture()
def some_tuple():
    misc_tuple = (3, ['tree', 'cloud'], False, {'name': 'Rob', 'ID': 1013, 'role': 'mgr'})
    return misc_tuple


def test_colors(some_list):
    assert some_list[1] == 'yellow'


def test_aliens(some_dict):
    assert len(some_dict) == 2


def test_tuple(some_tuple):
    assert some_tuple[3]['ID'] == 1013


