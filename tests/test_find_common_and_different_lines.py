import pytest
from main import find_common_and_different_lines


def test_find_common_and_different_lines():
    file1_lines = ["line1\n", "line2\n", "line3\n"]
    file2_lines = ["line2\n", "line3\n", "line4\n"]
    common_lines, different_lines = find_common_and_different_lines(file1_lines, file2_lines)
    assert common_lines == {"line2\n", "line3\n"}
    assert different_lines == {"line1\n", "line4\n"}