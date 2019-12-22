class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring_count = 0
        for start in range(len(s) - minSize + 1):
            for end in range(start + minSize - 1, start + maxSize):
                substring = s[start:end+1]
                letters_num = len(set(substring))
                if letters_num <= maxLetters:
                    substring_count += 1
                else:
                    break
        return substring_count
