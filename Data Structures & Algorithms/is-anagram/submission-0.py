class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for character in s:
            count_s[character] = count_s.get(character,0) + 1
        for character in t:
            count_t[character] = count_t.get(character, 0) + 1
        return count_s == count_t