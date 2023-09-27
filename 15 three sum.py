class Solution:
    def sort_list(self, nums):
        return nums.sort()

    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]

            if summ == target:
                return [left + 1, right + 1]
            elif summ < target:
                left += 1
            else:
                right -= 1

    def threeSum(self, nums):
        pass