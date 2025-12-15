from typing import List
import math


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #return self._single_number_using_set(nums)
        return self._single_number_using_xor(nums)


    def _single_number_using_set(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

    def _single_number_using_xor(self, nums):
        a = 0
        for num in nums:
            a ^= num

        return a