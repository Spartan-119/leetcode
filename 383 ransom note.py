class Solution:
    def canConstruct(self, ransomNote, magazine) -> bool:
        magazine_dict = {}

        for c in magazine:
            if c not in magazine_dict:
                magazine_dict[c] = 1
            else:
                magazine_dict[c] += 1

        # traverse through the ransomNote
        for char in ransomNote:
            if char not in magazine_dict or magazine_dict[char] == 0:
                return False
            else:
                magazine_dict[char] -= 1

        return True

###########
# the driver method
if __name__ == '__main__':
    s = Solution()
    ransomNote = ['a', 'aa', 'aa', 'bg', 'fihjjjjei']
    magazine = ['b', 'ab', 'aab', 'efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj', 'hjibagacbhadfaefdjaeaebgi']

    for i in range(len(ransomNote)):
        print(s.canConstruct(ransomNote[i], magazine[i]))