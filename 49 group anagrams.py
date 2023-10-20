class Solution:
    """
    you could create 3 methods:
    method1 - to find the valid anagrams
    method2 - to find if a string is in the final result list
    method3 - to apply method1 and method2 to this to find group anagrams
    """
    def isAnagram(self, s, t) -> bool:
        if len(s) != len(t):
            return False
        
        sdict, tdict = {}, {}
        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]] += 1

            if t[i] not in tdict:
                tdict[t[i]] = 1
            else:
                tdict[t[i]] += 1

        # now we check if both the dictionaries are identical or not
        if sdict == tdict:
            return True
        else:
            return False

    def isPresent(self, string, result_list) -> bool:
        found = False
        for sublist in result_list:
            if string in sublist:
                found = True
        
        if found: return True
        else: return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        result = []

        for left in range(len(strs)):
            temp_list = []
            # if this string is already in the result list
            if self.isPresent(strs[left], result):
                continue
            temp_list.append(strs[left])
            for right in range(left + 1, len(strs)):
                if self.isAnagram(strs[left], strs[right]):
                    #temp_list.append(strs[left])
                    temp_list.append(strs[right])
            result.append(temp_list)
            # returning all the elements from the python list
            #temp_list.clear()
        
        return result
        