class Solution:
    def majorityElement(self, nums):
        d = {}
        max_key = None
        max_count = 0

        for number in nums:
            if number not in d:
                d[number] = 1
            else:
                d[number] += 1
            
            if d[number] > max_count:
                max_key = number
                max_count = d[number]
        
        return max_key