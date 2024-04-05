import os
import pytest
from main import read_file


@pytest.fixture
def file1_content():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(current_directory, 'file1.txt')
    with open(file_name, 'r') as file:
        return file.readlines()


def test_read_file(file1_content):
    assert read_file('file1.txt') == file1_content