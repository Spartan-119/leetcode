class Solution:
    # this is the O(n ** 2) time complexity
    def twoSum1(self, numbers, target):
        for left in range(len(numbers)):
            for right in range(left + 1, len(numbers)):
                diff = target - numbers[left]
                if diff == numbers[right]:
                    return [left + 1, right + 1]
    
    # this is the second way, a more optimal way of doing it.
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

# Driver method to test the Solution class
def main():
    solution = Solution()

    # Test case 1 for twoSum1
    numbers1 = [2, 3, 4, 5]
    target1 = 6
    result1 = solution.twoSum(numbers1, target1)
    print("Result for twoSum:", result1)  # Expected output: [1, 2]

    # Test case 2 for twoSum
    numbers2 = [2, 7, 11, 15]
    target2 = 9
    result2 = solution.twoSum(numbers2, target2)
    print("Result for twoSum:", result2)  # Expected output: [1, 2]

if __name__ == "__main__":
    main()