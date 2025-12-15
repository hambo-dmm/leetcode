import pytest

from solution import Solution

instance = Solution()

test_cases = [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
    ([1], 1)
]


@pytest.mark.parametrize("nums, majority_element", test_cases)
def test_majority_element(nums, majority_element):
    assert instance.majorityElement(nums) == majority_element
