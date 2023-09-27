class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        each character in the pattern must point to a unique word in the string s.
        """
        words = s.split()
        # checking the first condition
        if len(words) != len(pattern):
            return False
        
        # let's have the dictionary for pattern
        charToWord, wordToChar = {}, {}

        for char, word in zip(pattern, words):
            if ((char in charToWord and charToWord[char] != word)
                or (word in wordToChar and wordToChar[word] != char)):
                return False  
            
            charToWord[char] = word
            wordToChar[word] = char
                    
        # if nothing goes awful till here, I will
        return True