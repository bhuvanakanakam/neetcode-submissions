class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # approach 1 - 2 dicts, O(n) but space is going to be more
        # count_s = {}
        # count_t = {}
        # for character in s:
        #     count_s[character] = count_s.get(character,0) + 1
        # for character in t:
        #     count_t[character] = count_t.get(character, 0) + 1
        # return count_s == count_t

        count = {}
        for character in s:
            count[character] = count.get(character,0) + 1
        for character in t:
            if count.get(character,0) == 0:
                return False
            count[character] -= 1
        return True