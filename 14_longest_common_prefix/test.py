import pytest
from solution import Solution

instance = Solution()


def test_case_1():
    strs = ["flower","flow","flight"]

    assert instance.longestCommonPrefix(strs) == "fl"

def test_case_2():
    strs = ["dog","racecar","car"]

    assert instance.longestCommonPrefix(strs) == ""

def test_case_3():
    strs = ["whistle", "whistle", "whistle"]

    assert instance.longestCommonPrefix(strs) == "whistle"


def test_case_no_strings_provided():
    strs = []

    with pytest.raises(ValueError) as e:
        result = instance.longestCommonPrefix(strs)
    assert "No strings provided" in str(e.value)