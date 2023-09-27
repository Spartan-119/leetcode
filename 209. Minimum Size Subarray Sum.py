from typing import *

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # giving the maximum value to the min_sum as a starting point
        min_sum = float('inf')
        current_sum = 0            
        start, end = 0, 0

        while end < len(nums):
            # the first edge case where
            # the item on the start index is >= target
            if nums[start] >= target:
                return 1
            # in every other case of course
            # you may want to expand the window by moving the end pointer to 
            # the right in the hope that your condition is met.
            end += 1
            sub_array = nums[start: end + 1]
            