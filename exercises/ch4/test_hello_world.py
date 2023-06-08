from hello_world import hello
import pytest


# Fixture to read contents of test file
@pytest.fixture()
def read_test_contents():
    hello()
    with open("hello.txt") as f:
        return f.read()


# Test without tmp_path fixtures
def test_hello(read_test_contents):
    assert read_test_contents == "Hello World!\n"


# Create a comparison text file in a temporary directory using tmp_path and compare to file under test
def test_tmp_path(tmp_path, read_test_contents):
    tmp_dir = tmp_path / 'sub'
    tmp_dir.mkdir()
    tmp_file = tmp_dir / 'compare_text.txt'
    print(tmp_file)  # C:\Users\Rob\AppData\Local\Temp\pytest-of-Rob\pytest-1\test_tmp_path0\sub\compare_text.txt
    tmp_file.write_text("Hello World!\n")
    assert read_test_contents == tmp_file.read_text()


# Create a comparison text file in a temporary directory using tmp_path_factory and compare to file under test
def test_tmp_path_factory(tmp_path_factory, read_test_contents):
    tmp_dir_2 = tmp_path_factory.mktemp('sub_factory')
    tmp_file_2 = tmp_dir_2 / 'compare_text_2.txt'
    print(tmp_file_2)
    tmp_file_2.write_text("Hello World!\n")
    assert read_test_contents == tmp_file_2.read_text()

