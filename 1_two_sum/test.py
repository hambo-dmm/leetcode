import pytest
from solution import Solution

instance = Solution()

def test_case_1():
    nums = [2,7,11,15]
    target = 9
    result = instance.twoSum(nums, target)

    assert set(result) == set([0,1])


def test_case_2():
    nums = [4,1,11,3]
    target = 7
    result = instance.twoSum(nums, target)

    assert set(result) == set([0,3])

def test_case_no_valid_indices():
    nums = [2,7,11,15]
    target = 32

    with pytest.raises(Exception) as e:
        result = instance.twoSum(nums, target)
    assert "No two indices sum to target" in str(e.value)