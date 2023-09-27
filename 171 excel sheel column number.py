class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        pass

alphabet_mapping = {}
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    alphabet_mapping[letter] = i + 1

print(alphabet_mapping)