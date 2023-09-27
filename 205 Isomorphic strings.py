class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}

        for i in range(len(s)):
            # the conditions that i have to watch out for are
            if ((s[i] in s2t and s2t[s[i]] != t[i])
            or (t[i] in t2s and t2s[t[i]] != s[i])):
                return False

            # this is how i will fill in the dictionaries
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        
        # if nothing goes awful, then I will
        return True