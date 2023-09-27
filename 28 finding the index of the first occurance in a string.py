class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check for edge case where needle is an empty string
        if not needle:
            return 0
        
        # If needle is longer than haystack, it cannot be found
        if len(needle) > len(haystack):
            return -1
        
        # Iterate through the haystack string
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring of haystack matches needle
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # If needle is not found in haystack
        return -1